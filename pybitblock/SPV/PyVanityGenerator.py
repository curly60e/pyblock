##PyBLOCK Vanity Generator##

from vanity_address.vanity_address import VanityAddressGenerator
from pprint import pprint
import signal
import sys
signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))

def callback(address):
    return address.startswith(b'1X')
          #address.slice(1).startsWith('X')
          #address.endsWith('X')
          #address.includes('X')
address = VanityAddressGenerator.generate_one(callback=callback)
print("Address:\t{address.address}\nPrivate key:\t{address.private_key}".format(address=address))
