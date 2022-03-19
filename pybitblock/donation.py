#Developer: Curly60e
#PyBLOCK its a clock of the Bitcoin blockchain.


import requests
import qrcode
import pickle
from nodeconnection import *

def donationAddr():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    url = 'bc1qjzaz34nv2ev55vfdu9m5qh0zq0fwcn6c7pkcrv'
    print("\033[1;30;47m")
    qr.add_data(url)
    qr.print_ascii()
    print("\033[0;37;40m")
    qr.clear()
    print(f"Bitcoin Address Bech32: {url}")

def donationPayNym():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    url = 'PM8TJhNTTq3YVocXuPtLjKx7pKkdUxqwTerWJ2j2a7dNitgyMmBPN6gK61yE17N2vgvQvKYokXktt6D6GZFTmocvDJhaUJfHt7ehEMmthjsT3NQHseFM'
    print("\033[1;30;47m")
    qr.add_data(url)
    qr.print_ascii()
    print("\033[0;37;40m")
    qr.clear()
    print(f"PayNym: {url}")

#Dev LN
def donationLN():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    url = 'pyblock@zbd.gg'
    print("\033[1;30;47m")
    qr.add_data(url)
    qr.print_ascii()
    print("\033[0;37;40m")
    qr.clear()
    print(f"Lightning Address: {url}")

#Tester Address
def donationAddrTst():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    url = 'bc1qwtzwu2evtchkvnf3ey6520yprsyv7vrjvhula5'
    print("\033[1;30;47m")
    qr.add_data(url)
    qr.print_ascii()
    print("\033[0;37;40m")
    qr.clear()
    print(f"Bitcoin Address Bech32: {url}")

#Tester LN
def donationLNTst():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    url = 'sn@getalby.com'
    print("\033[1;30;47m")
    qr.add_data(url)
    qr.print_ascii()
    print("\033[0;37;40m")
    qr.clear()
    print(f"Lightning Address: {url}")

def decodeQR():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    url = input("Insert your Bitcoin Address to show the QRCode: ")
    print("\033[1;30;47m")
    qr.add_data(url)
    qr.print_ascii()
    print("\033[0;37;40m")
    qr.clear()
    print(f"Bitcoin Address: {url}")
