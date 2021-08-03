#!/usr/bin/env python

from usb.core import find as finddev

import os
import codecs, time, logging, usb
from lib import common

# Parse command line arguments and initialize the radio
common.init_args('./nrf24-scanner.py')
common.parser.add_argument('-p', '--prefix', type=str, help='Promiscuous mode address prefix', default='')# opt : add the prefix of the address
common.parser.add_argument('-d', '--dwell', type=float, help='Dwell time per channel, in milliseconds', default='100') # the seconds for changing channels to scan
common.parse_and_init() # function to parse and create the common object

# Parse the prefix addresses
prefix_address = codecs.decode(common.args.prefix.replace(':', ''), 'hex') # decoding the address if entered
if len(prefix_address) > 5:
  raise Exception('Invalid prefix address: {0}'.format(args.address))

# Put the radio in promiscuous mode - if address typed add the address to the promi mode
common.radio.enter_promiscuous_mode(prefix_address)

# Convert dwell time from milliseconds to seconds
dwell_time = common.args.dwell / 1000

# Set the initial channel
common.radio.set_channel(common.channels[0])

# Sweep through the channels and decode ESB packets in pseudo-promiscuous mode
last_tune = time.time()
first_time = time.time()
channel_index = 0
addresses_index = []
# Scan for 30 seconds to find devices near.
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
    if ':'.join('{:02X}'.format(b) for b in address) not in addresses_index:
    	addresses_index.append(':'.join('{:02X}'.format(b) for b in address))
    # Log the packet
    logging.info('{0: >2}  {1: >2}  {2}  {3}'.format(
              common.channels[channel_index],
              len(payload),
              ':'.join('{:02X}'.format(b) for b in address),
              ':'.join('{:02X}'.format(b) for b in payload)))

#reseting the usb device, cancelling the unplug needed, and for continous operations        
dev = finddev(idVendor=0x1915, idProduct=0x0102) # the id's can be found in lsusb -v in terminal
dev.reset()
time.sleep(2)
if len(addresses_index) > 0:
	ans = input("do you want to attack the device?  Y/N ")
	# If the user want to attack he enters the number of the victim address and and start the attack script.
	if ans == "Y" or "y":
		i = 1
		for adr in addresses_index:
			print(str(i)+"." + adr)
			i+=1
		address = addresses_index[int(input("input the address you want to sniff and attack: "))-1]
		os.system("python3 ./nrf24-attack.py -a {0}".format(address))
	else:
		print("Goodbye")
else:
	print("No devices found, try to restart the program")
	dev = finddev(idVendor=0x1915, idProduct=0x0102) # the id's can be found in lsusb -v in terminal
	dev.reset()
	time.sleep(2)
