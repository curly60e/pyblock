import base64, codecs, json, requests
import pickle
import os
import os.path
import qrcode
import time as t
from pblogo import *

lndconnectload = ''

if os.path.isfile('blndconnect.conf'):
    lndconnectData = pickle.load(open("blndconnect.conf", "rb"))
    lndconnectload = str(lndconnectData)
else:
    ipport1 = input("Insert IP:PORT to your node: ")
    pickle.dump(ipport1, open("blndconnect.conf", "wb"))
    

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

def listchaintxns():
    url = 'https://{}/v1/transactions'.format(lndconnectload)
    r = requests.get(url, headers=headers, verify=cert_path)
    a = r.json()
    b = str(a)
    c = b.split(',')
    d = c
    for d in c:
        print(d)
    
def listinvoice():
    url = 'https://{}/v1/invoices'.format(lndconnectload)
    r = requests.get(url, headers=headers, verify=cert_path)
    a = r.json()
    b = str(a)
    c = b.split(',')
    d = c
    for d in c:
        print(d)

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
        
def clear(): # clear the screen
    os.system('cls' if os.name=='nt' else 'clear')



