##PyBLOCK Vanity Generator##

from vanity_address.vanity_address import VanityAddressGenerator
from pprint import pprint

def callback(address):
    return address.startswith(b'1X')
address = VanityAddressGenerator.generate_one(callback=callback)
print("Address:\t{address.address}\nPrivate key:\t{address.private_key}".format(address=address))
