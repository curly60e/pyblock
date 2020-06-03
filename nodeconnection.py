#Developer: Curly60e
#PyBLOCK its a clock of the Bitcoin blockchain.
#Version: 0.3.0

import base64, codecs, json, requests
import pickle
import os
import os.path
import qrcode
import time as t
from pblogo import *

lndconnectload = ''

if os.path.isfile('blndconnect.conf'): # Check if the file 'bclock.conf' is in the same folder
    lndconnectData = pickle.load(open("blndconnect.conf", "rb")) # Load the file 'bclock.conf'
    lndconnectload = lndconnectData # Copy the variable pathv to 'path'

else:
    lndconnectload = input("Insert IP:PORT to your node: ") # path to the bitcoin-cli
    pickle.dump(lndconnectload, open("blndconnect.conf", "wb")) # Save the file 'bclock.conf'


cert_path = 'tls.cert'
macaroon = codecs.encode(open('admin.macaroon', 'rb').read(), 'hex')
headers = {'Grpc-Metadata-macaroon': macaroon}


def getnewinvoice():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    url = 'https://{}/v1/invoices'.format(lndconnectload)
    data = { 

        }
    r = requests.post(url, headers=headers, verify=cert_path, data=json.dumps(data))
    a = r.json()
    print("\033[1;30;47m")
    qr.add_data(a['payment_request'])
    qr.print_ascii()
    print("\033[0;37;40m")
    print("Lightning Invoice: " + a['payment_request'])
    b = str(a['payment_request'])
    while True:
        url = 'https://{}/v1/payreq/{}'.format(lndconnectload, b)
        r = requests.get(url, headers=headers, verify=cert_path)
        a = r.json()
        url = 'https://{}/v1/invoice/{}'.format(lndconnectload,a['payment_hash'])
        rr = requests.get(url, headers=headers, verify=cert_path)
        m = rr.json()
        if m['state'] == 'SETTLED':
            print("\033[1;32;40m")
            clear()
            blogo()
            tick()
            print("\033[0;37;40m")
            t.sleep(2)
            break
        elif m['state'] == 'CANCELED':
            print("\033[1;31;40m")
            clear()
            blogo()
            canceled()
            print("\033[0;37;40m")
            t.sleep(2)
            break

    
def getnewaddress():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    url = 'https://{}/v1/newaddress'.format(lndconnectload)
    r = requests.get(url, headers=headers, verify=cert_path)
    addr = r.json()
    print("\033[1;30;47m")
    qr.add_data(addr['address'])
    qr.print_ascii()
    print("\033[0;37;40m")
    print("Bitcoin Address: " + addr['address'])
    cnt = input("Continue? Y: ")
    if cnt == "Y" or cnt == "y":
        t.sleep(1)
        
def listchaintxns():
    url = 'https://{}/v1/transactions'.format(lndconnectload)
    r = requests.get(url, headers=headers, verify=cert_path)
    a = r.json()
    b = str(a)
    c = b.split(',')
    d = c
    for d in c:
        print(d)
    cnt = input("Continue? Y: ")
    if cnt == "Y" or cnt == "y":
        t.sleep(1)
    
def listinvoice():
    url = 'https://{}/v1/invoices'.format(lndconnectload)
    r = requests.get(url, headers=headers, verify=cert_path)
    a = r.json()
    b = str(a)
    c = b.split(',')
    d = c
    for d in c:
        print(d)
    cnt = input("Continue? Y: ")
    if cnt == "Y" or cnt == "y":
        t.sleep(1)
        
def invoicesettle():
    invoice = input("Insert the invoice: ")
    while True:
        url = 'https://{}/v1/payreq/{}'.format(lndconnectload, invoice)
        r = requests.get(url, headers=headers, verify=cert_path)
        a = r.json()
        url = 'https://{}/v1/invoice/{}'.format(lndconnectload,a['payment_hash'])
        rr = requests.get(url, headers=headers, verify=cert_path)
        m = rr.json()
        if m['state'] == 'SETTLED':
            print("\033[1;32;40m")
            clear()
            blogo()
            tick()
            print("\033[0;37;40m")
            t.sleep(2)
            break
        elif m['state'] == 'CANCELED':
            print("\033[1;31;40m")
            clear()
            blogo()
            canceled()
            print("\033[0;37;40m")
            t.sleep(2)
            break


def getinfo():
    url = 'https://{}/v1/getinfo'.format(lndconnectload)
    r = requests.get(url, headers=headers, verify=cert_path)
    a = r.json()
    b = str(a)
    c = b.split(',')
    d = c
    for d in c:
        print(d)
    cnt = input("Continue? Y: ")
    if cnt == "Y" or cnt == "y":
        t.sleep(1)
        
def channels():
    url = 'https://{}/v1/channels'.format(lndconnectload)    
    r = requests.get(url, headers=headers, verify=cert_path)
    a = r.json()
    b = str(a)
    c = b.split(',')
    d = c
    for d in c:
        print(d)
    cnt = input("Continue? Y: ")
    if cnt == "Y" or cnt == "y":
        t.sleep(1)
        
def balanceOC():
    url = 'https://{}/v1/balance/blockchain'.format(lndconnectload)
    r = requests.get(url, headers=headers, verify=cert_path)
    a = r.json()
    print("Total Balance: " + a['total_balance'] + " sats")
    print("Confirmed Balance: " + a['confirmed_balance'] + " sats")
    print("Unconfirmed Balance: " + a['unconfirmed_balance'] + " sats")
    cnt = input("Continue? Y: ")
    if cnt == "Y" or cnt == "y":
        t.sleep(1)

def clear(): # clear the screen
    os.system('cls' if os.name=='nt' else 'clear')

