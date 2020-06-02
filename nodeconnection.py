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
    b = str(a)
    c = b.split(':')
    d = c[2]
    e = d.strip(" '")
    f = str(e)
    g = f.split(',')
    h = g[0]
    hh = h.strip("' ")
    print("\033[1;30;47m")
    qr.add_data(hh)
    qr.print_ascii()
    print("\033[0;37;40m")
    print("Lightning Invoice: " + hh)
    while True:
        url = 'https://{}/v1/payreq/{}'.format(lndconnectload,hh)
        r = requests.get(url, headers=headers, verify=cert_path)
        a = r.json()
        b = str(a)
        c = b.split(',')
        d = c[1]
        e = str(d)
        f = e.split(':')
        g = f[1]
        h = g.strip(" '")
        i = str(h)
        url = 'https://{}/v1/invoice/{}'.format(lndconnectload,i)
        rr = requests.get(url, headers=headers, verify=cert_path)
        m = rr.json()
        n = str(m)
        p = n.split(',')
        o = p[20]
        if 'SETTLED' in o:
            print("\033[1;32;40m")
            clear()
            blogo()
            tick()
            print("\033[0;37;40m")
            t.sleep(2)
            break
        elif 'CANCELED' in o:
            print("\033[1;31;40m")
            clear()
            blogo()
            canceled()
            print("\033[0;37;40m")
            t.sleep(2)
            break
    cnt = input("Continue? Y: ")
    if cnt == "Y" or cnt == "y":
        t.sleep(1)
    
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
    addre = str(addr)
    addres = addre.split(':')
    address = addres[1]
    addressb = str(address)
    addressbc = addressb.split('}')
    addressbc1 = addressbc[0]
    addressrm = str(addressbc1)
    addressrm1 = addressrm.split(',')
    a = addressrm1[0]
    b = a.replace("'", "")
    print("\033[1;30;47m")
    qr.add_data(b)
    qr.print_ascii()
    print("\033[0;37;40m")
    print("Bitcoin Address: " + b)
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
        url = 'https://{}/v1/payreq/{}'.format(lndconnectload,invoice)
        r = requests.get(url, headers=headers, verify=cert_path)
        a = r.json()
        b = str(a)
        c = b.split(',')
        d = c[1]
        e = str(d)
        f = e.split(':')
        g = f[1]
        h = g.strip(" '")
        i = str(h)
        url = 'https://{}/v1/invoice/{}'.format(lndconnectload,i)
        rr = requests.get(url, headers=headers, verify=cert_path)
        m = rr.json()
        n = str(m)
        p = n.split(',')
        o = p[20]
        if 'SETTLED' in o:
            print("\033[1;32;40m")
            clear()
            blogo()
            tick()
            print("\033[0;37;40m")
            t.sleep(2)
            break
        elif 'CANCELED' in o:
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

def clear(): # clear the screen
    os.system('cls' if os.name=='nt' else 'clear')
