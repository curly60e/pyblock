#Developer: Curly60e
#PyBLOCK its a clock of the Bitcoin blockchain.
#Version: 0.5.0

import base64, codecs, json, requests
import pickle
import os
import os.path
import qrcode
import simplejson as json
import time as t
from art import *
from pblogo import *

def clear(): # clear the screen
    os.system('cls' if os.name=='nt' else 'clear')

#-----------------------------LNBITS--------------------------------
def loadFileConnLNBits():
    lnbitLoad = {"wallet_name":"", "wallet_id":"", "admin_key":"", "invoice_read_key":""}

    clear()
    blogo()
    print("""\n\tATENTION: YOU ARE GOING TO CREATE A FILE WITH YOUR INFORMATION OF CONNECTION TO LNBITS.COM.
               WE WILL NEED SOME INFORMATION FROM YOUR ACCOUNT THAT THE ONLY ONE THAT WILL HAVE ACCESS IS YOU.
                      IF YOU DELETE THIS FILE YOU WILL NEED TO PAY AGAIN TO GET ACCESS FROM PyBLOCK.
                                       SAVE THE FILE 'lnbti.conf' IN A SAFE PLACE.\n
    """)
    lnbitLoad["wallet_name"] = input("Wallet name: ") # path to the bitcoin-cli
    lnbitLoad["wallet_id"] = input("Wallet ID: ")
    lnbitLoad["admin_key"] = input("Admin key: ")
    lnbitLoad["invoice_read_key"] = input("Invoice/read key: ")
    pickle.dump(lnbitLoad, open("lnbit.conf", "wb"))

def lnbitCreateNewInvoice():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    lnbitLoad = {"wallet_name":"", "wallet_id":"", "admin_key":"", "invoice_read_key":""}

    if os.path.isfile('lnbit.conf'): # Check if the file 'bclock.conf' is in the same folder
        lnbitData= pickle.load(open("lnbit.conf", "rb")) # Load the file 'bclock.conf'
        lnbitLoad = lnbitData # Copy the variable pathv to 'path'

    amt = input("Amount: ")
    memo = input("Memo: ")
    curl = 'curl -X POST https://lnbits.com/api/v1/payments -d ' + "'{" + '"out": false,' + '"amount":' + amt + ',' + '"memo":' + ' "' + memo + '"' + "}'" + ' -H "X-Api-Key: ' + lnbitLoad['invoice_read_key'] + '"' + ' -H "Content-type: application/json"'
    sh = os.popen(curl).read()
    n = str(sh)
    d = json.loads(n)
    q = d['payment_request']
    c = q.lower()
    print("\033[1;30;47m")
    qr.add_data(c)
    qr.print_ascii()
    print("\033[0;37;40m")
    print("Lightning Invoice: " + c)

lnbitCreateNewInvoice()
#-----------------------------END LNBITS--------------------------------
