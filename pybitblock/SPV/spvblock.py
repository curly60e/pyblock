#Developer: Curly60e
#Tester: __B__T__C__
#ℙ𝕪𝔹𝕃𝕆ℂ𝕂 𝕚𝕥𝕤 𝕒 𝔹𝕚𝕥𝕔𝕠𝕚𝕟 𝔻𝕒𝕤𝕙𝕓𝕠𝕒𝕣𝕕 𝕨𝕚𝕥𝕙 ℂ𝕪𝕡𝕙𝕖𝕣𝕡𝕦𝕟𝕜 𝕒𝕖𝕤𝕥𝕙𝕖𝕥𝕚𝕔.

import os
import os.path
import time as t
import pickle
import psutil
import qrcode
import random
import xmltodict
import sys
import subprocess
import requests
import json
import simplejson as json
import numpy as np
from cfonts import render, say
from clone import *
from donation import *
from feed import *
from art import *
from logos import *
from sysinf import *
from pblogo import *
from apisnd import *
from termcolor import colored, cprint
from terminal_matrix.matrix import *
from PIL import Image
from robohash import Robohash
from lnpay_py.wallet import LNPayWallet
from pycoingecko import CoinGeckoAPI
from binascii import unhexlify
from embit import bip39
from embit.wordlists.bip39 import WORDLIST


version = "2.0.11"

settings = {"gradient":"", "design":"block", "colorA":"green", "colorB":"yellow"}
settingsClock = {"gradient":"", "colorA":"green", "colorB":"yellow"}

def close():
    print("<<< Ctrl + C.\n\n")

def sysinfo():  #Cpu and memory usage
    print("    \033[0;37;40m----------------------")
    print("    \033[3;33;40mCPU Usage: \033[1;32;40m" + str(psutil.cpu_percent()) + "%\033[0;37;40m")
    print(
        f"    \033[3;33;40mMemory Usage: \033[1;32;40m{int(psutil.virtual_memory().percent)}% \033[0;37;40m"
    )

    print("    \033[0;37;40m----------------------")

def tmp():
    t.sleep(15)

def rectangle(n):
    x = n - 3
    y = n - x
    [
        print(''.join(i))
        for i in
        (
            ''*x
            if i in (0,y-1)
            else
            (
                f'{""*n}{"|"*n}{""*n}'
                if i >= (n+1)/2 and i <= (1*n)/2
                else
                f'\u001b[38;5;27m{"█"*(x-1)}'
            )
            for i in range(y)
        )
    ]

def counttxs():
    try:
        rr = requests.get('https://mempool.space/api/blocks/tip/height')
        rr.headers['Content-Type']
        qs = rr.text
        din = json.loads(qs)
        an = din
        bs = str(an)
        a = bs
        r = requests.get("https://bitcoinexplorer.org/api/mempool/count")
        r.headers['Content-Type']
        n = r.text
        di = json.loads(n)
        s = di
        e = int(s)
        n = e / 10
        nn = n
        clear()
        outputtxs = render(
            f'{e} txs',
            colors=[settingsClock['colorA'], settingsClock['colorB']],
            align='center',
            font='tiny',
        )

        print("\x1b[?25l" + outputtxs)
        shq = int(n)
        ss = str(rectangle(shq))
        qq = ss.replace("None","")
        print(f"\033[A{qq}\033[A")
        while True:
            x = a
            rr = requests.get('https://mempool.space/api/blocks/tip/height')
            rr.headers['Content-Type']
            qs = rr.text
            din = json.loads(qs)
            an = din
            bs = str(an)
            r = requests.get("https://bitcoinexplorer.org/api/mempool/count")
            r.headers['Content-Type']
            n = r.text
            di = json.loads(n)
            s = di
            e = int(s)
            n = e / 10
            if e > nn:
                clear()
                outputtxs = render(
                    f'{e} txs',
                    colors=[settingsClock['colorA'], settingsClock['colorB']],
                    align='center',
                    font='tiny',
                )

                print("\x1b[?25l" + outputtxs)
                shq = int(n)
                ss = str(rectangle(shq))
                qq = ss.replace("None","")
                print(f"\033[A{qq}\033[A")
                nn = e
            if bs > a:
                rr = requests.get('https://mempool.space/api/blocks/tip/height')
                rr.headers['Content-Type']
                qs = rr.text
                din = json.loads(qs)
                an = din
                bs = str(an)
                r = requests.get("https://bitcoinexplorer.org/api/mempool/count")
                print("\n\n\n")
                output = render(
                    bs,
                    colors=[settingsClock['colorA'], settingsClock['colorB']],
                    align='center',
                    font='tiny',
                )

                print("\a\x1b[?25l" + output)
                t.sleep(5)
                clear()
                a = bs
                nn = e
    except:
        pass

def blogo():

    if os.path.isfile('config/pyblocksettinconfig/gs.conf') or os.path.isfile('config/pyblocksettings.conf'): # Check if the file 'bclock.conf' is in the same folder
        settingsv = pickle.load(open("config/pyblocksettings.conf", "rb")) # Load the file 'bclock.conf'
        settings = settingsv # Copy the variable pathv to 'path'
    else:
        settings = {"gradient":"", "design":"block", "colorA":"green", "colorB":"yellow"}
        pickle.dump(settings, open("config/pyblocksettings.conf", "wb"))

    if settings["gradient"] == "grd":
        output = render('PyBLOCK', gradient=[settings['colorA'], settings['colorB']], align='left', font=settings['design'])
    else:
        output = render('PyBLOCK', colors=[settings['colorA'], settings['colorB']], align='left', font=settings['design'])

    print(output)

def tick():
    print("""\033[1;32;40m




                             @
                              @
                               @
                               @@
                                @@
                                @@@
                            @@@  @@.
                             @@@@@@@
                             @@@@@@@@
                              @@@@
                               @@@@
                           @    @@@@
                            @@@@@@@@
                             @@@@@@@@
                              @@@
                               @@@
                                @@
                                 @@
                                   @
                                    @






\033[0;37;40m""")

def canceled():
    print("""
                   )              (         (
   (     (      ( /(    (         )\ )      )\ )
   )\    )\     )\())   )\   (   (()/(  (  (()/(
 (((_)((((_)(  ((_)\  (((_)  )\   /(_)) )\  /(_))
 )\___ )\ _ )\  _((_) )\___ ((_) (_))  ((_)(_))_
((/ __|(_)_\(_)| \| |((/ __|| __|| |   | __||   \
 | (__  / _ \  | .` | | (__ | _| | |__ | _| | |) |
  \___|/_/ \_\ |_|\_|  \___||___||____||___||___/

""")



def logoA():
    print("""\n\n\033[1;33;40m
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*****@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@****************************#@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@***************************************@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@***********************************************@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@*****************************************************@@@@@@@@@@@@@
    @@@@@@@@@@@***********************************************************@@@@@@@@@@
    @@@@@@@@@******************************    *****************************@@@@@@@@
    @@@@@@@*******************************     ***     ***********************@@@@@@
    @@@@@@**********************    .****     ****    *************************@@@@@
    @@@@***********************                ,*     **************************@@@@
    @@@****************************                    ***************************@@
    @@******************************        *.              **********************#@
    @@*****************************         ********          *********************@
    @******************************        ***********        **********************
    @*****************************        ***********         **********************
    @*****************************                           ***********************
    *****************************                         **************************
    @***************************        ********           *************************
    @***************************        ***********.         ***********************
    @*********************  ***        *************         ***********************
    @@*******************              ************          **********************@
    @@********************                                  **********************@@
    @@@**************************                         ,***********************@@
    @@@@#***********************     ***     *.       **************************@@@@
    @@@@@@*********************     ****    ***********************************@@@@@
    @@@@@@@****************************     **********************************@@@@@@
    @@@@@@@@@***************************************************************@@@@@@@@
    @@@@@@@@@@@**********************************************************,@@@@@@@@@@
    @@@@@@@@@@@@@@*****************************************************@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@***********************************************@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@***************************************@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@#***************************@@@@@@@@@@@@@@@@@@@@@@@@@@\033[0;37;40m
    """)

def logoB():
    print("""\n\n\033[1;33;40m
                                            /////
                                ////////////////////////////%
                          ///////////////////////////////////////
                     ///////////////////////////////////////////////
                  /////////////////////////////////////////////////////
               ///////////////////////////////////////////////////////////
             //////////////////////////////    /////////////////////////////
           ///////////////////////////////     ///     ///////////////////////
          //////////////////////    .////     ////    /////////////////////////
        ///////////////////////                */     //////////////////////////
       ////////////////////////////                    *//////////////////////////
      //////////////////////////////        /.              //////////////////////
      /////////////////////////////         ////////          /////////////////////
     //////////////////////////////        //////////*        //////////////////////
     /////////////////////////////        ///////////         //////////////////////
     /////////////////////////////                           ///////////////////////
    /////////////////////////////                         */////////////////////////
     ///////////////////////////        ////////           /////////////////////////
     ///////////////////////////        ///////////,         ///////////////////////
     /////////////////////  ///        /////////////         ///////////////////////
      ///////////////////              ////////////          //////////////////////
      ////////////////////                                  //////////////////////
       //////////////////////////                         *///////////////////////
        %///////////////////////     ///     /.       //////////////////////////
          /////////////////////     ////    ///////////////////////////////////
           ////////////////////////////     //////////////////////////////////
             ///////////////////////////////////////////////////////////////
                //////////////////////////////////////////////////////////*
                  /////////////////////////////////////////////////////
                     ///////////////////////////////////////////////
                         ///////////////////////////////////////
                             %///////////////////////////
                                        /////\033[0;37;40m
    """)

def logoC():
    print("""\n\n\033[1;33;40m
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@
    @@@@@@@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@
    @@@@@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&    &&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@
    @@@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&     &&&     &&&&&&&&&&&&&&&&&&&&&&&@@@@@@
    @@@@@@&&&&&&&&&&&&&&&&&&&&&&    *&&&&     &&&&    &&&&&&&&&&&&&&&&&&&&&&&&&@@@@@
    @@@@&&&&&&&&&&&&&&&&&&&&&&&                #&     &&&&&&&&&&&&&&&&&&&&&&&&&&@@@@
    @@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&.                   %&&&&&&&&&&&&&&&&&&&&&&&&&&@@
    @@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&        &,              &&&&&&&&&&&&&&&&&&&&&&@@
    @@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&.        &&&&&&&&          &&&&&&&&&&&&&&&&&&&&&@
    @&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&        &&&&&&&&&&%        &&&&&&&&&&&&&&&&&&&&&&
    @&&&&&&&&&&&&&&&&&&&&&&&&&&&&&        &&&&&&&&&&&         &&&&&&&&&&&&&&&&&&&&&&
    @&&&&&&&&&&&&&&&&&&&&&&&&&&&&&                           &&&&&&&&&&&&&&&&&&&&&&&
    &&&&&&&&&&&&&&&&&&&&&&&&&&&&&                         %&&&&&&&&&&&&&&&&&&&&&&&&&
    @&&&&&&&&&&&&&&&&&&&&&&&&&&&        &&&&&&&&           &&&&&&&&&&&&&&&&&&&&&&&&&
    @&&&&&&&&&&&&&&&&&&&&&&&&&&&        &&&&&&&&&&&/         &&&&&&&&&&&&&&&&&&&&&&&
    @&&&&&&&&&&&&&&&&&&&&&  &&&        &&&&&&&&&&&&&         &&&&&&&&&&&&&&&&&&&&&&&
    @@&&&&&&&&&&&&&&&&&&&              &&&&&&&&&&&&          &&&&&&&&&&&&&&&&&&&&&&@
    @@&&&&&&&&&&&&&&&&&&&&                                  &&&&&&&&&&&&&&&&&&&&&&@@
    @@@&&&&&&&&&&&&&&&&&&&&&&&&&&                         %&&&&&&&&&&&&&&&&&&&&&&&@@
    @@@@@&&&&&&&&&&&&&&&&&&&&&&&     &&&     &,       &&&&&&&&&&&&&&&&&&&&&&&&&&@@@@
    @@@@@@&&&&&&&&&&&&&&&&&&&&&     &&&&    &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@
    @@@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&     &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@
    @@@@@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@
    @@@@@@@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@
    @@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@\033[0;37;40m
    """)

def gitclone():
    url = "https://github.com/curly60e/satellite"
    os.system(f"git clone {url}")
    os.system("mkdir satellite/api/examples/.gnupg")
    os.system("gpg --full-generate-key --homedir satellite/api/examples/.gnupg")

def satnode():
    try:
        os.system("python3 satellite/api/examples/demo-rx.py &")
        t.sleep(5)
        os.system("python3 satellite/api/examples/api_data_reader.py --demo  --plaintext ")
    except:
        os.system("ps -ef | grep api_data_reader.py | grep -v grep | awk '{print $2}' | xargs kill -9")
        os.system("ps -ef | grep demo-rx.py | grep -v grep | awk '{print $2}' | xargs kill -9")

def matrixsc():
    if os.path.isdir('$HOME/pyblock/terminal_matrix'):
        print("OK Pass")
    else:
        url = "https://github.com/curly60e/terminal_matrix.git"
        os.system(f"git clone {url}")

def main():
    scriptpath = os.path.join(os.path.dirname(__file__), 'PyBlock.py')
    os.system(f"python3 {scriptpath}")


if __name__ == "__main__":
    typer.run(main)


def opreturnOnchainONLY():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    try:
        clear()
        blogo()
        output = render(
            "OP_RETURN Message", colors=['yellow'], align='left', font='tiny'
        )

        print(output)
        message = input("Message: ")
        curl = (
            "curl --header "
            + """"Content-Type: application/json" """
            + "--request POST  --data "
            + """'{"message":"""
            + f'"{message}...PyBLOCK"'
            + "}'"
            + " https://opreturnbot.com/api/create"
        )

        while len(message) > 70:
            clear()
            blogo()
            print("Error! Only 80 characters allowed!")
            message = input("\nMessage: ")
        a = os.popen(curl).read()
        b = str(a)
        clear()
        blogo()
        print("\033[1;30;47m")
        qr.add_data(b)
        qr.print_ascii()
        print("\033[0;37;40m")
        print(f'LND Invoice: {b}')
        qr.clear()
        input("\nContinue...")
        if lndconnectload['ln']:
            invoiceN = b
            invoice = invoiceN.lower()
            lncli = " payinvoice "
            lsd = os.popen(f'{lndconnectload["ln"]} decodepayreq {invoice}').read()
            lsd0 = str(lsd)
            d = json.loads(lsd0)
            url = f"http://opreturnbot.com/api/status/{d['payment_hash']}"
        else:
            cert_path = lndconnectload["tls"]
            macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
            headers = {'Grpc-Metadata-macaroon': macaroon}
            url = f'https://{lndconnectload["ip_port"]}/v1/payreq/{b}'
            r = requests.get(url, headers=headers, verify=cert_path)
            s = r.json()
            url = f"http://opreturnbot.com/api/status/{s['payment_hash']}"
        response = requests.get(url)
        responseB = str(response.text)
        responseC = responseB
        clear()
        blogo()
        print("\nTransaction ID: " + responseC)
        input("\nContinue...")
    except:
        pass

def opreturn():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    try:
        clear()
        blogo()
        output = render(
            "OP_RETURN Message", colors=['yellow'], align='left', font='tiny'
        )

        print(output)
        message = input("Message: ")
        curl = (
            "curl --header "
            + """"Content-Type: application/json" """
            + "--request POST  --data "
            + """'{"message":"""
            + f'"{message}...PyBLOCK"'
            + "}'"
            + " https://opreturnbot.com/api/create"
        )

        while len(message) > 70:
            clear()
            blogo()
            print("Error! Only 80 characters allowed!")
            message = input("\nMessage: ")
        a = os.popen(curl).read()
        b = str(a)
        clear()
        blogo()
        print("\033[1;30;47m")
        qr.add_data(b)
        qr.print_ascii()
        print("\033[0;37;40m")
        print(f'LND Invoice: {b}')
        qr.clear()
        input("\nContinue...")
        if lndconnectload['ln']:
            invoiceN = b
            invoice = invoiceN.lower()
            lncli = " payinvoice "
            lsd = os.popen(f'{lndconnectload["ln"]} decodepayreq {invoice}').read()
            lsd0 = str(lsd)
            d = json.loads(lsd0)
            url = f"http://opreturnbot.com/api/status/{d['payment_hash']}"
        else:
            cert_path = lndconnectload["tls"]
            macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
            headers = {'Grpc-Metadata-macaroon': macaroon}
            url = f'https://{lndconnectload["ip_port"]}/v1/payreq/{b}'
            r = requests.get(url, headers=headers, verify=cert_path)
            s = r.json()
            url = f"http://opreturnbot.com/api/status/{s['payment_hash']}"
        response = requests.get(url)
        responseB = str(response.text)
        responseC = responseB
        clear()
        blogo()
        print("\nTransaction ID: " + responseC)
        input("\nContinue...")
    except:
        pass

def opreturn_view():
    try:
        clear()
        blogo()
        output = render(
            "OP_RETURN Message", colors=['yellow'], align='left', font='tiny'
        )

        print(output)
        responseC = input("TX ID: ")
        url2 = f'http://opreturnbot.com/api/view/{responseC}'
        r = requests.get(url2)
        r2 = str(r.text)
        r3 = r2
        clear()
        blogo()
        print("\nTransaction ID: " + responseC)
        print(f'OP_RETURN Message: {r3}')
        input("\nContinue...")
    except:
        pass

def opretminer():
    try:
        conn = """curl -s 'https://bitcointicker.co/latestblocks/' | xargs --null | html2text | grep "Coinbase" -A 70 | tr -d '|' | grep -v "Coinbase" | grep '6.25'"""
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render(
            "decoded coinbase", colors=['yellow'], align='left', font='tiny'
        )

        print(output)
        print(a)
        input("")
    except:
        pass

#-----------------------------GAMES--------------------------------
#------------------------------------------------------------------

def gameroom():
    try:
        clear()
        blogo()
        print("""
        --------------------------------------

                  INITIATE ARCADE?

        --------------------------------------
        """.format(closed()))
        input("\a\nContinue...")
        conn = "ssh gameroom@bitreich.org"
        os.system(conn).read()
    except:
        pass
#----------------------------------------------------------------------

#-----------------------------Stats--------------------------------

def statsConn():
    try:
        conn = """curl -s https://www.bitcoinblockhalf.com/ | html2text | grep -E "Total" -A 10  | grep -v -E "\--" | tr -d '*' | tr -d '"' """
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render("stats", colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\nContinue...")
    except:
        pass

#-----------------------------END Stats--------------------------------

#-----------------------------Block Templates--------------------------------

def blockTmpConn():
    try:
        conn = """curl -s https://miningpool.observer/template-and-block | html2text | grep "Template and Block for" -A 13 """
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render("Templates and Blocks", colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\nContinue...")
    except:
        pass

#-----------------------------END Block Templates--------------------------------

#-----------------------------Unspendable--------------------------------

def unspendableConn():
    try:
        conn = """curl -s https://get.txoutset.info/unspendable.csv """
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render("Bitcoin Unspendable", colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\nContinue...")
    except:
        pass

#-----------------------------END Unspendable--------------------------------

#-----------------------------PGP--------------------------------

def pgpConn():
    try:
        conn = """curl -s https://web.archive.org/web/20110228054007/http://www.bitcoin.org/Satoshi_Nakamoto.asc"""
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render(
            "pgp", colors=['yellow'], align='left', font='tiny'
        )

        print(output)
        print(a)
        input("\a\nContinue...")
    except:
        pass

#-----------------------------END PGP--------------------------------

#-----------------------------MT--------------------------------
def mtConn(): # here we convert the result of the command 'getblockcount' on a random art design
    while True:
        try:
            clear()
            close()
            mtclock()
        except:
            break

def mtclock():
    if os.path.isfile('config/pyblocksettingsClock.conf') or os.path.isfile('config/pyblocksettingsClock.conf'): # Check if the file 'bclock.conf' is in the same folder
        settingsv = pickle.load(open("config/pyblocksettingsClock.conf", "rb")) # Load the file 'bclock.conf'
        settingsClock = settingsv # Copy the variable pathv to 'path'
    else:
        settingsClock = {"gradient":"", "design":"block", "colorA":"green", "colorB":"yellow"}
        pickle.dump(settingsClock, open("config/pyblocksettingsClock.conf", "wb"))
    clear()
    r = requests.get('https://bitcoinexplorer.org/api/price/usd/sats')
    r.headers['Content-Type']
    n = r.text
    di = json.loads(n)
    a = di
    b = str(a)
    clear()
    close()
    output = render(str(a), colors=[settingsClock['colorA'], settingsClock['colorB']], align='center')
    print("\033[0;37;40m\x1b[?25l" + output)
    while True:
        x = b
        r = requests.get('https://bitcoinexplorer.org/api/price/usd/sats')
        r.headers['Content-Type']
        n = r.text
        di = json.loads(n)
        a = di
        if x < str(a):
            clear()
            close()
            output5 = subprocess.check_output(['sudo', 'iwgetid'])
            z = str(output5)
            pp = random.choice(list(faceshappy.values())).encode('utf-8').decode('latin-1')
            output = render(str(a), colors=[settingsClock['colorA'], settingsClock['colorB']], align='center')
            print("\033[0;37;40m\x1b[?25l" + output)
            b = str(a)    #try:

#-----------------------------END MT--------------------------------

#-----------------------------Satoshi--------------------------------

def satoshiConn():
    try:
        conn = """curl -s https://www.metzdowd.com/pipermail/cryptography/2009-January/014994.html | html2text | tail -n 82 | grep -v "Unsubscribe" | grep -v "Next message" | grep -v "Previous message"| grep -v "Messages sorted" | grep -v "More information" | grep -v "list]" """
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render(
            "𝐒𝐚𝐭𝐨𝐬𝐡𝐢 𝐍𝐚𝐤𝐚𝐦𝐨𝐭𝐨. 𝟎𝐱𝟏𝟖𝐂𝟎𝟗𝐄𝟖𝟔𝟓𝐄𝐂𝟗𝟒𝟖𝐀𝟏. 𝐃𝐄𝟒𝐄 𝐅𝐂𝐀𝟑 𝐄𝟏𝐀𝐁 𝟗𝐄𝟒𝟏 𝐂𝐄𝟗𝟔 𝐂𝐄𝐂𝐁 𝟏𝟖𝐂𝟎 𝟗𝐄𝟖𝟔 𝟓𝐄𝐂𝟗 𝟒𝟖𝐀𝟏.", colors=['green'], align='left', font='console'
        )

        print(output)
        print(a)
        input("\a\nContinue...")
    except:
        pass

#-----------------------------END Satoshi--------------------------------

#-----------------------------Whale Alert--------------------------------

def whalalConn():
    try:
        conn = """curl -s 'https://api.whale-alert.io/v1/transactions?api_key=3LYGErNwoCSj6QUsWOWdpEuGTuYxakMZ&limit=7&min_value=5000000&currency=btc' | jq  -C '.transactions[]' | tr -d '{|}|,|"|:|' | grep -E "blockchain|amount" -A 8 | grep -v -E "\--|from|symbol|to|id" | xargs -L 1 | sed 's/blockchain/PyBLØCK/g' | sed 's/amount/₿/g' | sed 's/_usd/=$/g' | sed 's/bitcoin/WHALE ALERT/g' | grep -E ' '"""
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render("whale alert", colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\nContinue...")
    except:
        pass

#-----------------------------END Whale Alert--------------------------------
#-----------------------------bwt.dev--------------------------------

def bwtConn():
    try:
        conn = "curl -s https://bwt.dev/banner.txt"
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        print(a)
        input("\a\nContinue...")
    except:
        pass

#-----------------------------END bwt.dev--------------------------------
#-----------------------------Dates--------------------------------

def datesConn():
    try:
        conn = """curl -s "https://bitcoinexplorer.org/fun" | html2text | grep "20" | grep -v -E "https" | grep -E " " | head -n 46 | tr -d '[' | tr -d ','"""
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render("dates", colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\nContinue...")
    except:
        pass

#-----------------------------END Dates--------------------------------
#-----------------------------Missing--------------------------------

def missingConn():
    try:
        conn = """curl -s https://miningpool.observer/missing/feed.xml | html2text | grep -v "link" | grep -v "https" | grep -v "Missing Transaction" """
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render("missing transactions", colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\nContinue...")
    except:
        pass

#-----------------------------END Missing--------------------------------
#-----------------------------Quotes--------------------------------

def quotesConn():
    try:
        conn = """curl -s "https://bitcoinexplorer.org/api/quotes/all" | jq -C '.[]' | tr -d '{|}|]|,' | sed 's/text/Quote/g' | sed 's/speaker/By/g' | sed 's/url/Link/g' | sed 's/date/Date/g' | grep -v -E 'conQuote'"""
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render("quotes", colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\nContinue...")
    except:
        pass

#-----------------------------END Quotes--------------------------------
#-----------------------------Hashrate--------------------------------

def miningConn():
    try:
        conn = """curl -s "https://bitcoinexplorer.org/api/mining/hashrate" | jq -C '.[]' | tr -d '{|}|]|,' | tr -d '"'"""
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render("hashrate", colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\nContinue...")
    except:
        pass

#-----------------------------END Hashrate--------------------------------

#-----------------------------Strings Dat--------------------------------

def decodeStrDat(): # show srings
    try:
        clear()
        blogo()
        output = render(
            "strings", colors=['yellow'], align='left', font='tiny'
        )

        print(output)
        responseC = input("Blk Dat: ")
        list = f"""curl -s 'https://bitcoinstrings.com/blk'{responseC}.txt | html2text | grep -v "blk" | grep -v "files" | grep -v "Advertisement" | grep -v "BitcoinStrings" """
        a = os.popen(list).read()
        clear()
        blogo()
        print("\nBLK: " + responseC)
        print("\nString: " + a)
        input("\a\nContinue...")
    except:
        pass

#-----------------------------End Strings Dat--------------------------------

#-----------------------------StatsLN--------------------------------

def stalnConn():
    try:
        conn = """curl -s 'https://1ml.com' | html2text | xargs -L 1 | grep -E "Number" -A 8"""
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render(
            "lightning stats", colors=['yellow'], align='left', font='tiny'
        )

        print(output)
        print(a)
        input("\a\nContinue...")
    except:
        pass

#-----------------------------END StatsLN--------------------------------
#-----------------------------StatRanking--------------------------------
def ranConn():
    try:
        conn = """curl -s 'https://1ml.com/node?order=capacity&json=true' | jq -C '.[]' | xargs -L 1  | tr -d '{|}|]|,' | grep -v -E "last_update|color|noderank" | sed 's/alias/Node/g' | grep -v -E "addresses" | grep -E " " | sed 's/capacity/RANK/g'
"""
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render("ranking", colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\nContinue...")
    except:
        pass
#-----------------------------END Ranking--------------------------------

def trustednode():
    try:
        clear()
        blogo()
        closed()
        addv = """
        ---------------------------------------------------------------

                    REMEMBER TO INITIALIZE \033[1;35;40mTOR\033[0;37;40m ON THE SHELL

                            $ source torsocks on

        ---------------------------------------------------------------

        """
        print(addv)
        input("\a\nContinue...")
        conn = "telnet cut45oarvxfvfydrjery6slyeca4zpal7tljygdt5bji7l3jsrrgwkad.onion 6023"
        os.system(conn)
    except:
        pass
#-----------------------------END GAMES--------------------------------

#-----------------------------wttr.in--------------------------------
def wttrDataV1():
    try:
        clear()
        blogo()
        weatherList = """
        ------------------------------------------------------------------------------------



            \033[1;31;40m*\033[0;37;40m uruguay                # city name
            \033[1;31;40m*\033[0;37;40m ~Giza+pyramid          # any location (+ for spaces)
            \033[1;31;40m*\033[0;37;40m Москва                 # Unicode name of any location in any language
            \033[1;31;40m*\033[0;37;40m muc                    # airport code (3 letters)
            \033[1;31;40m*\033[0;37;40m @lightninghood.com     # domain name
            \033[1;31;40m*\033[0;37;40m 94107                  # area codes
            \033[1;31;40m*\033[0;37;40m -78.46,106.79          # GPS coordinates
            \033[1;31;40m*\033[0;37;40m moon                   # Moon phase (add ,+US or ,+France for these cities)
            \033[1;31;40m*\033[0;37;40m moon@2009-01-03        # Moon phase for the date (@2016-10-25)

            PRESS \033[1;32;40mM\033[0;37;40m TO INSERT MORE DATA

        ------------------------------------------------------------------------------------

        """
        print(weatherList)
        selectData = input("Insert your data \033[1;31;40m*\033[0;37;40m : ")
        if selectData in ['M', 'm']:
            moreData = """

        ------------------------------------------------------------------------------------
                                        Supported languages

                        ar af be ca da de el es et fr fa hi hu ia id it nb nl
                        oc pl pt-br ro ru tr th uk vi zh-cn zh-tw (supported)

        ------------------------------------------------------------------------------------
        ------------------------------------------------------------------------------------
                                             Units

                    m        # metric (SI) (used by default everywhere except US)
                    u        # USCS (used by default in US)
                    M        # show wind speed in m/s

        ------------------------------------------------------------------------------------
            """
            print(moreData)
            selectData2 = input("Insert your data \033[1;31;40m*\033[0;37;40m : ")
            lang = input("Insert your language: ")
            unit = input("Insert your metric units: ")
            list = f"curl '{lang}.wttr.in/{selectData2}?F&{unit}'"
        else:
            list = f'curl wttr.in/{selectData}?F'
        a = os.popen(list).read()
        clear()
        blogo()
        print(a)
        input("Continue...")
    except:
        pass

def wttrDataV2():
    try:
        clear()
        blogo()
        weatherList = """
        ------------------------------------------------------------------------------------



            \033[1;31;40m*\033[0;37;40m uruguay                # city name
            \033[1;31;40m*\033[0;37;40m ~Giza+pyramid          # any location (+ for spaces)
            \033[1;31;40m*\033[0;37;40m Москва                 # Unicode name of any location in any language
            \033[1;31;40m*\033[0;37;40m muc                    # airport code (3 letters)
            \033[1;31;40m*\033[0;37;40m @lightninghood.com     # domain name
            \033[1;31;40m*\033[0;37;40m 94107                  # area codes
            \033[1;31;40m*\033[0;37;40m -78.46,106.79          # GPS coordinates

            PRESS \033[1;32;40mM\033[0;37;40m TO INSERT MORE DATA

        ------------------------------------------------------------------------------------

        """
        print(weatherList)
        selectData = input("Insert your data \033[1;31;40m*\033[0;37;40m : ")
        if selectData in ['M', 'm']:
            moreData = """

        ------------------------------------------------------------------------------------
                                        Supported languages

                        ar af be ca da de el es et fr fa hi hu ia id it nb nl
                        oc pl pt-br ro ru tr th uk vi zh-cn zh-tw (supported)

        ------------------------------------------------------------------------------------
        ------------------------------------------------------------------------------------
                                             Units

                    m        # metric (SI) (used by default everywhere except US)
                    u        # USCS (used by default in US)
                    M        # show wind speed in m/s

        ------------------------------------------------------------------------------------
            """
            print(moreData)
            selectData2 = input("Insert your data \033[1;31;40m*\033[0;37;40m : ")
            lang = input("Insert your language: ")
            unit = input("Insert your metric units: ")
            list = f"curl 'v2.wttr.in/{selectData2}?{unit}&F&lang={lang}'"

        else:
            list = f'curl v2.wttr.in/{selectData}?F'
        a = os.popen(list).read()
        clear()
        blogo()
        print(a)
        input("Continue...")
    except:
        pass


#-----------------------------END wttr.in--------------------------------

#-----------------------------RATE.SX--------------------------------

def rateSXList():
    try:
        clear()
        blogo()
        fiat = """
                -------------------------------------------
                        AUD    Australian dollar
                        BRL    Brazilian real
                        CAD    Canadian dollar
                        CHF    Swiss franc
                        CLP    Chilean peso
                        CNY    Chinese yuan
                        CZK    Czech koruna
                        DKK    Danish krone
                        EUR    Euro
                        GBP    Pound sterling
                        HKD    Hong Kong dollar
                        HUF    Hungarian forint
                        IDR    Indonesian rupiah
                        ILS    Israeli shekel
                        INR    Indian rupee
                        JPY    Japanese yen
                        KRW    South Korean won
                        MXN    Mexican peso
                        MYR    Malaysian ringgit
                        NOK    Norwegian krone
                        NZD    New Zealand dollar
                        PHP    Philippine peso
                        PKR    Pakistani rupee
                        PLN    Polish zloty
                        RUB    Russian ruble
                        SEK    Swedish krona
                        SGD    Singapore dollar
                        THB    Thai baht
                        TRY    Turkish lira
                        TWD    New Taiwan dollar
                        USD    Dollars
                -------------------------------------------
        """
        print(fiat)
        selectFiat = input("Insert a Fiat currency: ")
    except:
        pass
    while True:
        try:
            list = f"curl -s '{selectFiat}.rate.sx/?F&n=1'"
            a = os.popen(list).read()
            clear()
            blogo()
            closed()
            print(a)
            t.sleep(20)
        except:
            break

def rateSXGraph():
    try:
        clear()
        blogo()
        fiat = """
                -------------------------------------------
                        AUD    Australian dollar
                        BRL    Brazilian real
                        CAD    Canadian dollar
                        CHF    Swiss franc
                        CLP    Chilean peso
                        CNY    Chinese yuan
                        CZK    Czech koruna
                        DKK    Danish krone
                        EUR    Euro
                        GBP    Pound sterling
                        HKD    Hong Kong dollar
                        HUF    Hungarian forint
                        IDR    Indonesian rupiah
                        ILS    Israeli shekel
                        INR    Indian rupee
                        JPY    Japanese yen
                        KRW    South Korean won
                        MXN    Mexican peso
                        MYR    Malaysian ringgit
                        NOK    Norwegian krone
                        NZD    New Zealand dollar
                        PHP    Philippine peso
                        PKR    Pakistani rupee
                        PLN    Polish zloty
                        RUB    Russian ruble
                        SEK    Swedish krona
                        SGD    Singapore dollar
                        THB    Thai baht
                        TRY    Turkish lira
                        TWD    New Taiwan dollar
                        USD    Dollars
                -------------------------------------------
        """
        print(fiat)
        selectFiat = input("Insert a Fiat currency: ")
    except:
        pass
    while True:
        try:
            list = f"curl -s '{selectFiat}.rate.sx/btc' | grep -v -E 'Use'"
            a = os.popen(list).read()
            clear()
            blogo()
            closed()
            print(a)
            t.sleep(20)
        except:
            break

#-----------------------------END RATE.SX--------------------------------



#-----------------------------COINGECKO--------------------------------

def CoingeckoPP():
    try:
        btcInfo = CoinGeckoAPI()
        n = btcInfo.get_price(ids='bitcoin', vs_currencies='usd,eur,gbp,jpy,aud')
        q = n['bitcoin']
        usd = q['usd']
        eur = q['eur']
        gbp = q['gbp']
        jpy = q['jpy']
        aud = q['aud']


        print("""
        --------------------COINGECKO BITCOIN PRICE-----------------------

                              1 BTC = {} USD
                              1 BTC = {} EUR
                              1 BTC = {} GBP
                              1 BTC = {} JPY
                              1 BTC = {} AUD

        ------------------------------------------------------------------

                                  ...BUT...

                                1 BTC = 1 BTC

        ------------------------------------------------------------------
        """.format(usd,eur,gbp,jpy,aud))
        input("Continue...")
    except:
        pass

#-----------------------------END COINGECKO--------------------------------


#-----------------------------LNBITS--------------------------------

def loadFileConnLNBits(lnbitLoad):
    lnbitLoad = {"wallet_name":"", "wallet_id":"", "admin_key":"", "invoice_read_key":""}

    if os.path.isfile('lnbit.conf'): # Check if the file 'bclock.conf' is in the same folder
        lnbitData= pickle.load(open("lnbit.conf", "rb")) # Load the file 'bclock.conf'
        lnbitLoad = lnbitData # Copy the variable pathv to 'path'
    else:
        clear()
        blogo()
        print("""\n\t   \033[1;33;40mATENTION\033[0;37;40m: YOU ARE GOING TO CREATE A FILE WITH YOUR INFORMATION OF CONNECTION TO LNBITS.COM.
                   WE WILL NEED SOME INFORMATION FROM YOUR ACCOUNT THAT THE ONLY ONE THAT WILL HAVE ACCESS IS YOU.
                          IF YOU DELETE THIS FILE YOU WILL NEED TO PAY AGAIN TO GET ACCESS FROM PyBLOCK.
                                           SAVE THE FILE '\033[1;33;40mlnbitSN.conf\033[0;37;40m' IN A SAFE PLACE.\n
        """)
        lnbitLoad["wallet_name"] = input("Wallet name: ") # path to the bitcoin-cli
        lnbitLoad["wallet_id"] = input("Wallet ID: ")
        lnbitLoad["admin_key"] = input("Admin key: ")
        lnbitLoad["invoice_read_key"] = input("Invoice/read key: ")
        pickle.dump(lnbitLoad, open("lnbit.conf", "wb"))
    return lnbitLoad

def createFileConnLNBits():
    clear()
    blogo()
    print("""\n\t   \033[1;33;40mATENTION\033[0;37;40m: YOU ARE GOING TO CREATE A FILE WITH YOUR INFORMATION OF CONNECTION TO LNBITS.COM.
               WE WILL NEED SOME INFORMATION FROM YOUR ACCOUNT THAT THE ONLY ONE THAT WILL HAVE ACCESS IS YOU.
                      IF YOU DELETE THIS FILE YOU WILL NEED TO PAY AGAIN TO GET ACCESS FROM PyBLOCK.
                                       SAVE THE FILE '\033[1;33;40mlnbitSN.conf\033[0;37;40m' IN A SAFE PLACE.\n
    """)
    lnbitLoad = {
        'wallet_id': '',
        'admin_key': '',
        'invoice_read_key': '',
        'wallet_name': input("Wallet name: "),
    }

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
    try:
        print("\n\tLNBITS CREATE INVOICE\n")
        amt = input("Amount: ")
        memo = input("Memo: ")
        a = loadFileConnLNBits(['invoice_read_key'])
        b = str(a['invoice_read_key'])
        curl = (
            'curl -X POST https://lnbits.com/api/v1/payments -d '
            + "'{"
            + f""""out": false, "amount": {amt}, "memo": "{memo} -PyBLOCK" """
            + "}'"
            + f""" -H "X-Api-Key: {b} " -H "Content-type: application/json" """
        )

        sh = os.popen(curl).read()
        clear()
        blogo()
        n = str(sh)
        d = json.loads(n)
        q = d['payment_request']
        c = q.lower()
        node_not = input("Do you want to pay this invoice with your node? Y/n: ")

        while True:
            if node_not in ["Y", "y"]:
                lndconnectload = {"ip_port":"", "tls":"", "macaroon":"", "ln":""}
                lndconnectData = pickle.load(open("blndconnect.conf", "rb")) # Load the file 'bclock.conf'
                lndconnectload = lndconnectData # Copy the variable pathv to 'path'
                if lndconnectload['ip_port']:
                    print("\nInvoice: " + c + "\n")
                    payinvoice()
                elif lndconnectload['ln']:
                    print("\nInvoice: " + c + "\n")
                    localpayinvoice()
            elif node_not in ["N", "n"]:
                print("\033[1;30;47m")
                qr.add_data(c)
                qr.print_ascii()
                print("\033[0;37;40m")
                qr.clear()
                print(f'Lightning Invoice: {c}')
                t.sleep(10)
                dn = str(d['checking_id'])
                checkcurl = (
                    f'curl -X GET https://lnbits.com/api/v1/payments/{dn}'
                    + f""" -H "X-Api-Key: {b}" -H "Content-type: application/json" """
                )


                rsh = os.popen(checkcurl).read()
                clear()
                blogo()
                nn = str(rsh)
                dd = json.loads(nn)
                db = dd['paid']
                if db != True:
                    continue
                clear()
                blogo()
                tick()
                t.sleep(2)
                break
    except:
        pass

def lnbitPayInvoice():
    bolt = input("Invoice: ")
    a = loadFileConnLNBits(['admin_key'])
    b = str(a['admin_key'])
    curl = (
        'curl -X POST https://lnbits.com/api/v1/payments -d '
        + "'{"
        + f""""out": true, "bolt11": "{bolt}" """
        + "}'"
        + f""" -H "X-Api-Key: {b}" -H "Content-type: application/json" """
    )

    try:
        sh = os.popen(curl).read()
        n = str(sh)
        d = json.loads(n)
        dn = str(d['checking_id'])
        a = loadFileConnLNBits(['invoice_read_key'])
        b = str(a['invoice_read_key'])
        while True:
            checkcurl = (
                f'curl -X GET https://lnbits.com/api/v1/payments/{dn}'
                + f""" -H "X-Api-Key: {b}" -H "Content-type: application/json" """
            )


            rsh = os.popen(checkcurl).read()
            clear()
            blogo()
            nn = str(rsh)
            dd = json.loads(nn)
            db = dd['paid']
            if db != True:
                continue
            tick()
            t.sleep(2)
            break
    except:
        pass

def lnbitCreatePayWall():
    while True:
        try:
            url = input("Url: ")
            memo = input("Memo: ")
            desc = input("Description: ")
            amt = input("Amount in sats: ")
            remb = input("Remembers Y/n: ")
            a = loadFileConnLNBits(['admin_key'])
            if remb in ["Y", "y"]:
                remember = "true"
            elif remb in ["N", "n"]:
                remember = "false"
            b = str(a['admin_key'])
            curl = (
                'curl -X POST https://lnbits.com/paywall/api/v1/paywalls -d '
                + "'{"
                + f""""url": "{url}", "memo": "{memo}", "description": "{desc}", "amount": {amt}, "remembers": {remember} """
                + "}'"
                + f""" -H  "Content-type: application/json" -H "X-Api-Key: {b}" """
            )

            sh = os.popen(curl).read()
            clear()
            blogo()
            n = str(sh)
            d = json.loads(n)
            print("\n\tPAYWALL CREATED SUCCESSFULLY\n")
            t.sleep(2)
            clear()
            aa = loadFileConnLNBits(['invoice_read_key'])
            bb = str(a['invoice_read_key'])
            checkcurl = f"""curl -X GET https://lnbits.com/paywall/api/v1/paywalls -H "X-Api-Key: {bb}" """


            sh = os.popen(checkcurl).read()
            clear()
            blogo()
            n = str(sh)
            d = json.loads(n)
            while True:
                print("\n\tLNBITS PAYWALL LIST\n")
                for item_ in d:
                    s = item_
                    print(f'ID: {s["id"]}')
                nd = input("\nSelect ID: ")
                for item in d:
                    s = item
                    nn = s['id']
                    if nd == nn:
                        print("\n----------------------------------------------------------------------------------------------------------------")
                        print(
                            """
                        \tLNBITS PAYWALL DECODED

                        ID: {}
                        Amount: {} sats
                        Description: {}
                        Memo: {}
                        Extras: {}
                        Remembers: {}
                        URL: {}
                        Wallet: {}
                        """.format(
                                nn,
                                s['amount'],
                                s['description'],
                                s['memo'],
                                s['extras'],
                                s['remembers'],
                                s['url'],
                                s['wallet'],
                            )
                        )

                        print("----------------------------------------------------------------------------------------------------------------\n")
                input("Continue...")
            clear()
            blogo()
        except:
            break

def lnbitListPawWall():
    a = loadFileConnLNBits(['invoice_read_key'])
    b = str(a['invoice_read_key'])
    checkcurl = (
        'curl -X GET https://lnbits.com/paywall/api/v1/paywalls -H'
        + f""" "X-Api-Key: {b}" """
    )

    sh = os.popen(checkcurl).read()
    clear()
    blogo()
    n = str(sh)
    d = json.loads(n)
    while True:
        print("\n\tLNBITS PAYWALL LIST\n")
        try:
            for item_ in d:
                s = item_
                print(f'ID: {s["id"]}')
            nd = input("\nSelect ID: ")
            for item in d:
                s = item
                nn = s['id']
                if nd == nn:
                    print("\n----------------------------------------------------------------------------------------------------------------")
                    print("""
                    \tLNBITS PAYWALL DECODED

                    ID: {}
                    Amount: {} sats
                    Description: {}
                    Memo: {}
                    Extras: {}
                    Remembers: {}
                    URL: {}
                    Wallet: {}
                    """.format(s['id'], s['amount'], s['description'], s['memo'], s['extras'], s['remembers'], s['url'], s['wallet']))
                    print("----------------------------------------------------------------------------------------------------------------\n")
        except:
            break
        input("Continue...")
        clear()
        blogo()

def lnbitDeletePayWall():
    while True:
        try:
            a = loadFileConnLNBits(['invoice_read_key'])
            b = str(a['invoice_read_key'])
            checkcurl = (
                'curl -X GET https://lnbits.com/paywall/api/v1/paywalls -H'
                + f""" "X-Api-Key: {b}" """
            )

            sh = os.popen(checkcurl).read()
            clear()
            blogo()
            n = str(sh)
            d = json.loads(n)
            while True:
                print("\n\tLNBITS PAYWALL LIST\n")
                try:
                    for item_ in d:
                        s = item_
                        print(f'ID: {s["id"]}')
                    nd = input("\nSelect ID: ")
                    for item in d:
                        s = item
                        nn = s['id']
                        if nd == nn:
                            print("\n----------------------------------------------------------------------------------------------------------------")
                            print("""
                            \tLNBITS PAYWALL DECODED

                            ID: {}
                            Amount: {} sats
                            Description: {}
                            Memo: {}
                            Extras: {}
                            Remembers: {}
                            URL: {}
                            Wallet: {}
                            """.format(s['id'], s['amount'], s['description'], s['memo'], s['extras'], s['remembers'], s['url'], s['wallet']))
                            print("----------------------------------------------------------------------------------------------------------------\n")
                except:
                    break
                input("Continue...")
                break
            print("\n\tDELETE PAYWALL\n")
            a = loadFileConnLNBits(['admin_key'])
            b = str(a['admin_key'])
            id = input("Insert PayWall ID: ")
            curl = (
                f"curl -X DELETE https://lnbits.com/paywall/api/v1/paywalls/{id}"
                + f""" -H "X-Api-Key: {b}" """
            )

            sh = os.popen(curl).read()
            clear()
            blogo()
            print("\n\tPAYWALL DELETED SUCCESSFULLY\n")
            t.sleep(2)
            clear()
        except:
            break

def lnbitsLNURLw():
    while True:
        try:
            clear()
            blogo()
            print("""
            ----------------------
                 CREATE LNURL
            ----------------------\n""")
            title = input("Title: ")
            minwith = input("Minimum Withdraw: ")
            maxwith = input("Maximum Withdraw: ")
            usesw = input("Uses: ")
            waittime = input("Wait Time: ")
            isunique = input("Is unique? true/false: ")
            a = loadFileConnLNBits(['admin_key'])
            b = str(a['admin_key'])
            curl = (
                'curl -X POST https://lnbits.com/withdraw/api/v1/links -d '
                + """'{"title":"""
                + f'"{title}", "min_withdrawable": {minwith}, "max_withdrawable": {maxwith}, "uses": {usesw}, "wait_time": {waittime}, "is_unique": {isunique}'
                + "}'"
                + f' -H "Content-type: application/json" -H "X-Api-Key: {b}"'
            )

            sh = os.popen(curl).read()
            clear()
            blogo()
            n = str(sh)
            d = json.loads(n)
            print("\n\tLNURLW CREATED SUCCESSFULLY\n")
            t.sleep(2)
            clear()
            while True:
                checkcurl = f'curl -X GET https://lnbits.com/withdraw/api/v1/links -H "X-Api-Key: {b}"'

                sh = os.popen(checkcurl).read()
                clear()
                blogo()
                n = str(sh)
                d = json.loads(n)
                print("\n\tLNBITS LNURLW LIST\n")
                for item_ in d:
                    s = item_
                    print(f'ID: {s["id"]} Uses: ' + str(s['uses']) + " Used: " + str(s['used']))
                nd = input("\nSelect ID: ")
                for item in d:
                    s = item
                    nn = s['id']
                    if nd == nn:
                        print("\n----------------------------------------------------------------------------------------------------------------")
                        print("""
                        \tLNBITS LNURLW DECODED

                        ID: {}
                        LNURL: {}
                        Wait Time: {}
                        Uses: {}
                        Used: {}
                        Minimum Withdraw: {}
                        Maximum Withdraw: {}
                        """.format(s['id'], s['lnurl'], s['wait_time'], s['uses'], s['used'], s['min_withdrawable'], s['max_withdrawable']))
                        print("----------------------------------------------------------------------------------------------------------------\n")
                input("Continue...")
                clear()
                blogo()
        except:
            break

def lnbitsLNURLwList():
    try:
        while True:
            a = loadFileConnLNBits(['admin_key'])
            b = str(a['admin_key'])
            checkcurl = f'curl -X GET https://lnbits.com/withdraw/api/v1/links -H "X-Api-Key: {b}"'

            sh = os.popen(checkcurl).read()
            clear()
            blogo()
            n = str(sh)
            d = json.loads(n)
            print("\n\tLNBITS LNURLW LIST\n")
            for item_ in d:
                s = item_
                print(f'ID: {s["id"]} Uses: ' + str(s['uses']) + " Used: " + str(s['used']))
            nd = input("\nSelect ID: ")
            for item in d:
                s = item
                nn = s['id']
                if nd == nn:
                    print("\n----------------------------------------------------------------------------------------------------------------")
                    print("""
                    \tLNBITS LNURLW DECODED

                    ID: {}
                    LNURL: {}
                    Wait Time: {}
                    Uses: {}
                    Used: {}
                    Minimum Withdraw: {}
                    Maximum Withdraw: {}
                    """.format(s['id'], s['lnurl'], s['wait_time'], s['uses'], s['used'], s['min_withdrawable'], s['max_withdrawable']))
                    print("----------------------------------------------------------------------------------------------------------------\n")
            input("Continue...")
    except:
        print("\n")

#-------------------------1d646820055e4e2da218e801eaacfc94----END LNBITS--------------------------------
#-----------------------------LNPAY--------------------------------

def loadFileConnLNPay(lnpayLoad):
    lnpayLoad = {"key":""}

    if os.path.isfile('lnpay.conf'): # Check if the file 'bclock.conf' is in the same folder
        lnpayData= pickle.load(open("lnpay.conf", "rb")) # Load the file 'bclock.conf'
        lnpayLoad = lnpayData # Copy the variable pathv to 'path'
    else:
        clear()
        blogo()
        print("""\n\t   \033[1;33;40mATENTION\033[0;37;40m: YOU ARE GOING TO CREATE A FILE WITH YOUR INFORMATION OF CONNECTION TO LNPAY.CO.
                   WE WILL NEED SOME INFORMATION FROM YOUR ACCOUNT THAT THE ONLY ONE THAT WILL HAVE ACCESS IS YOU.
                          IF YOU DELETE THIS FILE YOU WILL NEED TO PAY AGAIN TO GET ACCESS FROM PyBLOCK.
                                           SAVE THE FILE '\033[1;33;40mlnpaySN.conf\033[0;37;40m' IN A SAFE PLACE.\n
        """)
        lnpayLoad["key"] = input("API Key: ")
        print("\n\tWALLET ACCESS KEYS\n")
        lnpayLoad["wallet_key_id"] = input("Wallet Admin: ")
        pickle.dump(lnpayLoad, open("lnpay.conf", "wb"))
    clear()
    blogo()
    return lnpayLoad

def createFileConnLNPay():
    clear()
    blogo()
    print("""\n\t   \033[1;33;40mATENTION\033[0;37;40m: YOU ARE GOING TO CREATE A FILE WITH YOUR INFORMATION OF CONNECTION TO LNPAY.CO.
               WE WILL NEED SOME INFORMATION FROM YOUR ACCOUNT THAT THE ONLY ONE THAT WILL HAVE ACCESS IS YOU.
                      IF YOU DELETE THIS FILE YOU WILL NEED TO PAY AGAIN TO GET ACCESS FROM PyBLOCK.
                                       SAVE THE FILE '\033[1;33;40mlnpaySN.conf\033[0;37;40m' IN A SAFE PLACE.\n
    """)
    lnpayLoad["key"] = input("API Key: ")
    print("\n\tWALLET ACCESS KEYS\n")
    lnpayLoad["wallet_key_id"] = input("Wallet Admin: ")
    pickle.dump(lnpayLoad, open("lnpay.conf", "wb"))

def lnpayGetBalance():
    a = loadFileConnLNPay(['key'])
    b = str(a['key'])
    n = loadFileConnLNPay(['wallet_key_id'])
    q = str(n['wallet_key_id'])
    lnpay_py.initialize(b)
    clear()
    blogo()
    my_wallet = LNPayWallet(q)
    info = my_wallet.get_info()
    print("\n---------------------------------------------------------------------------------------------------")
    print("""
    \tLNPAY WALLET BALANCE

    Wallet ID: {}
    Wallet Name: {}
    Balance: {} sats
    """.format(info['id'], info['user_label'], info['balance']))
    print("---------------------------------------------------------------------------------------------------\n")
    input("\nContinue... ")

def lnpayCreateInvoice():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    a = loadFileConnLNPay(['key'])
    b = str(a['key'])
    n = loadFileConnLNPay(['wallet_key_id'])
    q = str(n['wallet_key_id'])
    lnpay_py.initialize(b)
    clear()
    blogo()
    my_wallet = LNPayWallet(q)
    amt = input("\nAmount in Sats: ")
    memo = input("Memo: ")
    invoice_params = {'num_satoshis': amt, 'memo': f'{memo} -PyBLOCK'}
    try:
        invoice = my_wallet.create_invoice(invoice_params)
        clear()
        blogo()
        node_not = input("Do you want to pay this invoice with your node? Y/n: ")
        while True:
            if node_not in ["Y", "y"]:
                lndconnectload = {"ip_port":"", "tls":"", "macaroon":"", "ln":""}
                lndconnectData = pickle.load(open("blndconnect.conf", "rb")) # Load the file 'bclock.conf'
                lndconnectload = lndconnectData # Copy the variable pathv to 'path'
                if lndconnectload['ip_port']:
                    print("\nInvoice: " + invoice['payment_request'] + "\n")
                    payinvoice()
                elif lndconnectload['ln']:
                    print("\nInvoice: " + invoice['payment_request'] + "\n")
                    localpayinvoice()
            elif node_not in ["N", "n"]:
                print("\033[1;30;47m")
                qr.add_data(invoice['payment_request'])
                qr.print_ascii()
                print("\033[0;37;40m")
                qr.clear()
                print(f'Lightning Invoice: {invoice["payment_request"]}')
                t.sleep(10)
                curl = f'curl -u {b}: https://api.lnpay.co/v1/lntx/{invoice["id"]}?fields=settled,num_satoshis'

                rsh = os.popen(curl).read()
                clear()
                blogo()
                nn = str(rsh)
                dd = json.loads(nn)
                db = dd['settled']
                if db != 1:
                    continue
                clear()
                blogo()
                tick()
                t.sleep(2)
                break
    except:
        pass

def lnpayGetTransactions():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    a = loadFileConnLNPay(['key'])
    b = str(a['key'])
    n = loadFileConnLNPay(['wallet_key_id'])
    q = str(n['wallet_key_id'])
    lnpay_py.initialize(b)
    clear()
    blogo()
    my_wallet = LNPayWallet(q)

    transactions = my_wallet.get_transactions()
    while True:
        try:
            print("\n\tLNPAY LIST PAYMENTS\n")
            for transaction_ in transactions:
                s = transaction_
                q = s['lnTx']

                print(f'ID: {s["id"]}')
            nd = input("\nSelect ID: ")
            for transaction in transactions:
                s = transaction
                nn = s['id']
                if nd == nn:
                    print("\n----------------------------------------------------------------------------------------------------")
                    nnn = s['lnTx']
                    print("""
                    \tLNPAY LIST PAYMENT DECODED

                    ID: {}
                    Amount: {} sats
                    Memo: {}
                    Invoice: {}
                    RHash: {}
                    """.format(nnn['id'], nnn['num_satoshis'], nnn['memo'], nnn['payment_request'], nnn['r_hash_decoded']))
                    print("----------------------------------------------------------------------------------------------------\n")
                    print("\033[1;30;47m")
                    qr.add_data(nnn['payment_request'])
                    qr.print_ascii()
                    print("\033[0;37;40m")
                    qr.clear()
            input("Continue...")
            clear()
            blogo()
        except:
            break
    clear()
    blogo()

def lnpayPayInvoice():
    a = loadFileConnLNPay(['key'])
    b = str(a['key'])
    n = loadFileConnLNPay(['wallet_key_id'])
    q = str(n['wallet_key_id'])
    lnpay_py.initialize(b)
    clear()
    blogo()
    my_wallet = LNPayWallet(q)
    try:
        print("\n\tLNPAY PAY INVOICE\n")
        inv = input("\nInvoice: ")
        curl = f'curl -u{b}: https://api.lnpay.co/v1/node/default/payments/decodeinvoice?payment_request={inv}'

        clear()
        rsh = os.popen(curl).read()
        nn = str(rsh)
        dd = json.loads(nn)
        clear()
        blogo()
        print("\n----------------------------------------------------------------------------------------------------")
        print("""
        \tLNPAY INVOICE DECODED

        Destination: {}
        Amount: {} sats
        Memo: {}
        Invoice: {}
        """.format(dd['destination'], dd['num_satoshis'], dd['description'], inv))
        print("----------------------------------------------------------------------------------------------------\n")
        print("<<< Cancel Control + C")
        input("\nEnter to Continue... ")
        invoice_params = {
            'payment_request': inv
        }
        pay_result = my_wallet.pay_invoice(invoice_params)
    except:
        pass

def lnpayTransBWallets():
    a = loadFileConnLNPay(['key'])
    b = str(a['key'])
    n = loadFileConnLNPay(['wallet_key_id'])
    q = str(n['wallet_key_id'])
    lnpay_py.initialize(b)
    clear()
    blogo()
    print("""\n\tLNPAY TRANSFER BETWEEN WALLETS
    \nCaution: If you Transfer to another of your LNPay wallets
    you will only access to your funds via Web.\n""")
    try:
        wall = input("Wallet destination ID: ")
        amt = input("Amount in Sats: ")
        memo = input("Memo: ")
        my_wallet = LNPayWallet(q)
        transfer_params = {
            'dest_wallet_id': wall,
            'num_satoshis': amt,
            'memo': memo
        }
        transfer_result = my_wallet.internal_transfer(transfer_params)
        p = transfer_result['wtx_transfer_in']
        e = transfer_result['wtx_transfer_out']
        f = e['wal']
        v = p['wal']
        print("\n----------------------------------------------------------------------------------------------------")
        print("""
        \tLNPAY TRANSFER BETEWWN WALLETS INFORMATION

        ID: {}
        Amount: {} sats
        Memo: {}
        To Wallet: {}
        From Wallet: {}
        """.format(p['id'], p['num_satoshis'], p['user_label'], v['user_label'], f['user_label']))
        print("----------------------------------------------------------------------------------------------------\n")
        input("Continue...")
    except:
        pass

#-----------------------------END LNPAY--------------------------------
#-----------------------------OPENNODE--------------------------------

def loadFileConnOpenNode(opennodeLoad):
    opennodeLoad = {"key":"","wdr":"","inv":""}

    if os.path.isfile('opennode.conf'): # Check if the file 'bclock.conf' is in the same folder
        opennodeData= pickle.load(open("opennode.conf", "rb")) # Load the file 'bclock.conf'
        opennodeLoad = opennodeData # Copy the variable pathv to 'path'
    else:
        clear()
        blogo()
        print("""\n\t   \033[1;33;40mATENTION\033[0;37;40m: YOU ARE GOING TO CREATE A FILE WITH YOUR INFORMATION OF CONNECTION TO OPENNODE.COM.
                   WE WILL NEED SOME INFORMATION FROM YOUR ACCOUNT THAT THE ONLY ONE THAT WILL HAVE ACCESS IS YOU.
                          IF YOU DELETE THIS FILE YOU WILL NEED TO PAY AGAIN TO GET ACCESS FROM PyBLOCK.
                                           SAVE THE FILE '\033[1;33;40mopennodeSN.conf\033[0;37;40m' IN A SAFE PLACE.\n
        """)
        opennodeLoad["key"] = input("API Read Only Key: ")
        opennodeLoad["wdr"] = input("API Withdrawall Key: ")
        opennodeLoad["inv"] = input("API Invoices Key: ")
        pickle.dump(opennodeLoad, open("opennode.conf", "wb"))
    clear()
    blogo()
    return opennodeLoad

def createFileConnOpenNode():
    clear()
    blogo()
    print("""\n\t   \033[1;33;40mATENTION\033[0;37;40m: YOU ARE GOING TO CREATE A FILE WITH YOUR INFORMATION OF CONNECTION TO OPENNODE.COM.
               WE WILL NEED SOME INFORMATION FROM YOUR ACCOUNT THAT THE ONLY ONE THAT WILL HAVE ACCESS IS YOU.
                      IF YOU DELETE THIS FILE YOU WILL NEED TO PAY AGAIN TO GET ACCESS FROM PyBLOCK.
                                       SAVE THE FILE '\033[1;33;40mopennodeSN.conf\033[0;37;40m' IN A SAFE PLACE.\n
    """)
    opennodeLoad = {'wdr': '', 'inv': '', 'key': input("API Read Only Key: ")}
    opennodeLoad["wdr"] = input("API Withdrawall Key: ")
    opennodeLoad["inv"] = input("API Invoices Key: ")
    pickle.dump(opennodeLoad, open("opennode.conf", "wb"))

def OpenNodelistfunds():
    a = loadFileConnOpenNode(['wdr'])
    b = str(a['wdr'])
    curl = f'curl https://api.opennode.co/v1/account/balance -H "Content-Type: application/json" -H "Authorization: {b}"'


    sh = os.popen(curl).read()
    clear()
    blogo()
    n = str(sh)
    d = json.loads(n)
    r = d['data']
    print("\n----------------------------------------------------------------------------------------------------")
    p = r['balance']
    print("""
    OPENNODE BALANCE

    Amount: {} sats
    """.format(p['BTC']))
    print("----------------------------------------------------------------------------------------------------\n")
    input("Continue...")

def OpenNodeCheckStatus():
    curl = "curl -X GET https://status.opennode.com/history.rss"
    sh = os.popen(curl).read()
    clear()
    blogo()
    my_dict=xmltodict.parse(sh)
    n=json.dumps(my_dict)
    nn = str(n)
    qq = json.loads(n)
    a = qq['rss']
    b = a['channel']
    c = b['title']
    d = b['item']
    dd = d[0]
    e = dd['title']
    print("""
    \n----------------------------------------------------------------------------------------------------
    \n\t{}

    {}\n
    {}

    \n----------------------------------------------------------------------------------------------------
    """.format(c.upper(),e,b['pubDate']))
    input("Enter to Continue...")

def OpenNodecreatecharge():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    a = loadFileConnOpenNode(['key'])
    b = str(a['key'])
    fiat = input("Are you going to pay in FIAT? Y/n:")
    if fiat in ["Y", "y"]:
        print("\n----------------------------------------------------------------------------------------------------")
        print("""
        \tFIAT supported on OpenNode:

        AED,AFN,ALL,AMD,ANG,AOA,ARS,AUD,AWG,AZN,BAM,BBD,BDT,BGN,BHD,BIF,BMD,BND,BOB,BRL,BSD,BTN,BWP,
        BYN,BZD,CAD,CDF,CHF,CLF,CLP,CNH,CNY,COP,CRC,CUC,CUP,CVE,CZK,DJF,DKK,DOP,DZD,EGP,ERN,ETB,EUR,
        FJD,FKP,GBP,GEL,GGP,GHS,GIP,GMD,GNF,GTQ,GYD,HKD,HNL,HRK,HTG,HUF,IDR,ILS,IMP,INR,IQD,IRR,ISK,
        JEP,JMD,JOD,JPY,KES,KGS,KHR,KMF,KPW,KRW,KWD,KYD,KZT,LAK,LBP,LKR,LRD,LSL,LYD,MAD,MDL,MGA,MKD,
        MMK,MNT,MOP,MRO,MUR,MVR,MWK,MXN,MYR,MZN,NAD,NGN,NIO,NOK,NPR,NZD,OMR,PAB,PEN,PGK,PHP,PKR,PLN,
        PYG,QAR,RON,RSD,RUB,RWF,SAR,SBD,SCR,SDG,SEK,SGD,SHP,SLL,SOS,SRD,SSP,STD,SVC,SYP,SZL,THB,TJS,
        TMT,TND,TOP,TRY,TTD,TWD,TZS,UAH,UGX,USD,UYU,UZS,VES,VND,VUV,WST,XAF,XAG,XAU,XCD,XDR,XOF,XPD,
        XPF,XPT,YER,ZAR,ZMW,ZWL,USDC.
        """)
        print("\n----------------------------------------------------------------------------------------------------")
        selection = input("Select a FIAT currency: ")
        amt = input(f"Amount in {selection}: ")
        curl = (
            f'curl https://api.opennode.co/v1/charges -X POST -H "Authorization: {b}"'
            + ' -H "Content-Type: application/json" -d '
            + "'{"
            + f'"amount": "{amt}", "currency": "{selection.upper()}"'
            + "}'"
        )


        sh = os.popen(curl).read()
        clear()
        blogo()
        n = str(sh)
        d = json.loads(n)
        dd = d['data']
        qq = dd['lightning_invoice']
        nn = qq['payreq']
        mm = nn.lower()
        pp = dd['address']
        while True:
            try:
                print("\n----------------------------------------------------------------------------------------------------")
                print("""
                \tOPENNODE PAYMENT REQUEST

                Amount: {} {}
                ID: {}
                Status: {}
                Invoice: {}
                Onchain Address: {}
                Amount: {} sats
                """.format(amt, selection.upper(), dd['id'], dd['status'], mm, pp, dd['amount']))
                print("----------------------------------------------------------------------------------------------------\n")
                pay = input("Invoice or Onchain Address? I/O: ")
                if pay in ["I", "i"]:
                    node_not = input("Do you want to pay this invoice with your node? Y/n: ")
                    if node_not in ["Y", "y"]:
                        lndconnectData = pickle.load(open("blndconnect.conf", "rb")) # Load the file 'bclock.conf'
                        lndconnectload = {"ip_port":"", "tls":"", "macaroon":"", "ln":""}
                        lndconnectload = lndconnectData # Copy the variable pathv to 'path'
                        if lndconnectload['ip_port']:
                            print("\nInvoice: " + mm + "\n")
                            payinvoice()
                        elif lndconnectload['ln']:
                            print("\nInvoice: " + mm + "\n")
                            localpayinvoice()
                    elif node_not in ["N", "n"]:
                        print("\033[1;30;47m")
                        qr.add_data(mm)
                        qr.print_ascii()
                        print("\033[0;37;40m")
                        qr.clear()
                        print("\nLightning Invoice: " + mm)
                elif pay in ["O", "o"]:
                    print("\033[1;30;47m")
                    qr.add_data(pp)
                    qr.print_ascii()
                    print("\033[0;37;40m")
                    qr.clear()
                    print(f"\nAmount in sats: {dd['amount']} sats")
                    print("\nOnchain Address: " + pp)
                input("\nContinue...")
                clear()
                blogo()
            except:
                break
    elif fiat in ["N", "n"]:
        amt = input("Amount in sats: ")
        curl = (
            f'curl https://api.opennode.co/v1/charges -X POST -H"Authorization: {b}"'
            + ' -H "Content-Type: application/json" -d '
            + "'{"
            + f'"amount": "{amt}", "currency": "BTC"'
            + "}'"
        )


        sh = os.popen(curl).read()
        clear()
        blogo()
        n = str(sh)
        d = json.loads(n)
        dd = d['data']
        qq = dd['lightning_invoice']
        nn = qq['payreq']
        mm = nn.lower()
        pp = dd['address']
        while True:
            try:
                print("\n----------------------------------------------------------------------------------------------------")
                print("""
                \tOPENNODE PAYMENT REQUEST

                Amount: {} sats
                ID: {}
                Status: {}
                Invoice: {}
                Onchain Address: {}
                Amount: {} sats
                """.format(amt, dd['id'], dd['status'], mm, pp, dd['amount']))
                print("----------------------------------------------------------------------------------------------------\n")
                pay = input("Invoice or Onchain Address? I/O: ")
                if pay in ["I", "i"]:
                    node_not = input("Do you want to pay this invoice with your node? Y/n: ")
                    if node_not in ["Y", "y"]:
                        lndconnectData = pickle.load(open("blndconnect.conf", "rb")) # Load the file 'bclock.conf'
                        lndconnectload = {"ip_port":"", "tls":"", "macaroon":"", "ln":""}
                        lndconnectload = lndconnectData # Copy the variable pathv to 'path'
                        if lndconnectload['ip_port']:
                            print("\nInvoice: " + mm + "\n")
                            payinvoice()
                        elif lndconnectload['ln']:
                            print("\nInvoice: " + mm + "\n")
                            localpayinvoice()
                    elif node_not in ["N", "n"]:
                        print("\033[1;30;47m")
                        qr.add_data(mm)
                        qr.print_ascii()
                        print("\033[0;37;40m")
                        qr.clear()
                        print("\nLightning Invoice: " + mm)
                elif pay in ["O", "o"]:
                    print("\033[1;30;47m")
                    qr.add_data(pp)
                    qr.print_ascii()
                    print("\033[0;37;40m")
                    qr.clear()
                    print(f"\nAmount in sats: {dd['amount']} sats")
                    print("\nOnchain Address: " + pp)
                input("\nContinue...")
                clear()
                blogo()
            except:
                break

def OpenNodeiniciatewithdrawal():
    a = loadFileConnOpenNode(['wdr'])
    b = str(a['wdr'])
    c = loadFileConnOpenNode(['key'])
    d = str(a['key'])
    lnchain = input("Are you going to pay with Lightning or Onchain? L/O: ")
    clear()
    blogo()
    if lnchain in ["L", "l"]:
        try:
            while True:
                invoice = input("\nInvoice: ")
                checkcurl = (
                    f'curl https://api.opennode.co/v1/charge/decode -X POST -H "Authorization: {b}" -H "Content-Type: application/json" -d '
                    + "'{"
                    + f'"pay_req": "{invoice}"'
                    + "}'"
                )

                ssh = os.popen(checkcurl).read()
                nn = str(ssh)
                dd = json.loads(nn)
                print(dd)
                if invoice != "":
                    break
                print("\n----------------------------------------------------------------------------------------------------")
                print("""
                    \tOPENNODE TRANSFER REQUEST

                    Message: {}
                    """.format(dd['message']))
                print("----------------------------------------------------------------------------------------------------\n")
            rr = dd['data']
            ss = rr['pay_req']

            print("\n----------------------------------------------------------------------------------------------------")
            print("""
            \tOPENNODE TRANSFER REQUEST

            Network: {}
            Amount: {} sats
            Destination: {}
            Hash: {}
            """.format(ss['network'],ss['amount'],ss['pub_key'],ss['hash']))
            print("----------------------------------------------------------------------------------------------------\n")
            print("<<< Cancel Control + C")
            input("\nEnter to Continue... ")

            curl = (
                f'curl https://api.opennode.co/v2/withdrawals -X POST -H "Content-Type: application/json" -H "Authorization: {b}"'
                + " -d '{"
                + f'"type": "ln", "address": "{invoice}", "callback_url": ""'
                + "}'"
            )

            sh = os.popen(curl).read()
            n = str(sh)
            d = json.loads(n)
            clear()
            blogo()
            tick()
            t.sleep(2)
        except:
            pass

    elif lnchain in ["O", "o"]:
        try:
            while True:
                print("\n\tOPENNODE TRANSFER REQUEST\n")
                print("\n\tMinimum amount 200000 sats\n")
                address = input("\nBitcoin Address: ")
                amt = int(input("Amount in sats: "))
                curl = (
                    f'curl https://api.opennode.co/v2/withdrawals -X POST -H "Content-Type: application/json" -H "Authorization: {b}"'
                    + " -d '{"
                    + f'"type": "chain", "amount": {amt}, "address": "{address}", "callback_url": ""'
                    + "}'"
                )

                if amt < 199999:
                    sh = os.popen(curl).read()
                    n = str(sh)
                    d = json.loads(n)
                    print("\n----------------------------------------------------------------------------------------------------")
                    print("""
                    \tOPENNODE TRANSFER REQUEST

                    Message: {}
                    """.format(d['message']))
                    print("----------------------------------------------------------------------------------------------------\n")
                elif amt > 200000:
                    sh = os.popen(curl).read()
                    n = str(sh)
                    d = json.loads(n)
                    dd = d['data']
                    print("\n----------------------------------------------------------------------------------------------------")
                    print("""
                    \tOPENNODE TRANSFER REQUEST

                    Amount: {} sats
                    Address Destination: {}
                    Fee: {}
                    Status: {}
                    """.format(dd['amount'],dd['address'],dd['fee'], dd['status']))
                    print("----------------------------------------------------------------------------------------------------\n")
                    input("\nContinue... ")
                    clear()
                    blogo()
                    logoB()
                    t.sleep(2)
                    break
        except:
            pass

def OpenNodeListPayments():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    a = loadFileConnOpenNode(['wdr'])
    b = str(a['wdr'])
    curl = f'curl https://api.opennode.co/v1/withdrawals -H "Content-Type: application/json" -H "Authorization: {b}"'

    sh = os.popen(curl).read()
    clear()
    blogo()
    print("\n\tOPENNODE TRANSACTIONS LIST\n")
    n = str(sh)
    d = json.loads(n)
    da = d['data']
    while True:
        try:
            for item_ in da:
                s = item_
                n = s['status']
                q = str(n)
                print(f'ID: {s["id"]} {q}')
            nd = input("\nSelect ID: ")
            for item in da:
                s = item
                nn = s['id']
                if nd == nn:
                    print("\n----------------------------------------------------------------------------------------------------")
                    print("""
                    \tOPENNODE TRANSACTION DECODED
                    ID: {}
                    Amount: {} sats
                    Type: {}
                    Invoice or Tx ID: {}
                    Status: {}
                    """.format(s['id'], s['amount'], s['type'], s['reference'], s['status']))
                    print("----------------------------------------------------------------------------------------------------\n")
                    print("\033[1;30;47m")
                    qr.add_data(s['reference'])
                    qr.print_ascii()
                    print("\033[0;37;40m")
                    qr.clear()
            input("Continue...")
            clear()
            blogo()
            print("\n\tOPENNODE TRANSACTIONS LIST\n")
        except:
            break

#-----------------------------END OPENNODE--------------------------------
#-----------------------------TIPPINME--------------------------------

def loadFileTippinMe(tippinmeLoad):
    tippinmeLoad = {"key":""}

    if os.path.isfile('tippinme.conf'): # Check if the file 'bclock.conf' is in the same folder
        tippinmeData= pickle.load(open("tippinme.conf", "rb")) # Load the file 'bclock.conf'
        tippinmeLoad = tippinmeData # Copy the variable pathv to 'path'
    else:
        clear()
        blogo()
        print("""\n\t   \033[1;33;40mATENTION\033[0;37;40m: YOUR CONFIGURATION INFORMATION WILL BE SAVE IN '\033[1;33;40mtippinme.conf\033[0;37;40m'
                                                                IF YOU NEED TO START AGAIN, DELETE IT.\n
        """)
        tippinmeLoad["key"] = input("Twitter @user: ")
        pickle.dump(tippinmeLoad, open("tippinme.conf", "wb"))
    clear()
    blogo()
    return tippinmeLoad

def createFileTippinMe():
    clear()
    blogo()
    print("""\n\t   \033[1;33;40mATENTION\033[0;37;40m: YOUR CONFIGURATION INFORMATION WILL BE SAVE IN '\033[1;33;40mtippinme.conf\033[0;37;40m'
                                                                IF YOU NEED TO START AGAIN, DELETE IT.\n
    """)
    tippinmeLoad = {'key': input("Twitter @user: ")}
    pickle.dump(tippinmeLoad, open("tippinme.conf", "wb"))

def tippinmeGetInvoice():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    a = loadFileTippinMe(['key'])
    b = str(a['key'])
    try:
        print("\n\tTIPPINME GENERATE INVOICE\n")
        q = input("Amount in Sats: ")
        clear()
        blogo()
        url = f'https://api.tippin.me/v1/public/addinvoice/{b}/{q}'
        response = requests.get(url)
        responseB = str(response.text)
        responseC = responseB
        lnreq = responseC.split(',')
        lnurl = lnreq[1]
        lnurlS = str(lnurl)
        lnurlR = lnurlS.split(':')
        lnurlW = lnbc1R[1]
        ln = str(lnurlW)
        ln1 = ln.strip('"')
        node_not = input("Do you want to pay this invoice with your node? Y/n: ")
        if node_not in ["Y", "y"]:
            lndconnectload = {"ip_port":"", "tls":"", "macaroon":"", "ln":""}
            lndconnectData = pickle.load(open("blndconnect.conf", "rb")) # Load the file 'bclock.conf'
            lndconnectload = lndconnectData # Copy the variable pathv to 'path'
            if lndconnectload['ip_port']:
                print("\nInvoice: " + ln1 + "\n")
                payinvoice()
            elif lndconnectload['ln']:
                print("\nInvoice: " + ln1 + "\n")
                localpayinvoice()
        elif node_not in ["N", "n"]:
            print("\033[1;30;47m")
            qr.add_data(ln1)
            qr.print_ascii()
            print("\033[0;37;40m")
            print(f'LND Invoice: {ln1}')
            response.close()
            input("Continue...")
    except:
        pass

#-----------------------------END TIPPINME--------------------------------
#-----------------------------TALLYCOIN------------------------------
def loadFileConnTallyCo(tallycoLoad):
    tallycoLoad = {"tallyco.conf":"","id":""}

    if os.path.isfile('tallyco.conf'): # Check if the file 'bclock.conf' is in the same folder
        tallyData= pickle.load(open("tallyco.conf", "rb")) # Load the file 'bclock.conf'
        tallycoLoad = tallyData # Copy the variable pathv to 'path'
    else:
        clear()
        blogo()
        print("""\n\t   \033[1;33;40mATENTION\033[0;37;40m: YOU ARE GOING TO CREATE A FILE WITH YOUR INFORMATION OF CONNECTION TO TALLYCO.IN.
                   WE WILL NEED SOME INFORMATION FROM YOUR ACCOUNT THAT THE ONLY ONE THAT WILL HAVE ACCESS IS YOU.
                          IF YOU DELETE THIS FILE YOU WILL NEED TO PAY AGAIN TO GET ACCESS FROM PyBLOCK.
                                           SAVE THE FILE '\033[1;33;40mtallycoSN.conf\033[0;37;40m' IN A SAFE PLACE.\n
        """)
        print("\nEXAMPLE: https://tallyco.in/s/{fundraiser_id}/\n")
        tallycoLoad["id"] = input("User ID or Twitter @USER: ")
        pickle.dump(tallycoLoad, open("tallyco.conf", "wb"))
    clear()
    blogo()
    return tallycoLoad

def createFileConnTallyCo():
    clear()
    blogo()
    print("""\n\t   \033[1;33;40mATENTION\033[0;37;40m: YOU ARE GOING TO CREATE A FILE WITH YOUR INFORMATION OF CONNECTION TO TALLYCO.IN.
               WE WILL NEED SOME INFORMATION FROM YOUR ACCOUNT THAT THE ONLY ONE THAT WILL HAVE ACCESS IS YOU.
                      IF YOU DELETE THIS FILE YOU WILL NEED TO PAY AGAIN TO GET ACCESS FROM PyBLOCK.
                                       SAVE THE FILE '\033[1;33;40mtallycoSN.conf\033[0;37;40m' IN A SAFE PLACE.\n
    """)
    print("\nEXAMPLE: https://tallyco.in/s/{fundraiser_id}/\n")
    tallycoLoad = {'fundraiser_id': '', 'id': input("User ID or Twitter @USER: ")}
    pickle.dump(tallycoLoad, open("tallyco.conf", "wb"))

def tallycoGetPayment():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    c = loadFileConnTallyCo(['id'])
    d = str(c['id'])
    try:
        amount = input("Amount in Sats: ")
        print("""\nPayment Method Example: 'ln' or 'btc'
                 'ln' = Lightnin Netowrk
                 'btc'= Bitcoin Onchain Payment
                    \n""")
        lnd_onchain = input("Payment Method: ")
        curl = (
            "curl -d "
            + f'"type=profile&id={d}&satoshi_amount={amount}&payment_method={lnd_onchain}"'
            + " -X POST https://api.tallyco.in/v1/payment/request/"
        )

        tallycomethod = os.popen(curl).read()
        n = str(tallycomethod)
        d = json.loads(n)
        clear()
        blogo()
        if lnd_onchain == "ln":
            e = d['lightning_pay_request']
            f = e.lower()
            print("\033[1;30;47m")
            qr.add_data(f)
            qr.print_ascii()
            print("\033[0;37;40m")
            print(f'LND Invoice: {f}')
            qr.clear()
            input("\nContinue...")
        elif lnd_onchain == "btc":
            e = d['btc_address']
            print("\033[1;30;47m")
            qr.add_data(e)
            qr.print_ascii()
            print("\033[0;37;40m")
            print(f'Amount: {d["cost"]}')
            print(f'Bitcoin Address: {e}')
            qr.clear()
            input("\nContinue...")
    except:
        pass


def tallycoDonateid():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    clear()
    blogo()
    try:
        donate = input("Donate to ID: ")
        amount = input("Amount in Sats: ")
        print("""\nPayment Method Example: 'ln' or 'btc'
                 'ln' = Lightnin Netowrk
                 'btc'= Bitcoin Onchain Payment
                    \n""")
        lnd_onchain = input("Payment Method: ")
        curl = (
            "curl -d "
            + f'"type=profile&id={donate}&satoshi_amount={amount}&payment_method={lnd_onchain}"'
            + " -X POST https://api.tallyco.in/v1/payment/request/"
        )

        tallycomethod = os.popen(curl).read()
        n = str(tallycomethod)
        d = json.loads(n)
        clear()
        blogo()
        if lnd_onchain in ["ln", "lN", "Ln", "LN"]:
            node_not = input("Do you want to pay this tip with your node? Y/n: ")
            if node_not in ["Y", "y"]:
                lndconnectload = {"ip_port":"", "tls":"", "macaroon":"", "ln":""}
                lndconnectData = pickle.load(open("blndconnect.conf", "rb")) # Load the file 'bclock.conf'
                lndconnectload = lndconnectData # Copy the variable pathv to 'path'
                if lndconnectload['ip_port']:
                    e = d['lightning_pay_request']
                    f = e.lower()
                    print("\nInvoice: " + f + "\n")
                    payinvoice()
                elif lndconnectload['ln']:
                    e = d['lightning_pay_request']
                    f = e.lower()
                    print("\nInvoice: " + f + "\n")
                    localpayinvoice()
            elif node_not in ["N", "n"]:
                e = d['lightning_pay_request']
                f = e.lower()
                print("\033[1;30;47m")
                qr.add_data(f)
                qr.print_ascii()
                print("\033[0;37;40m")
                print(f'LND Invoice: {f}')
                qr.clear()
                input("\nContinue...")
        elif lnd_onchain in ["btc", "bTC", "BtC", "BTC", "BTc", "btC"]:
            e = d['btc_address']
            print("\033[1;30;47m")
            qr.add_data(e)
            qr.print_ascii()
            print("\033[0;37;40m")
            print(f'Amount: {d["cost"]}')
            print(f'Bitcoin Address: {e}')
            qr.clear()
            input("\nContinue...")
    except:
        pass


#-----------------------------END TALLYCOIN------------------------------
#-----------------------------MEMPOOL.SPACE------------------------------

def fee():
    try:
        while True:
            r = requests.get('https://mempool.space/api/v1/fees/recommended')
            r.headers['Content-Type']
            n = r.text
            di = json.loads(n)
            clear()
            blogo()
            print("""
            ------------------------
                Fastest Fee:   {}
                Half Hour Fee: {}
                Hour Fee:      {}
            ------------------------
            <<< Back Control + C
            """.format(di['fastestFee'], di['halfHourFee'], di['hourFee']))
            t.sleep(5)
            print("\n\t    Getting New Information")
    except:
        pass

def blocks():
    try:
        while True:
            clear()
            blogo()
            print("\n\t             Getting New Information")
            r = requests.get('https://mempool.space/api/v1/fees/mempool-blocks')
            r.headers['Content-Type']
            n = r.text
            di = json.loads(n)
            for n in range(len(di)):
                q = di[n]
                clear()
                blogo()
                print("""
                -----------------------------------------
                                  BLOCK
                -----------------------------------------
                    Block Size:   {} bytes
                    Block VSize:  {} bytes
                    Transactions: {}
                    Total Fees:   {}
                    Median Fee:   {}
                -----------------------------------------
                <<< Back Control + C
                """.format(q['blockSize'], q['blockVSize'], q['nTx'], q['totalFees'], q['medianFee']))
                t.sleep(3)
    except:
        pass



def remoteHalving():
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except:
        pass

def remotegetblock():
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except:
        pass

def remotegetblockcount(): # get access to bitcoin-cli with the command getblockcount
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except:
        pass

def remoteconsole(): # get into the console from bitcoin-cli
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except:
        pass

def runthenumbersConn():
    try:
        conn = """curl -s https://bitcoinexplorer.org/api/blockchain/coins"""
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render("total amount", colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\n")
    except:
        pass

def channelbalance():
    try:
        conn = """curl -s https://bitcoinexplorer.org/api/blockchain/coins"""
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render("channel balance", colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\n")
    except:
        pass


def listonchaintxs():
    try:
        clear()
        blogo()
        output = render(
            "Onchain Txs", colors=['yellow'], align='left', font='tiny'
        )

        print(output)
        responseC = input("TX ID: ")
        url2 = f'https://mempool.space/api/tx/{responseC}'
        r = requests.get(url2)
        r2 = str(r.text)
        r3 = r2
        clear()
        blogo()
        print("\nTransaction ID: " + responseC)
        print(f'Onchain Txs: {r3}')
        input("\n")
    except:
        pass

def balanceOC():
    try:
        conn = """curl -s https://bitcoinexplorer.org/api/blockchain/coins"""
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render("balance", colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\n")
    except:
        pass

def localkeysendC():
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except:
        pass

def localchatsendAC():
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except:
        pass


def localchatnewAC():
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except:
        pass

def localchatlistAC():
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except:
        pass

def localchatsendBC():
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except:
        pass

def localchatnewBC():
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except:
        pass

def localchatlistBC():
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except:
        pass

def localchatsendCC():
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except:
        pass

def localchatnewCC():
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except:
        pass

def localchatlistCC():
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except:
        pass

def localchannelbalanceC():
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except:
        pass

def localnewaddressC():
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except:
        pass

def localbalanceOCC():
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except:
        pass

def localrebalancelndC():
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except:
        pass

# Remote connection with rest -------------------------------------

def getnewinvoice():
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except:
        pass

def payinvoice():
    try:
        clear()
        blogo()
        output = render(
            "invoice decoder", colors=['yellow'], align='left', font='tiny'
        )

        print(output)
        responseC = input("Invoice: ")
        url2 = f'https://lndecode.com/?invoice={responseC}'
        r = requests.get(url2)
        r2 = str(r.text)
        r3 = r2
        clear()
        blogo()
        print("\nInvoice: " + responseC)
        print(f'Invoice: {r3}')
        input("\n")
    except:
        pass

def getnewaddress():
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except:
        pass

def listinvoice():
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except:
        pass

def getinfo():
    try:
        clear()
        blogo()
        output = render(
            "node info", colors=['yellow'], align='left', font='tiny'
        )

        print(output)
        responseC = input("Public Key: ")
        list = f"curl -s 'https://1ml.com/node/'{responseC}/json'"
        a = os.popen(list).read()
        clear()
        blogo()
        print("\nNode: " + responseC)
        print(a)
        input("\a\nContinue...")
    except:
        pass


def consoleLNC(): # get into the console from bitcoin-cli
    try:
        conn = """curl -s https://github.com/tomosaigon/lncli-commands | html2text | grep -E "## COMMANDS" -A 120"""
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render("lncli-commands", colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\n")
    except:
        pass

def locallistpeersQQC():
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except:
        pass

def localconnectpeerC():
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except:
        pass

def locallistchaintxnsC():
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except:
        pass

def locallistinvoicesC():
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except:
        pass

def locallistchannelsC():
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except:
        pass

def localgetinfoC():
    try:
        clear()
        blogo()
        output = render(
            "node info", colors=['yellow'], align='left', font='tiny'
        )

        print(output)
        responseC = input("Public Key: ")
        list = f"curl -s https://1ml.com/node/{responseC}/json"
        a = os.popen(list).read()
        clear()
        blogo()
        print("\nNode: " + responseC)
        print(a)
        input("\nContinue...")
    except:
        pass

def localaddinvoiceC():
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except:
        pass

def localpayinvoiceC():
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except:
        pass

def localgetnetworkinfoC():
    try:
        conn = """curl -s https://1ml.com/trends | html2text | grep -E "Increase|Decrease" -A 4 | tr -d '{|}|]|,' | tr -d '"' | tr -d '* [' | tr -d '-' | tr -d '#' | xargs -L 1"""
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render(
            "lightning network info", colors=['yellow'], align='left', font='tiny'
        )

        print(output)
        print(a)
        input("\a\n")
    except:
        pass

#-----------------------------Slush--------------------------------

def slDIFFConn():
    try:
        conn = """curl -s https://insights.braiins.com/api/v1.0/difficulty-stats"""
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render("difficulty", colors=['yellow'], align='left', font='tiny')
        print(output)
        b = json.loads(a)
        print(f"""\n

            Block epoch: {b['blocks_epoch']}
            Difficulty: {b['difficulty']}
            Epoch block time: {b['epoch_block_time']}
            Estimated adjustment: {b['estimated_adjustment']}
            Estimated adjustemnt date: {b['estimated_adjustment_date']}
            Estimated next differece: {b['estimated_next_diff']}
            Previous adjustment: {b['previous_adjustment']}

        """)
        input("\a\nContinue...")
    except:
        pass

def slHASHConn():
    try:
        conn = """curl -s https://insights.braiins.com/api/v1.0/hash-rate-stats"""
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render("hash rate", colors=['yellow'], align='left', font='tiny')
        print(output)
        b = json.loads(a)
        print(f"""\n

            Averiage fees per block: {b['avg_fees_per_block']}
            Current hashrate: {b['current_hashrate']}
            Fees percent: {b['fees_percent']}
            Hash price: {b['hash_price']}
            Hash rate 30: {b['hash_rate_30']}
            Hash value: {b['hash_value']}
            Rev. USD: {b['rev_usd']}

        """)
        input("\a\nContinue...")
    except:
        pass

def slPOOLConn():
    try:
        conn = """curl -s https://insights.braiins.com/api/v1.0/pool-stats?json=1 | jq -C '.[]' | tr -d '{|}|]|,' | xargs -L 1 | grep -E " " """
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render("pool", colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\nContinue...")
    except:
        pass

def slHISTConn():
    try:
        conn = """curl -s https://insights.braiins.com/api/v1.0/hashrate-and-difficulty-history?json=1 | jq -C '.[]' | tr -d '{|}|]|,' | xargs -L 1 | grep -E " " """
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render("history", colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\nContinue...")
    except:
        pass

def getPoolSlushCheck():

    s = ""
    sq = s

    api = ""
    try:
        if os.path.isfile("config/slushAPI.conf"):
            apiv = pickle.load(open("config/slushAPI.conf", "rb"))
            api = apiv
        else:
            clear()
            blogo()
            api = input("Insert SlushPool API KEY: ")
            pickle.dump(api, open("config/slushAPI.conf", "wb"))
    except:
        pass

    while True:
        try:
            slushpoolbtc = f"curl https://slushpool.com/accounts/profile/json/btc/ -H 'SlushPool-Auth-Token: {api}' 2>/dev/null"

            slushpoolbtcblock = f"curl https://slushpool.com/stats/json/btc/ -H 'SlushPool-Auth-Token: {api}' 2>/dev/null"


            b = os.popen(slushpoolbtc)
            c = b.read()
            d = json.loads(c)
            f = d['btc']

            bblock = os.popen(slushpoolbtcblock)
            cblock = bblock.read()
            dblock = json.loads(cblock)
            fblock = dblock['btc']
            eblock = fblock['blocks']
            for i in eblock:
            	qnq = sorted(eblock)
            	for n in qnq:
            		s = n

            if s > sq:
                newblock = f"\a\n\n\t\t\u001b[31;1m    New Block Mined \u001b[38;5;27m{s}\u001b[31;1m! \u001b[38;5;202mFresh sats for you!\033[0;37;40m"

                sq = s
            else:
                newblock = s

            clear()
            blogo()
            print("""\033[A

    --------------------------------------------------------------------------------------------

                        \033[0;37;40mBraiins Pool

                        Username: {}
                        Confirmed reward: \u001b[38;5;40m{}\033[0;37;40m BTC
                        Unconfirmed reward: \u001b[33;1m{}\033[0;37;40m BTC
                        Estimated reward: {} BTC
                        All Time reward: {} BTC
                        Hash Rate 5m: {} Gh/s
                        Hash Rate 60m: {} Gh/s
                        Hash Rate 24h: {} Gh/s
                        Hash Rate Scoring: \u001b[38;5;27m{}\033[0;37;40m Gh/s
                        Hash Rate Yesterday: {} Gh/s
                        Connected Workers: {}
                        Disconnected Workers: {}
                        Last Block discovered: {}

    --------------------------------------------------------------------------------------------

            \033[A""".format(d['username'], f['confirmed_reward'], f['unconfirmed_reward'], f['estimated_reward'], f['all_time_reward'], f['hash_rate_5m'], f['hash_rate_60m'], f['hash_rate_24h'], f['hash_rate_scoring'], f['hash_rate_yesterday'], f['ok_workers'], f['off_workers'],newblock))

            t.sleep(10)

        except:
            break


#-----------------------------END Slush--------------------------------

def ckpoolpoolLOCALOnchainONLY():

    s = ""
    sq = s

    api = ""
    try:
        if os.path.isfile("config/CKPOOLAPI.conf"):
            apiv = pickle.load(open("config/CKPOOLAPI.conf", "rb"))
            api = apiv
        else:
            clear()
            blogo()
            api = input("Insert CKPool Wallet.Worker: ")
            pickle.dump(api, open("config/CKPOOLAPI.conf", "wb"))
    except:
        pass

    while True:
        try:
            ckpool = f"curl https://solo.ckpool.org/users/{api} 2>/dev/null"


            b = os.popen(ckpool)
            c = b.read()
            d = json.loads(c)
            f = d['worker']
            e = f[0]

            clear()
            blogo()
            print("""\033[A

    --------------------------------------------------------------------------------------------

                        \033[0;37;40mCKPool BTC

                        Username: {}
                        Hash Rate 1m: {}
                        Hash Rate 5m: {}
                        Hash Rate 1h: {}
                        Hash Rate 1d: {}
                        Hash Rate 7d: {}
                        Last Share: \u001b[38;5;27m{}\033[0;37;40m
                        Shares: {}
                        Best Share: {}
                        Best Ever: {}
                        Workers: {}

    --------------------------------------------------------------------------------------------

            \033[A""".format(e['workername'], e['hashrate1m'], e['hashrate5m'], e['hashrate1hr'], e['hashrate1d'], e['hashrate7d'], e['lastshare'], e['shares'], e['bestshare'], e['bestever'], d['workers']))

            t.sleep(10)

        except:
            break


def kanopoolpoolLOCALOnchainONLY():

    s = ""
    sq = s

    api = ""
    try:
        if os.path.isfile("config/KANOPOOLUSER.conf", "config/KANOPOOLAPI.conf"):
            apiv = pickle.load(open("config/KANOPOOLUSER.conf", "rb"))
            api = apiv
            apiv2 = pickle.load(open("config/KANOPOOLAPI.conf", "rb"))
            api2 = apiv2
        else:
            clear()
            blogo()
            api = input("Insert KanoPool Username: ")
            pickle.dump(api, open("config/KANOPOOLUSER.conf", "wb"))
            api2 = input("Insert KanoPool API KEY: ")
            pickle.dump(api2, open("config/KANOPOOLAPI.conf", "wb"))
    except:
        pass

    while True:
        try:
            kanopool = f"curl https://kano.is/index.php?k=api&username={api}&api={api2}&json=y&work=y 2>/dev/null"


            b = os.popen(kanopool)
            c = b.read()
            d = json.loads(c)
            f = d['worker']
            e = f[0]

            clear()
            blogo()
            print("""\033[A

    --------------------------------------------------------------------------------------------

                        \033[0;37;40mKanoPool BTC

                        Username: {}
                        Hash Rate 1m: {}
                        Hash Rate 5m: {}
                        Hash Rate 1h: {}
                        Hash Rate 1d: {}
                        Hash Rate 7d: {}
                        Last Share: \u001b[38;5;27m{}\033[0;37;40m
                        Shares: {}
                        Best Share: {}
                        Best Ever: {}
                        Workers: {}

    --------------------------------------------------------------------------------------------

            \033[A""".format(e['workername'], e['hashrate1m'], e['hashrate5m'], e['hashrate1hr'], e['hashrate1d'], e['hashrate7d'], e['lastshare'], e['shares'], e['bestshare'], e['bestever'], d['workers']))

            t.sleep(10)

        except:
            break


def getblock():
    try:
        conn = """curl -s https://developer.bitcoin.org/reference/rpc/getblockchaininfo.html | html2text | grep -E Result -A 50 | grep -v Result """
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render("getblockchaininfo", colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\nContinue...")
    except:
        pass

def searchTXS():
    try:
        clear()
        blogo()
        output = render(
            "Tx", colors=['yellow'], align='left', font='tiny'
        )

        print(output)
        responseC = input("TX: ")
        url2 = f'https://mempool.space/api/tx/{responseC}'
        r = requests.get(url2)
        r2 = str(r.text)
        r3 = r2
        clear()
        blogo()
        print("\nTransaction ID: " + responseC)
        print(f'Tx: {r3}')
        input("\n")
    except:
        pass

def untxsConn():
    try:
        conn = """curl -s https://mempool.space/api/mempool/txids | jq -C '.[]' """
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render("uncorfirmed txs", colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\nContinue...")
    except:
        pass

def getnewaddressOnchain():
    try:
        clear()
        blogo()
        closed()
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except:
        pass

def gettransactionsOnchain():
    try:
        clear()
        blogo()
        output = render(
            "Tx", colors=['yellow'], align='left', font='tiny'
        )

        print(output)
        responseC = input("TX: ")
        url2 = f'https://mempool.space/api/tx/{responseC}'
        r = requests.get(url2)
        r2 = str(r.text)
        r3 = r2
        clear()
        blogo()
        print("\nTransaction ID: " + responseC)
        print(f'Tx: {r3}')
        input("\n")
    except:
        pass

def getblockcount(): # get access to bitcoin-cli with the command getblockcount
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except:
        pass

def getbestblockhash():
    try:
        clear()
        blogo()
        output = render(
            "Block Hash", colors=['yellow'], align='left', font='tiny'
        )

        print(output)
        responseC = input("Shot enter to view the hash ")
        url2 = f'https://mempool.space/api/blocks/tip/hash{responseC}'
        r = requests.get(url2)
        r2 = str(r.text)
        r3 = r2
        clear()
        blogo()
        print("\nHash: " + responseC)
        print(f'Block Hash {r3}')
        input("\n")
    except:
        pass

def clear(): # clear the screen
    os.system('cls' if os.name=='nt' else 'clear')

def getgenesis():
    try:
        conn = """curl -s https://en.bitcoin.it/wiki/Genesis_block | html2text | grep -E 52706 -A 48 | grep -v 52706"""
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render("genesis", colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\n")
    except:
        pass

def readHexBlock():
    try:
        clear()
        blogo()
        output = render(
            "Block", colors=['yellow'], align='left', font='tiny'
        )

        print(output)
        responseC = input("BLOCK: ")
        list = f"curl -s 'https://mempool.space/api/tx/{responseC}/hex' "
        a = os.popen(list).read()
        clear()
        blogo()
        print("\nHex: " + responseC)
        print("\nPyBLOCK Hex: " + a)
        input("\nContinue...")
    except:
        pass

def readHexTx():
    try:
        clear()
        blogo()
        output = render(
            "Block", colors=['yellow'], align='left', font='tiny'
        )

        print(output)
        responseC = input("BLOCK: ")
        list = f"curl -s https://mempool.space/api/blocks/{responseC}"
        a = os.popen(list).read()
        clear()
        blogo()
        print("\nBlock: " + responseC)
        print("\nPyBLOCK Decoded: " + a)
        input("\nContinue...")
    except:
        pass

def console(): # get into the console from bitcoin-cli
    try:
        clear()
        blogo()
        output = render(
            "RPC", colors=['yellow'], align='left', font='tiny'
        )

        print(output)
        responseC = input("RPC Command: ")
        list = f"""curl -s 'https://bitcoinexplorer.org/rpc-browser?method={responseC}#Help-Content' | html2text | grep -E "Arguments" -A 777 | grep -E -v "Recent|https|http|version|commit|released|Hidden Service|on Twitter|explorer|###### Project|###### App Details|###### Links" """
        a = os.popen(list).read()
        clear()
        blogo()
        print("\nRPC: " + responseC)
        print("\nPyBLOCK Help: " + a)
        input("\n")
    except:
        pass

def screensv():
    try:
        doit()
    except (KeyboardInterrupt, SystemExit):
        matrix.close()
        clear()
        blogo()
        menu()

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.25)
#------------------------------------------------------

def artist(): # here we convert the result of the command 'getblockcount' on a random art design
    while True:
        try:
            clear()
            close()
            design()
        except:
            break

def design():
    if os.path.isfile('config/pyblocksettingsClock.conf') or os.path.isfile('config/pyblocksettingsClock.conf'): # Check if the file 'bclock.conf' is in the same folder
        settingsv = pickle.load(open("config/pyblocksettingsClock.conf", "rb")) # Load the file 'bclock.conf'
        settingsClock = settingsv # Copy the variable pathv to 'path'
    else:
        settingsClock = {"gradient":"", "design":"block", "colorA":"green", "colorB":"yellow"}
        pickle.dump(settingsClock, open("config/pyblocksettingsClock.conf", "wb"))
    clear()
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    n = r.text
    di = json.loads(n)
    a = di
    b = str(a)
    clear()
    close()
    output = render(str(a), colors=[settingsClock['colorA'], settingsClock['colorB']], align='center')
    print("\033[0;37;40m\x1b[?25l" + output)
    while True:
        x = b
        r = requests.get('https://mempool.space/api/blocks/tip/height')
        r.headers['Content-Type']
        n = r.text
        di = json.loads(n)
        a = di
        if x < str(a):
            clear()
            close()
            output5 = subprocess.check_output(['sudo', 'iwgetid'])
            z = str(output5)
            pp = random.choice(list(faceshappy.values())).encode('utf-8').decode('latin-1')
            output = render(str(a), colors=[settingsClock['colorA'], settingsClock['colorB']], align='center')
            print("\033[0;37;40m\x1b[?25l" + output)
            b = str(a)    #try:

#--------------------------------- Hex Block Decoder Functions -------------------------------------

def getrawtx(): # show confirmations from transactions
    try:
        clear()
        blogo()
        output = render(
            "Tx", colors=['yellow'], align='left', font='tiny'
        )

        print(output)
        responseC = input("Tx: ")
        list = (
            f"curl -s https://mempool.space/api/tx/{responseC}"
            + """/merkle-proof | jq -C '.[]'"""
        )

        a = os.popen(list).read()
        clear()
        blogo()
        print("\nTx: " + responseC)
        print("\nMerkle Proof: " + a)
        input("\nContinue...")
    except:
        pass

def runthenumbers():
    try:
        conn = """curl -s https://bitcoinexplorer.org/api/blockchain/coins"""
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render("total amount", colors=['yellow'], align='left', font='tiny')
        outputT = render(f"{a} sats", colors=['green'], align='left', font='tiny')
        print(output)
        print(outputT)
        input("\a\nContinue...")
    except:
        pass

def countdownblock():
    try:
        clear()
        blogo()
        closed()
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except:
        pass

def countdownblockConn():
    try:
        clear()
        blogo()
        closed()
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except:
        pass

def localHalving():
    try:
        conn = """curl -s https://www.bitcoinblockhalf.com/ | html2text | grep -E "Blocks until mining reward is halved" | tr -d '*' """
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render("blocks to halving", colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\nContinue...")
    except:
        pass

#--------------------------------- End Hex Block Decoder Functions -------------------------------------

def pdfconvert():
    try:
        conn = """curl -s https://nakamotoinstitute.org/bitcoin/ | html2text | grep October -A 428"""
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render("whitepaper", colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\nControl + C...")
    except:
        pass

#--------------------------------- NYMs -----------------------------------

def get_ansi_color_code(r, g, b):
    if r == g == b:
        if r < 8:
            return 16
        return 231 if r > 248 else round(((r - 8) / 247) * 24) + 232
    return 16 + (36 * round(r / 255 * 5)) + (6 * round(g / 255 * 5)) + round(b / 255 * 5)


def get_color(r, g, b):
    return f"\x1b[48;5;{int(get_ansi_color_code(r, g, b))}m \x1b[0m"


def robotNym():
    try:
        if path['bitcoincli']:
            lncli = " getinfo"
            lsd = os.popen(lndconnectload['ln'] + lncli).read()
            lsd0 = str(lsd)
            alias = json.loads(lsd0)
        else:
            cert_path = lndconnectload["tls"]
            macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
            headers = {'Grpc-Metadata-macaroon': macaroon}
            url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
            r = requests.get(url, headers=headers, verify=cert_path)
            alias = r.json()

        hash = alias['identity_pubkey']
        rh = Robohash(hash)
        rh.assemble(roboset='set1')
        with open("file.png", "wb") as f:
        	rh.img.save(f, format="png")

        img_path = open("file.png", "rb")
        img = Image.open(img_path)

        h = 40
        w = int((img.width / img.height) * 90)

        img = img.resize((w,h), Image.ANTIALIAS)
        img_arr = np.asarray(img)
        h,w,c = img_arr.shape

        for x in range(h):
            for y in range(w):
                pix = img_arr[x][y]
                print(get_color(pix[0], pix[1], pix[2]), sep='', end='')
            print()
        image = "\n\t\t\t\t\t    \u001b[31;1mNode\u001b[38;5;93mNym\033[0;37;40m\n"+ "\n\t         \u001b[33;1m" + alias['identity_pubkey'] + "\033[0;37;40m"
        print(image)
        input("\n\nContinue...")
    except:
        menuSelection()


#---------------------------------Warden Terminal----------------------------------
def callGitWardenTerminal():
    if not os.path.isdir('warden_terminal'):
        git = "git clone https://github.com/pxsocs/warden_terminal.git"
        os.system(git)
    os.system("cd warden_terminal && python3 node_warden.py")

#---------------------------------Nostr Terminal----------------------------------
def callGitNostrMacTerminal():
    try:
        clear()
        blogo()
        output = render(
            "Nostr Console macOS", colors=['yellow'], align='left', font='tiny'
        )
        if os.path.isdir ('nostr_console_pyblock'):
            os.system("cd nostr_console_pyblock && rm -rf nostr_console_macOS && wget https://raw.githubusercontent.com/curly60e/pyblock/master/pybitblock/nostr_console_pyblock/nostr_console_macOS && chmod 777 *")
        else: # Check if the file 'bclock.conf' is in the same folder
            os.system("mkdir nostr_console_pyblock && cd nostr_console_pyblock && wget https://raw.githubusercontent.com/curly60e/pyblock/master/pybitblock/nostr_console_pyblock/nostr_console_macOS")
        clear()
        blogo()

        print(output)
        responseC = input("Paste your PrivateKey: ")
        os.system(f"cd nostr_console_pyblock && ./nostr_console_macOS -k {responseC}")
    except:
        menuSelection()

def callGitNostrWinTerminal():
    try:
        clear()
        blogo()
        output = render(
            "Nostr Console Windows", colors=['yellow'], align='left', font='tiny'
        )
        if os.path.isdir ('nostr_console_pyblock'):
            os.system("cd nostr_console_pyblock && rm -rf nostr_console_win64.exe && wget https://raw.githubusercontent.com/curly60e/pyblock/master/pybitblock/nostr_console_pyblock/nostr_console_win64.exe && chmod 777 *")
        else: # Check if the file 'bclock.conf' is in the same folder
            os.system("mkdir nostr_console_pyblock && cd nostr_console_pyblock && wget https://raw.githubusercontent.com/curly60e/pyblock/master/pybitblock/nostr_console_pyblock/nostr_console_win64.exe")
        clear()
        blogo()
        print(output)
        responseC = input("Paste your PrivateKey: ")
        os.system(f"cd nostr_console_pyblock && ./nostr_console_win64.exe -k {responseC}")
    except:
        menuSelection()

def callGitNostrLinTerminal():
    try:
        clear()
        blogo()
        output = render(
            "Nostr Console Linux", colors=['yellow'], align='left', font='tiny'
        )
        if os.path.isdir ('nostr_console_pyblock'):
            os.system("cd nostr_console_pyblock && rm -rf nostr_console_elf64 && wget https://raw.githubusercontent.com/curly60e/pyblock/master/pybitblock/nostr_console_pyblock/nostr_console_elf64 && chmod 777 *")
        else: # Check if the file 'bclock.conf' is in the same folder
            os.system("mkdir nostr_console_pyblock && cd nostr_console_pyblock && wget https://raw.githubusercontent.com/curly60e/pyblock/master/pybitblock/nostr_console_pyblock/nostr_console_elf64 && chmod 777 *")
        clear()
        blogo()
        print(output)
        responseC = input("Paste your PrivateKey: ")
        os.system(f"cd nostr_console_pyblock && ./nostr_console_elf64 -k {responseC}")
    except:
        menuSelection()

def callGitNostrSeedTerminal():
    try:
        clear()
        blogo()
        output = render(
            "Nostr BIP39", colors=['yellow'], align='left', font='tiny'
        )
        if os.path.isdir ('nostr_seed'):
            print("...pass...")
        else: # Check if the file 'bclock.conf' is in the same folder
            os.system("mkdir nostr_seed && cd nostr_seed && wget https://gist.githubusercontent.com/odudex/93cfb5628b22f8675ab1939fd43133f4/raw/b48f047c0358a9ae50c2027106bdf5e37ee1fe5c/nostr_seed.py")
        clear()
        blogo()
        print(output)
        responseC = input("Paste your PrivateKey to convert into 24 BIP39 Seed words and vice-versa: ")
        os.system(f"cd nostr_seed && python3 nostr_seed.py {responseC}")
        input("\a\nContinue...")
    except:
        menuSelection()
#---------------------------------Cashu----------------------------------
def callGitCashu():
    if not os.path.isdir('Cashu'):
        git = "pip3 install cashu && mkdir Cashu"
        os.system(git)
    os.system("cd Cashu && cashu")

#---------------------------------ColdCore-----------------------------------------
def callColdCore():
    clear()
    blogo()
    close()
    try:
        if not os.path.isfile('$HOME/.pyblock/public.txt'):
            msg = """
            \033[0;37;40m-------------------------\a\u001b[31;1mFILE NOT FOUND\033[0;37;40m----------------------------
                    To ColdCore works it needs to import your wallet's
                        public information on your coldcard, go to
                        -----------------------------------------
                        |                                       |
                        |    \033[1;37;40mAdvanced > MicroSD > Dump Summary\033[0;37;40m  |
                        |                                       |
                        -----------------------------------------
                             Copy the file \033[1;37;40mpublic.txt\033[0;37;40m inside
                                the main \u001b[31;1mpyblock\033[0;37;40m folder
              (see: https://coldcardwallet.com/docs/microsd#dump-summary-file)
            -------------------------------------------------------------------"""
            print(msg)
            input("\nContinue...")
        else:
            if not os.path.isdir('$HOME/.pyblock/coldcore'):
                git = "git clone https://github.com/jamesob/coldcore.git"
                install = "cd coldcore && chmod +x coldcore && cp coldcore ~/.local/bin/coldcore"
                os.system(git)
                os.system(install)
            os.system("coldcore")
    except:
        menuSelection()

#--------------------------------- Menu section -----------------------------------

def MainMenuCROPPED(): #Main Menu
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m\a
    \033[1;37;40mVersion\033[0;37;40m: {}


    \u001b[31;1mA.\033[0;37;40m PyBLOCK
    \u001b[38;5;202mB.\033[0;37;40m Bitcoin Core
    \u001b[33;1mL.\033[0;37;40m Lightning Network
    \u001b[38;5;40mP.\033[0;37;40m Platforms
    \u001b[38;5;27mS.\033[0;37;40m Settings
    \u001b[38;5;15mX.\033[0;37;40m Donate
    \u001b[38;5;93mQ.\033[0;37;40m Exit
    \n\n\x1b[?25h""".format(n,b, version, checkupdate()))
    mainmenuLOCALcontrol(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def bitcoincoremenuLOCAL():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Bitcoin-cli Console
    \u001b[38;5;202mB.\033[0;37;40m Show Genesis Block
    \u001b[38;5;202mC.\033[0;37;40m Show Blockchain Information
    \u001b[38;5;202mD.\033[0;37;40m Run the Numbers
    \u001b[38;5;202mE.\033[0;37;40m Decode Block
    \u001b[38;5;202mF.\033[0;37;40m Show QR from a Bitcoin Address
    \u001b[38;5;202mG.\033[0;37;40m Show Merkle Proof from a Tx
    \u001b[38;5;202mH.\033[0;37;40m Miscellaneous
    \u001b[38;5;202mI.\033[0;37;40m ColdCore
    \u001b[38;5;202mJ.\033[0;37;40m Whitepaper
    \u001b[38;5;202mM.\033[0;37;40m Moscow Time
    \u001b[38;5;202mO.\033[0;37;40m OP_RETURN
    \u001b[38;5;202mZ.\033[0;37;40m Stats
    \u001b[38;5;202mQ.\033[0;37;40m Hashrate
    \u001b[38;5;202mU.\033[0;37;40m Unconfirmed Txs
    \u001b[38;5;202mS.\033[0;37;40m Mempool
    \u001b[33;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,b, version, checkupdate()))
    bitcoincoremenuLOCALcontrolA(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def bitcoincoremenuLOCALOPRETURN():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Send OP_RETURN
    \u001b[38;5;202mB.\033[0;37;40m View OP_RETURN
    \u001b[38;5;202mC.\033[0;37;40m View Decoded Coinbase
    \u001b[33;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,b, version, checkupdate()))
    bitcoincoremenuLOCALcontrolO(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def lightningnetworkLOCAL():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[33;1mA.\033[0;37;40m Lncli Console
    \u001b[33;1mB.\033[0;37;40m New Invoice
    \u001b[33;1mC.\033[0;37;40m Pay Invoice
    \u001b[33;1mD.\033[0;37;40m Make a KeySend Payment
    \u001b[33;1mE.\033[0;37;40m New Bitcoin Address
    \u001b[33;1mF.\033[0;37;40m List Invoices
    \u001b[33;1mG.\033[0;37;40m Channel Balance
    \u001b[33;1mH.\033[0;37;40m Show Channels
    \u001b[33;1mI.\033[0;37;40m Rebalance Channel
    \u001b[33;1mJ.\033[0;37;40m Show Peers
    \u001b[33;1mK.\033[0;37;40m Connect Peers
    \u001b[33;1mL.\033[0;37;40m Onchain Balance
    \u001b[33;1mM.\033[0;37;40m List Onchain Transactions
    \u001b[33;1mN.\033[0;37;40m Get Node Info
    \u001b[33;1mO.\033[0;37;40m Get Network Information
    \u001b[33;1mP.\033[0;37;40m PyChat
    \u001b[33;1mZ.\033[0;37;40m Stats
    \u001b[33;1mT.\033[0;37;40m Ranking
    \u001b[33;1mQ.\033[0;37;40m LNBits List LNURL     \033[3;35;40m{lnbitspaid}\033[0;37;40m
    \u001b[33;1mS.\033[0;37;40m LNBits Create LNURL   \033[3;35;40m{lnbitspaid}\033[0;37;40m
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,b, version, checkupdate(), lnbitspaid = "UNLOCKED" if os.path.isfile("lnbitSN.conf") else "LOCKED"))
    lightningnetworkLOCALcontrol(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def chatConn():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Open
    \u001b[38;5;202mB.\033[0;37;40m Close
    \u001b[38;5;202mC.\033[0;37;40m Hidden
    \u001b[31;1mQ.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, b, version, checkupdate()))
    chatConnA(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def pyCHATA():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)

    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Write
    \u001b[38;5;202mB.\033[0;37;40m Read
    \u001b[38;5;202mC.\033[0;37;40m List
    \u001b[31;1mQ.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, b, version, checkupdate()))
    chatConnB(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def pyCHATB():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)

    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Write
    \u001b[38;5;202mB.\033[0;37;40m Read
    \u001b[38;5;202mC.\033[0;37;40m List
    \u001b[31;1mQ.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, b, version, checkupdate()))
    chatConnC(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def pyCHATC():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)

    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Write
    \u001b[38;5;202mB.\033[0;37;40m Read
    \u001b[38;5;202mC.\033[0;37;40m List
    \u001b[31;1mQ.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, b, version, checkupdate()))
    chatConnD(input("\033[1;32;40mSelect option: \033[0;37;40m"))


def APIMenuLOCAL():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m TippinMe      FREE
    \033[1;32;40mB.\033[0;37;40m Tallycoin     FREE
    \033[1;32;40mC.\033[0;37;40m Mempool       FREE
    \033[1;32;40mD.\033[0;37;40m CoinGecko     FREE
    \033[1;32;40mE.\033[0;37;40m Rate.sx       FREE
    \033[1;32;40mF.\033[0;37;40m BWT           FREE
    \033[1;32;40mG.\033[0;37;40m LNBits        \033[3;35;40m{lnbitspaid}\033[0;37;40m
    \033[1;32;40mH.\033[0;37;40m LNPay         \033[3;35;40m{lnpaypaid}\033[0;37;40m
    \033[1;32;40mI.\033[0;37;40m OpenNode      \033[3;35;40m{opennodepaid}\033[0;37;40m
    \033[1;32;40mJ.\033[0;37;40m SatNode       FREE
    \033[1;32;40mK.\033[0;37;40m Weather       FREE
    \033[1;32;40mL.\033[0;37;40m Arcade        FREE
    \033[1;32;40mM.\033[0;37;40m Whale Alert   FREE
    \033[1;32;40mN.\033[0;37;40m Nostr         FREE
    \033[1;32;40mS.\033[0;37;40m Braiins Pool  FREE
    \033[1;32;40mW.\033[0;37;40m CKPool        FREE
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,b, version, checkupdate(),lnbitspaid = "PAID" if os.path.isfile("lnbitSN.conf") else "PREMIUM", lnpaypaid = "PAID" if os.path.isfile("lnpaySN.conf") else "PREMIUM", opennodepaid = "PAID" if os.path.isfile("opennodeSN.conf") else "PREMIUM"))
    platfformsLOCALcontrol(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def decodeHex(): # show hex
    try:
        clear()
        blogo()
        output = render(
            "decode", colors=['yellow'], align='left', font='tiny'
        )

        print(output)
        responseC = input("Block Height: ")
        list = (
            f"curl -s 'https://bitcoinexplorer.org/api/block/'{responseC}"
            + """ | jq -C '.[]' | tr -d '{|}|]|,'"""
        )
        a = os.popen(list).read()
        clear()
        blogo()
        print("\nBlock: " + responseC)
        print("\nDecoded: " + a)
        input("\a\nContinue...")
    except:
        pass

def miscellaneousLOCAL():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Ascii ₿
    \u001b[38;5;202mB.\033[0;37;40m System
    \u001b[38;5;202mC.\033[0;37;40m Dates
    \u001b[38;5;202mD.\033[0;37;40m Quotes
    \u001b[38;5;202mP.\033[0;37;40m PGP
    \u001b[38;5;202mS.\033[0;37;40m Satoshi Nakamoto
    \u001b[38;5;202mZ.\033[0;37;40m Bitcoin Strings
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, b, version, checkupdate()))
    miscellaneousLOCALmenu(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def slushpoolREMOTEOnchainONLY():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Difficulty
    \u001b[38;5;202mB.\033[0;37;40m Hash Rate
    \u001b[38;5;202mC.\033[0;37;40m Pool
    \u001b[38;5;202mD.\033[0;37;40m History
    \u001b[38;5;202mE.\033[0;37;40m Miner
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,b, version, checkupdate()))
    slushpoolLOCALOnchainONLYMenu(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def slushpoolLOCALOnchainONLY():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Difficulty
    \u001b[38;5;202mB.\033[0;37;40m Hash Rate
    \u001b[38;5;202mC.\033[0;37;40m Pool
    \u001b[38;5;202mD.\033[0;37;40m History
    \u001b[38;5;202mE.\033[0;37;40m Miner
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,b, version, checkupdate()))
    slushpoolLOCALOnchainONLYMenu(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def runTheNumbersMenu():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Countdown Block
    \033[1;32;40mB.\033[0;37;40m Countdown Halving
    \033[1;32;40mC.\033[0;37;40m Audit
    \033[1;32;40mD.\033[0;37;40m Templates & Blocks
    \033[1;32;40mE.\033[0;37;40m Missing Transactions
    \033[1;32;40mU.\033[0;37;40m Bitcoin Unspendable
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, b, version, checkupdate()))
    runTheNumbersControl(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def runTheNumbersMenuConn():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Countdown Block
    \033[1;32;40mB.\033[0;37;40m Countdown Halving
    \033[1;32;40mC.\033[0;37;40m Audit
    \033[1;32;40mD.\033[0;37;40m Templates & Blocks
    \033[1;32;40mE.\033[0;37;40m Missing Transactions
    \033[1;32;40mU.\033[0;37;40m Bitcoin Unspendable
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,b, version, checkupdate()))
    runTheNumbersControlConn(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def weatherMenuOnchainONLY():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Version 1
    \033[1;32;40mB.\033[0;37;40m Version 2
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,b, version, checkupdate()))
    menuWeatherOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def weatherMenu():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Version 1
    \033[1;32;40mB.\033[0;37;40m Version 2
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, b, version, checkupdate()))
    menuWeather(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def dnt(): # Donation selection menu
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;15mA.\033[0;37;40m Developers Donation
    \u001b[38;5;15mB.\033[0;37;40m Testers Donation
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, b, version, checkupdate()))
    menuC(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def dntOnchainONLY(): # Donation selection menu
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;15mA.\033[0;37;40m Developers Donation
    \u001b[38;5;15mB.\033[0;37;40m Testers Donation
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, b, version, checkupdate()))
    menuCOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))


def dntDev(): # Dev Donation Menu
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Samourai PayNym
    \u001b[38;5;202mB.\033[0;37;40m Bitcoin Address
    \u001b[33;1mC.\033[0;37;40m Lightning Network
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, b, version, checkupdate()))
    menuE(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def dntDevOnchainONLY(): # Dev Donation Menu
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Samourai PayNym
    \u001b[38;5;202mB.\033[0;37;40m Bitcoin Address
    \u001b[33;1mC.\033[0;37;40m Lightning Network
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,b, version, checkupdate()))
    menuEOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def dntTst(): # Tester Donation Menu
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Bitcoin Address
    \u001b[33;1mB.\033[0;37;40m Lightning Network
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,b, version, checkupdate()))
    menuF(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def dntTstOnchainONLY(): # Tester Donation Menu
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Bitcoin Address
    \u001b[33;1mB.\033[0;37;40m Lightning Network
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, b, version, checkupdate()))
    menuFOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))


def satnodeMenu(): # Satnode Menu
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Start SatNode
    \033[1;32;40mB.\033[0;37;40m Feed
    \033[1;32;40mC.\033[0;37;40m Setup
    \033[1;34;40mS.\033[0;37;40m Send a Message to Space
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, b, version, checkupdate()))
    menuD(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def satnodeMenuOnchainONLY(): # Satnode Menu
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Start SatNode
    \033[1;32;40mB.\033[0;37;40m Feed
    \033[1;32;40mC.\033[0;37;40m Setup
    \033[1;34;40mS.\033[0;37;40m Send a Message to Space
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, b, version, checkupdate()))
    menuD(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def rateSX():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Rate
    \033[1;32;40mB.\033[0;37;40m Chart
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, b, version, checkupdate()))
    rateSXMenu(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def rateSXOncainONLY():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Rate
    \033[1;32;40mB.\033[0;37;40m Chart
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, b, version, checkupdate()))
    rateSXMenuOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def mempoolmenu():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Blocks
    \033[1;32;40mB.\033[0;37;40m Recommended Fee
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,b, version, checkupdate()))
    mempoolmenuS(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def mempoolmenuOnchainONLY():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Blocks
    \033[1;32;40mB.\033[0;37;40m Recommended Fee
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,b, version, checkupdate()))
    mempoolmenuSOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))


def APILnbit():
    bitLN = {"NN":"","pd":""}
    if os.path.isfile('lnbitSN.conf'): # Check if the file 'bclock.conf' is in the same folder
        bitData= pickle.load(open("lnbitSN.conf", "rb")) # Load the file 'bclock.conf'
        bitLN = bitData # Copy the variable pathv to 'path'
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[0;37;40mLNBits SN:{} \033[1;34;40mPremium\033[0;37;40m

    \033[1;32;40mA.\033[0;37;40m New Invoice
    \033[1;32;40mB.\033[0;37;40m Pay Invoice
    \033[1;32;40mC.\033[0;37;40m New PayWall
    \033[1;32;40mD.\033[0;37;40m Delete PayWall
    \033[1;32;40mE.\033[0;37;40m List PayWalls
    \033[1;32;40mF.\033[0;37;40m Create LNURL
    \033[1;32;40mG.\033[0;37;40m List LNURL
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,b, version, bitLN['NN'], checkupdate()))
    menuLNBPI(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def APILnbitOnchainONLY():
    bitLN = {"NN":"","pd":""}
    if os.path.isfile('lnbitSN.conf'): # Check if the file 'bclock.conf' is in the same folder
        bitData= pickle.load(open("lnbitSN.conf", "rb")) # Load the file 'bclock.conf'
        bitLN = bitData # Copy the variable pathv to 'path'
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[0;37;40mLNBits SN:{} \033[1;34;40mPremium\033[0;37;40m

    \033[1;32;40mA.\033[0;37;40m New Invoice
    \033[1;32;40mB.\033[0;37;40m Pay Invoice
    \033[1;32;40mC.\033[0;37;40m New PayWall
    \033[1;32;40mD.\033[0;37;40m Delete PayWall
    \033[1;32;40mE.\033[0;37;40m List PayWalls
    \033[1;32;40mF.\033[0;37;40m Create LNURL
    \033[1;32;40mG.\033[0;37;40m List LNURL
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, b, version, bitLN['NN'], checkupdate()))
    menuLNBPIOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def APILnPay():
    bitLN = {"NN":"","pd":""}
    if os.path.isfile('lnpaySN.conf'): # Check if the file 'bclock.conf' is in the same folder
        bitData= pickle.load(open("lnpaySN.conf", "rb")) # Load the file 'bclock.conf'
        bitLN = bitData # Copy the variable pathv to 'path'
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[0;37;40mLNPay SN:{} \033[1;34;40mPremium\033[0;37;40m

    \033[1;32;40mA.\033[0;37;40m New Invoice
    \033[1;32;40mB.\033[0;37;40m Pay Invoice
    \033[1;32;40mC.\033[0;37;40m Wallet Balance
    \033[1;32;40mD.\033[0;37;40m List Invoices
    \033[1;32;40mE.\033[0;37;40m Transfer Between Wallets
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,b, version, bitLN['NN'], checkupdate()))
    menuLNPAY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def APILnPayOnchainONLY():
    bitLN = {"NN":"","pd":""}
    if os.path.isfile('lnpaySN.conf'): # Check if the file 'bclock.conf' is in the same folder
        bitData= pickle.load(open("lnpaySN.conf", "rb")) # Load the file 'bclock.conf'
        bitLN = bitData # Copy the variable pathv to 'path'
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[0;37;40mLNPay SN:{} \033[1;34;40mPremium\033[0;37;40m

    \033[1;32;40mA.\033[0;37;40m New Invoice
    \033[1;32;40mB.\033[0;37;40m Pay Invoice
    \033[1;32;40mC.\033[0;37;40m Wallet Balance
    \033[1;32;40mD.\033[0;37;40m List Invoices
    \033[1;32;40mE.\033[0;37;40m Transfer Between Wallets
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,b, version, bitLN['NN'], checkupdate()))
    menuLNPAYOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def APIOpenNode():
    bitLN = {"NN":"","pd":""}
    if os.path.isfile('opennodeSN.conf'): # Check if the file 'bclock.conf' is in the same folder
        bitData= pickle.load(open("opennodeSN.conf", "rb")) # Load the file 'bclock.conf'
        bitLN = bitData # Copy the variable pathv to 'path'
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[0;37;40mOpenNode SN:{} \033[1;34;40mPremium\033[0;37;40m

    \033[1;32;40mA.\033[0;37;40m New Invoice
    \033[1;32;40mB.\033[0;37;40m Pay Invoice
    \033[1;32;40mC.\033[0;37;40m Wallet Balance
    \033[1;32;40mD.\033[0;37;40m List Payments
    \033[1;32;40mS.\033[0;37;40m Status
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,b, version, bitLN['NN'], checkupdate()))
    menuOpenNode(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def APIOpenNodeOnchainONLY():
    bitLN = {"NN":"","pd":""}
    if os.path.isfile('opennodeSN.conf'): # Check if the file 'bclock.conf' is in the same folder
        bitData= pickle.load(open("opennodeSN.conf", "rb")) # Load the file 'bclock.conf'
        bitLN = bitData # Copy the variable pathv to 'path'
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[0;37;40mOpenNode SN:{} \033[1;34;40mPremium\033[0;37;40m

    \033[1;32;40mA.\033[0;37;40m New Invoice
    \033[1;32;40mB.\033[0;37;40m Pay Invoice
    \033[1;32;40mC.\033[0;37;40m Wallet Balance
    \033[1;32;40mD.\033[0;37;40m List Payments
    \033[1;32;40mS.\033[0;37;40m Status
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,b, version, bitLN['NN'], checkupdate()))
    menuOpenNodeOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def APITippinMe():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[0;37;40mTippinMe

    \033[1;32;40mA.\033[0;37;40m New Invoice
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,b, version, checkupdate()))
    menuTippinMe(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def APITippinMeOnchainONLY():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[0;37;40mTippinMe

    \033[1;32;40mA.\033[0;37;40m New Invoice
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,b, version, checkupdate()))
    menuTippinMeOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def APITallyCo():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[0;37;40mTallyCoin

    \033[1;32;40mA.\033[0;37;40m Get Payment
    \033[1;32;40mB.\033[0;37;40m Tip User
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,b, version, checkupdate()))
    menuTallyCo(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def APITallyCoOnchainONLY():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[0;37;40mTallyCoin

    \033[1;32;40mA.\033[0;37;40m Get Payment
    \033[1;32;40mB.\033[0;37;40m Tip User
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,b, version, checkupdate()))
    menuTallyCoOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))
#-------------------------------- SETTINGS -----------------------------------------------


def settings4Local():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;27mA.\033[0;37;40m Change Logo Design
    \u001b[38;5;27mB.\033[0;37;40m Change Logo Colors
    \u001b[38;5;27mC.\033[0;37;40m Change Clock Colors
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,b, version, checkupdate()))
    menuSettingsLocal(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def designQ():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Block
    \033[1;31;40mB.\033[0;37;40m Slick
    \033[1;31;40mC.\033[0;37;40m Tiny
    \033[1;31;40mD.\033[0;37;40m Grid
    \033[1;31;40mE.\033[0;37;40m Pallet
    \033[1;31;40mF.\033[0;37;40m Shade
    \033[1;31;40mG.\033[0;37;40m Chrome
    \033[1;31;40mH.\033[0;37;40m Simple
    \033[1;31;40mI.\033[0;37;40m Simple Block
    \033[1;31;40mJ.\033[0;37;40m 3D
    \033[1;31;40mK.\033[0;37;40m Simple 3D
    \033[1;31;40mL.\033[0;37;40m Huge
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,b, version, checkupdate()))
    menuDesign(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def designC():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Block
    \033[1;31;40mB.\033[0;37;40m Slick
    \033[1;31;40mC.\033[0;37;40m Tiny
    \033[1;31;40mD.\033[0;37;40m Grid
    \033[1;31;40mE.\033[0;37;40m Pallet
    \033[1;31;40mF.\033[0;37;40m Shade
    \033[1;31;40mG.\033[0;37;40m Chrome
    \033[1;31;40mH.\033[0;37;40m Simple
    \033[1;31;40mI.\033[0;37;40m Simple Block
    \033[1;31;40mJ.\033[0;37;40m 3D
    \033[1;31;40mK.\033[0;37;40m Simple 3D
    \033[1;31;40mL.\033[0;37;40m Huge
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,b, version, checkupdate()))
    menuDesignClock(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colors():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Front Color
    \033[1;31;40mB.\033[0;37;40m Back Color
    \033[1;31;40mC.\033[0;37;40m Rainbow
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,b, version, checkupdate()))
    menuColors(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colorsC():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Front Color
    \033[1;31;40mB.\033[0;37;40m Back Color
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,b, version, checkupdate()))
    menuColorsClock(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colorsSelectFront():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Black
    \033[1;31;40mB.\033[0;37;40m Red
    \033[1;31;40mC.\033[0;37;40m Green
    \033[1;31;40mD.\033[0;37;40m Yellow
    \033[1;31;40mE.\033[0;37;40m Blue
    \033[1;31;40mF.\033[0;37;40m Magenta
    \033[1;31;40mG.\033[0;37;40m Cyan
    \033[1;31;40mH.\033[0;37;40m White
    \033[1;31;40mI.\033[0;37;40m Gray
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,b, version, checkupdate()))
    menuColorsSelectFront(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colorsSelectFrontClock():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Black
    \033[1;31;40mB.\033[0;37;40m Red
    \033[1;31;40mC.\033[0;37;40m Green
    \033[1;31;40mD.\033[0;37;40m Yellow
    \033[1;31;40mE.\033[0;37;40m Blue
    \033[1;31;40mF.\033[0;37;40m Magenta
    \033[1;31;40mG.\033[0;37;40m Cyan
    \033[1;31;40mH.\033[0;37;40m White
    \033[1;31;40mI.\033[0;37;40m Gray
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,b, version, checkupdate()))
    menuColorsSelectFrontClock(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colorsSelectBack():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Black
    \033[1;31;40mB.\033[0;37;40m Red
    \033[1;31;40mC.\033[0;37;40m Green
    \033[1;31;40mD.\033[0;37;40m Yellow
    \033[1;31;40mE.\033[0;37;40m Blue
    \033[1;31;40mF.\033[0;37;40m Magenta
    \033[1;31;40mG.\033[0;37;40m Cyan
    \033[1;31;40mH.\033[0;37;40m White
    \033[1;31;40mI.\033[0;37;40m Gray
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,b, version, checkupdate()))
    menuColorsSelectBack(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colorsSelectBackClock():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Black
    \033[1;31;40mB.\033[0;37;40m Red
    \033[1;31;40mC.\033[0;37;40m Green
    \033[1;31;40mD.\033[0;37;40m Yellow
    \033[1;31;40mE.\033[0;37;40m Blue
    \033[1;31;40mF.\033[0;37;40m Magenta
    \033[1;31;40mG.\033[0;37;40m Cyan
    \033[1;31;40mH.\033[0;37;40m White
    \033[1;31;40mI.\033[0;37;40m Gray
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n ,b, version, checkupdate()))
    menuColorsSelectBackClock(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colorsSelectRainbow():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Start Color
    \033[1;31;40mB.\033[0;37;40m End Color
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,b, version, checkupdate()))
    menuColorsSelectRainbow(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colorsSelectRainbowStart():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)

    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Black
    \033[1;31;40mB.\033[0;37;40m Red
    \033[1;31;40mC.\033[0;37;40m Green
    \033[1;31;40mD.\033[0;37;40m Yellow
    \033[1;31;40mE.\033[0;37;40m Blue
    \033[1;31;40mF.\033[0;37;40m Magenta
    \033[1;31;40mG.\033[0;37;40m Cyan
    \033[1;31;40mH.\033[0;37;40m White
    \033[1;31;40mI.\033[0;37;40m Gray
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,b, version, checkupdate()))
    menuColorsSelectRainbowStart(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colorsSelectRainbowEnd():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Black
    \033[1;31;40mB.\033[0;37;40m Red
    \033[1;31;40mC.\033[0;37;40m Green
    \033[1;31;40mD.\033[0;37;40m Yellow
    \033[1;31;40mE.\033[0;37;40m Blue
    \033[1;31;40mF.\033[0;37;40m Magenta
    \033[1;31;40mG.\033[0;37;40m Cyan
    \033[1;31;40mH.\033[0;37;40m White
    \033[1;31;40mI.\033[0;37;40m Gray
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,b, version, checkupdate()))
    menuColorsSelectRainbowEnd(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def nostrConn():
    clear()
    blogo()
    sysinfo()
    n = "CROPPED"
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    nn = r.text
    di = json.loads(nn)
    a = di
    b = str(a)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Linux
    \033[1;32;40mB.\033[0;37;40m Windows
    \033[1;32;40mC.\033[0;37;40m Mac
    \033[1;32;40mS.\033[0;37;40m Bip39
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,b, version, checkupdate()))
    nostrmenu(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def menuSelection():
    chln = {"fullbtclnd":"","fullbtc":"","cropped":""}
    if os.path.isfile('config/intro.conf'):
        chain = pickle.load(open("config/intro.conf", "rb"))
        chln = chain
        print(chln + "\n")
        if chln == "B":
            path = {"ip_port":"", "rpcuser":"", "rpcpass":"", "bitcoincli":""}
            pathv = pickle.load(open("config/bclock.conf", "rb")) # Load the file 'bclock.conf'
            path = pathv # Copy the variable pathv to 'path'
            MainMenuLOCALChainONLY()
        elif chln == "A":
            path = {"ip_port":"", "rpcuser":"", "rpcpass":"", "bitcoincli":""}
            pathv = pickle.load(open("config/bclock.conf", "rb")) # Load the file 'bclock.conf'
            path = pathv # Copy the variable pathv to 'path'
            MainMenuLOCAL()
        elif chln == "C":
            MainMenuCROPPED()
    else:
        if os.path.isfile('config/blndconnect.conf'):
            chln['offchain'] = "offchain"
        else:
            chln['onchain'] = "onchain"

        pickle.dump(chln, open("config/selection.conf", "wb"))


def menuSelectionLN():
    lndconnectload = {"ip_port":"", "tls":"", "macaroon":"", "lncli":""}
    lndconnectData = pickle.load(open("config/blndconnect.conf", "rb")) # Load the file 'bclock.conf'
    lndconnectload = lndconnectData # Copy the variable pathv to 'path'
    if lndconnectload['ln']:
        menuLNDLOCAL()
    else:
        menuLND()

def aaccPPiLNBits():
    try:
        bitLN = {"NN":"","pd":""}
        if os.path.isfile('config/lnbitSN.conf'):
            bitData= pickle.load(open("config/lnbitSN.conf", "rb"))
            bitLN = bitData
            APILnbit()
        else:
            qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
            )
            bitLN['NN'] = randrange(10000000)
            curl = (
                'curl -X POST https://lnbits.com/api/v1/payments -d '
                + "'{"
                + f""""out": false, "amount": 1000, "memo": "LNBits on PyBLOCK {bitLN['NN']}" """
                + "}'"
                + """ -H "X-Api-Key: 1d646820055e4e2da218e801eaacfc94 " -H "Content-type: application/json" """
            )

            sh = os.popen(curl).read()
            clear()
            blogo()
            n = str(sh)
            d = json.loads(n)
            q = d['payment_request']
            c = q.lower()
            while True:
                print("\033[1;30;47m")
                qr.add_data(c)
                qr.print_ascii()
                print("\033[0;37;40m")
                qr.clear()
                print(f"Lightning Invoice: {c}")
                dn = str(d['checking_id'])
                t.sleep(10)
                checkcurl = (
                    f'curl -X GET https://lnbits.com/api/v1/payments/{dn}'
                    + """ -H "X-Api-Key: 1d646820055e4e2da218e801eaacfc94" -H "Content-type: application/json" """
                )

                rsh = os.popen(checkcurl).read()
                clear()
                blogo()
                nn = str(rsh)
                dd = json.loads(nn)
                db = dd['paid']
                if db is not True:
                    continue

                clear()
                blogo()
                tick()
                bitLN['pd'] = "PAID"
                pickle.dump(bitLN, open("config/lnbitSN.conf", "wb"))
                createFileConnLNBits()
                break
    except:
        clear()
        blogo()
        print("\n\tSERIAL NUMBER NOT FOUND\n")
        input("Continue...")

def aaccPPiLNPay():
    try:
        bitLN = {"NN":"","pd":""}
        if os.path.isfile('config/lnpaySN.conf'): # Check if the file 'bclock.conf' is in the same folder
            bitData= pickle.load(open("config/lnpaySN.conf", "rb")) # Load the file 'bclock.conf'
            bitLN = bitData # Copy the variable pathv to 'path'
            APILnPay()
        else:
            qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
            )
            bitLN['NN'] = randrange(10000000)
            curl = (
                'curl -X POST https://lnbits.com/api/v1/payments -d '
                + "'{"
                + f""""out": false, "amount": 1000, "memo": "LNPay on PyBLOCK {bitLN['NN']}" """
                + "}'"
                + """ -H "X-Api-Key: 1d646820055e4e2da218e801eaacfc94 " -H "Content-type: application/json" """
            )

            sh = os.popen(curl).read()
            clear()
            blogo()
            n = str(sh)
            d = json.loads(n)
            q = d['payment_request']
            c = q.lower()
            while True:
                print("\033[1;30;47m")
                qr.add_data(c)
                qr.print_ascii()
                print("\033[0;37;40m")
                qr.clear()
                print(f"Lightning Invoice: {c}")
                dn = str(d['checking_id'])
                t.sleep(10)
                checkcurl = (
                    f'curl -X GET https://lnbits.com/api/v1/payments/{dn}'
                    + """ -H "X-Api-Key: 1d646820055e4e2da218e801eaacfc94" -H "Content-type: application/json" """
                )

                rsh = os.popen(checkcurl).read()
                clear()
                blogo()
                nn = str(rsh)
                dd = json.loads(nn)
                db = dd['paid']
                if db is not True:
                    continue

                clear()
                blogo()
                tick()
                bitLN['pd'] = "PAID"
                pickle.dump(bitLN, open("config/lnpaySN.conf", "wb"))
                createFileConnLNPay()
                break

    except:
        clear()
        blogo()
        print("\n\tSERIAL NUMBER NOT FOUND\n")
        input("Continue...")

def aaccPPiOpenNode():
    try:
        bitLN = {"NN":"","pd":""}
        if os.path.isfile('config/opennodeSN.conf'): # Check if the file 'bclock.conf' is in the same folder
            bitData= pickle.load(open("config/opennodeSN.conf", "rb")) # Load the file 'bclock.conf'
            bitLN = bitData # Copy the variable pathv to 'path'
            APIOpenNode()
        else:
            qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
            )
            bitLN['NN'] = randrange(10000000)
            curl = (
                'curl -X POST https://lnbits.com/api/v1/payments -d '
                + "'{"
                + f""""out": false, "amount": 1000, "memo": "OpenNode on PyBLOCK {bitLN['NN']}" """
                + "}'"
                + """ -H "X-Api-Key: 1d646820055e4e2da218e801eaacfc94 " -H "Content-type: application/json" """
            )

            sh = os.popen(curl).read()
            clear()
            blogo()
            n = str(sh)
            d = json.loads(n)
            q = d['payment_request']
            c = q.lower()
            while True:
                print("\033[1;30;47m")
                qr.add_data(c)
                qr.print_ascii()
                print("\033[0;37;40m")
                qr.clear()
                print(f"Lightning Invoice: {c}")
                dn = str(d['checking_id'])
                t.sleep(10)
                checkcurl = (
                    f'curl -X GET https://lnbits.com/api/v1/payments/{dn}'
                    + """ -H "X-Api-Key: 1d646820055e4e2da218e801eaacfc94" -H "Content-type: application/json" """
                )

                rsh = os.popen(checkcurl).read()
                clear()
                blogo()
                nn = str(rsh)
                dd = json.loads(nn)
                db = dd['paid']
                if db is not True:
                    continue

                clear()
                blogo()
                tick()
                bitLN['pd'] = "PAID"
                pickle.dump(bitLN, open("config/opennodeSN.conf", "wb"))
                createFileConnOpenNode()
                break

    except:
        clear()
        blogo()
        print("\n\tSERIAL NUMBER NOT FOUND\n")
        input("Continue...")


def aaccPPiTippinMe():
    if os.path.isfile('config/tippinme.conf'): # Check if the file 'bclock.conf' is in the same folder
        APITippinMe()
    else:
        createFileTippinMe()

def aaccPPiTallyCo():
    if os.path.isfile('config/tallyco.conf'): # Check if the file 'bclock.conf' is in the same folder
        APITallyCo()
    else:
        createFileConnTallyCo()

def checkupdate():
    r = requests.get('https://raw.githubusercontent.com/curly60e/pyblock/master/ver.txt')
    r.headers['Content-Type']
    n = r.text
    di = json.loads(n)
    if di['version'] == version:
        q = print(" ")
    else:
        print("\n    ------------------------------------------")
        q = print("    \033[1;31;40mNew version available\033[0;37;40m > Exit and $pip3 install pybitblock -U ")
        print("    ------------------------------------------")

def testlogo():
    output = render('PyBLOCK', colors=[settings['colorA'], settings['colorB']], align='left', font=settings['design'])
    print(output)
    print("""

    -------------------------
        Design:      {}
        Front Color: {}
        Back Color:  {}
    -------------------------

    """.format(settings['design'], settings['colorA'], settings['colorB']))
    try:
        print("<<< Cancel Control + C")
        input("Enter To Apply...")
        settings["gradient"] = "color"
        pickle.dump(settings, open("config/pyblocksettings.conf", "wb"))
    except:
        pass

def testlogoRB():
    output = render('PyBLOCK', gradient=[settings['colorA'], settings['colorB']], align='left', font=settings['design'])
    print(output)
    print("""

    -------------------------
        Design:      {}
        Start Color: {}
        End Color:   {}
    -------------------------

    """.format(settings['design'], settings['colorA'], settings['colorB']))
    try:
        print("<<< Cancel Control + C")
        input("Enter To Apply...")
        settings["gradient"] = "grd"
        pickle.dump(settings, open("config/pyblocksettings.conf", "wb"))
    except:
        pass

def testClock():
    bitcoinclient = path['bitcoincli'] + " getblockcount"
    block = os.popen(str(bitcoinclient)).read() # 'getblockcount' convert to string
    b = block
    output = render(str(b), colors=[settingsClock['colorA'], settingsClock['colorB']], align='left')
    print(output)
    print("""

    -------------------------
        Front Color: {}
        Back Color:  {}
    -------------------------

    """.format(settingsClock['colorA'], settingsClock['colorB']))
    try:
        print("<<< Cancel Control + C")
        input("Enter To Apply...")
        settingsClock["gradient"] = "color"
        pickle.dump(settingsClock, open("config/pyblocksettingsClock.conf", "wb"))
    except:
        pass

#--------------------------------- End Menu section -----------------------------------
#--------------------------------- Main Menu execution --------------------------------

def menuSettingsLocal(menuSTT):
    if menuSTT in ["A", "a"]:
        clear()
        blogo()
        designQ()
    elif menuSTT in ["B", "b"]:
        clear()
        blogo()
        colors()
    elif menuSTT in ["C", "c"]:
        clear()
        blogo()
        colorsC()

def menuSettingsLocalOnchainONLY(menuSTT):
    if menuSTT in ["A", "a"]:
        clear()
        blogo()
        designQOnchainONLY()
    elif menuSTT in ["B", "b"]:
        clear()
        blogo()
        colorsOnchainONLY()
    elif menuSTT in ["C", "c"]:
        clear()
        blogo()
        colorsCOnchainONLY()

def menuSettingsRemote(menuSTT):
    if menuSTT in ["A", "a"]:
        clear()
        blogo()
        designQ()
    elif menuSTT in ["B", "b"]:
        clear()
        blogo()
        colors()
    elif menuSTT in ["C", "c"]:
        clear()
        blogo()
        colorsCRemote()

def menuColors(menuCLS):
    if menuCLS in ["A", "a"]:
        colorsSelectFront()
    elif menuCLS in ["B", "b"]:
        colorsSelectBack()
    elif menuCLS in ["C", "c"]:
        colorsSelectRainbow()
    elif menuCLS in ["F", "f"]:
        colors()

def menuColorsOnchainONLY(menuCLS):
    if menuCLS in ["A", "a"]:
        colorsSelectFrontOnchainONLY()
    elif menuCLS in ["B", "b"]:
        colorsSelectBackOnchainONLY()
    elif menuCLS in ["C", "c"]:
        colorsSelectRainbowOnchainONLY()
    elif menuCLS in ["F", "f"]:
        colorsOnchainONLY()

def menuColorsClock(menuCLS):
    if menuCLS in ["A", "a"]:
        colorsSelectFrontClock()
    elif menuCLS in ["B", "b"]:
        colorsSelectBackClock()
    elif menuCLS in ["F", "f"]:
        colors()

def menuColorsClockOnchainONLY(menuCLS):
    if menuCLS in ["A", "a"]:
        colorsSelectFrontClockOnchainONLY()
    elif menuCLS in ["B", "b"]:
        colorsSelectBackClockOnchainONLY()
    elif menuCLS in ["F", "f"]:
        colorsOnchainONLY()

def menuColorsClockRemote(menuCLS):
    if menuCLS in ["A", "a"]:
        colorsSelectFrontClockRemote()
    elif menuCLS in ["B", "b"]:
        colorsSelectBackClockRemote()
    elif menuCLS in ["F", "f"]:
        colors()

def menuColorsSelectRainbow(menuRF):
    if menuRF in ["A", "a"]:
        colorsSelectRainbowStart()
    elif menuRF in ["B", "b"]:
        colorsSelectRainbowEnd()
    elif menuRF in ["F", "f"]:
        colors()

def menuColorsSelectRainbowOnchainONLY(menuRF):
    if menuRF in ["A", "a"]:
        colorsSelectRainbowStartOnchaiONLY()
    elif menuRF in ["B", "b"]:
        colorsSelectRainbowEndOnchainONLY()
    elif menuRF in ["F", "f"]:
        colorsOnchainONLY()

def menuColorsSelectRainbowEnd(menuCF):
    if menuCF in ["A", "a"]:
        clear()
        blogo()
        settings["colorB"] = "black"
        testlogoRB()
    elif menuCF in ["B", "b"]:
        clear()
        blogo()
        settings["colorB"] = "red"
        testlogoRB()
    elif menuCF in ["C", "c"]:
        clear()
        blogo()
        settings["colorB"] = "green"
        testlogoRB()
    elif menuCF in ["D", "d"]:
        clear()
        blogo()
        settings["colorB"] = "yellow"
        testlogo()
    elif menuCF in ["E", "e"]:
        clear()
        blogo()
        settings["colorB"] = "blue"
        testlogoRB()
    elif menuCF in ["F", "f"]:
        clear()
        blogo()
        settings["colorB"] = "magenta"
        testlogoRB()
    elif menuCF in ["G", "g"]:
        clear()
        blogo()
        settings["colorB"] = "cyan"
        testlogoRB()
    elif menuCF in ["H", "h"]:
        clear()
        blogo()
        settings["colorB"] = "white"
        testlogoRB()
    elif menuCF in ["I", "i"]:
        clear()
        blogo()
        settings["colorB"] = "gray"
        testlogoRB()
    elif menuCF in ["R", "r"]:
        colors()

def menuColorsSelectRainbowEndOnchainONLY(menuCF):
    if menuCF in ["A", "a"]:
        clear()
        blogo()
        settings["colorB"] = "black"
        testlogoRB()
    elif menuCF in ["B", "b"]:
        clear()
        blogo()
        settings["colorB"] = "red"
        testlogoRB()
    elif menuCF in ["C", "c"]:
        clear()
        blogo()
        settings["colorB"] = "green"
        testlogoRB()
    elif menuCF in ["D", "d"]:
        clear()
        blogo()
        settings["colorB"] = "yellow"
        testlogo()
    elif menuCF in ["E", "e"]:
        clear()
        blogo()
        settings["colorB"] = "blue"
        testlogoRB()
    elif menuCF in ["F", "f"]:
        clear()
        blogo()
        settings["colorB"] = "magenta"
        testlogoRB()
    elif menuCF in ["G", "g"]:
        clear()
        blogo()
        settings["colorB"] = "cyan"
        testlogoRB()
    elif menuCF in ["H", "h"]:
        clear()
        blogo()
        settings["colorB"] = "white"
        testlogoRB()
    elif menuCF in ["I", "i"]:
        clear()
        blogo()
        settings["colorB"] = "gray"
        testlogoRB()
    elif menuCF in ["R", "r"]:
        colorsOnchainONLY()

def menuColorsSelectRainbowStart(menuCF):
    if menuCF in ["A", "a"]:
        clear()
        blogo()
        settings["colorA"] = "black"
        testlogoRB()
    elif menuCF in ["B", "b"]:
        clear()
        blogo()
        settings["colorA"] = "red"
        testlogoRB()
    elif menuCF in ["C", "c"]:
        clear()
        blogo()
        settings["colorA"] = "green"
        testlogoRB()
    elif menuCF in ["D", "d"]:
        clear()
        blogo()
        settings["colorA"] = "yellow"
        testlogoRB()
    elif menuCF in ["E", "e"]:
        clear()
        blogo()
        settings["colorA"] = "blue"
        testlogoRB()
    elif menuCF in ["F", "f"]:
        clear()
        blogo()
        settings["colorA"] = "magenta"
        testlogoRB()
    elif menuCF in ["G", "g"]:
        clear()
        blogo()
        settings["colorA"] = "cyan"
        testlogoRB()
    elif menuCF in ["H", "h"]:
        clear()
        blogo()
        settings["colorA"] = "white"
        testlogoRB()
    elif menuCF in ["I", "i"]:
        clear()
        blogo()
        settings["colorA"] = "gray"
        testlogoRB()
    elif menuCF in ["R", "r"]:
        colors()

def menuColorsSelectRainbowStartOnchainONLY(menuCF):
    if menuCF in ["A", "a"]:
        clear()
        blogo()
        settings["colorA"] = "black"
        testlogoRB()
    elif menuCF in ["B", "b"]:
        clear()
        blogo()
        settings["colorA"] = "red"
        testlogoRB()
    elif menuCF in ["C", "c"]:
        clear()
        blogo()
        settings["colorA"] = "green"
        testlogoRB()
    elif menuCF in ["D", "d"]:
        clear()
        blogo()
        settings["colorA"] = "yellow"
        testlogoRB()
    elif menuCF in ["E", "e"]:
        clear()
        blogo()
        settings["colorA"] = "blue"
        testlogoRB()
    elif menuCF in ["F", "f"]:
        clear()
        blogo()
        settings["colorA"] = "magenta"
        testlogoRB()
    elif menuCF in ["G", "g"]:
        clear()
        blogo()
        settings["colorA"] = "cyan"
        testlogoRB()
    elif menuCF in ["H", "h"]:
        clear()
        blogo()
        settings["colorA"] = "white"
        testlogoRB()
    elif menuCF in ["I", "i"]:
        clear()
        blogo()
        settings["colorA"] = "gray"
        testlogoRB()
    elif menuCF in ["R", "r"]:
        colorsOnchainONLY()

def menuColorsSelectBack(menuCF):
    if menuCF in ["A", "a"]:
        clear()
        blogo()
        settings["colorB"] = "black"
        testlogo()
    elif menuCF in ["B", "b"]:
        clear()
        blogo()
        settings["colorB"] = "red"
        testlogo()
    elif menuCF in ["C", "c"]:
        clear()
        blogo()
        settings["colorB"] = "green"
        testlogo()
    elif menuCF in ["D", "d"]:
        clear()
        blogo()
        settings["colorB"] = "yellow"
        testlogo()
    elif menuCF in ["E", "e"]:
        clear()
        blogo()
        settings["colorB"] = "blue"
        testlogo()
    elif menuCF in ["F", "f"]:
        clear()
        blogo()
        settings["colorB"] = "magenta"
        testlogo()
    elif menuCF in ["G", "g"]:
        clear()
        blogo()
        settings["colorB"] = "cyan"
        testlogo()
    elif menuCF in ["H", "h"]:
        clear()
        blogo()
        settings["colorB"] = "white"
        testlogo()
    elif menuCF in ["I", "i"]:
        clear()
        blogo()
        settings["colorB"] = "gray"
        testlogo()
    elif menuCF in ["R", "r"]:
        colors()

def menuColorsSelectBackOnchainONLY(menuCF):
    if menuCF in ["A", "a"]:
        clear()
        blogo()
        settings["colorB"] = "black"
        testlogo()
    elif menuCF in ["B", "b"]:
        clear()
        blogo()
        settings["colorB"] = "red"
        testlogo()
    elif menuCF in ["C", "c"]:
        clear()
        blogo()
        settings["colorB"] = "green"
        testlogo()
    elif menuCF in ["D", "d"]:
        clear()
        blogo()
        settings["colorB"] = "yellow"
        testlogo()
    elif menuCF in ["E", "e"]:
        clear()
        blogo()
        settings["colorB"] = "blue"
        testlogo()
    elif menuCF in ["F", "f"]:
        clear()
        blogo()
        settings["colorB"] = "magenta"
        testlogo()
    elif menuCF in ["G", "g"]:
        clear()
        blogo()
        settings["colorB"] = "cyan"
        testlogo()
    elif menuCF in ["H", "h"]:
        clear()
        blogo()
        settings["colorB"] = "white"
        testlogo()
    elif menuCF in ["I", "i"]:
        clear()
        blogo()
        settings["colorB"] = "gray"
        testlogo()
    elif menuCF in ["R", "r"]:
        colorsOnchainONLY()

def menuColorsSelectFront(menuCF):
    if menuCF in ["A", "a"]:
        clear()
        blogo()
        settings["colorA"] = "black"
        testlogo()
    elif menuCF in ["B", "b"]:
        clear()
        blogo()
        settings["colorA"] = "red"
        testlogo()
    elif menuCF in ["C", "c"]:
        clear()
        blogo()
        settings["colorA"] = "green"
        testlogo()
    elif menuCF in ["D", "d"]:
        clear()
        blogo()
        settings["colorA"] = "yellow"
        testlogo()
    elif menuCF in ["E", "e"]:
        clear()
        blogo()
        settings["colorA"] = "blue"
        testlogo()
    elif menuCF in ["F", "f"]:
        clear()
        blogo()
        settings["colorA"] = "magenta"
        testlogo()
    elif menuCF in ["G", "g"]:
        clear()
        blogo()
        settings["colorA"] = "cyan"
        testlogo()
    elif menuCF in ["H", "h"]:
        clear()
        blogo()
        settings["colorA"] = "white"
        testlogo()
    elif menuCF in ["I", "i"]:
        clear()
        blogo()
        settings["colorA"] = "gray"
        testlogo()
    elif menuCF in ["R", "r"]:
        colors()

def menuColorsSelectFrontOncainONLY(menuCF):
    if menuCF in ["A", "a"]:
        clear()
        blogo()
        settings["colorA"] = "black"
        testlogo()
    elif menuCF in ["B", "b"]:
        clear()
        blogo()
        settings["colorA"] = "red"
        testlogo()
    elif menuCF in ["C", "c"]:
        clear()
        blogo()
        settings["colorA"] = "green"
        testlogo()
    elif menuCF in ["D", "d"]:
        clear()
        blogo()
        settings["colorA"] = "yellow"
        testlogo()
    elif menuCF in ["E", "e"]:
        clear()
        blogo()
        settings["colorA"] = "blue"
        testlogo()
    elif menuCF in ["F", "f"]:
        clear()
        blogo()
        settings["colorA"] = "magenta"
        testlogo()
    elif menuCF in ["G", "g"]:
        clear()
        blogo()
        settings["colorA"] = "cyan"
        testlogo()
    elif menuCF in ["H", "h"]:
        clear()
        blogo()
        settings["colorA"] = "white"
        testlogo()
    elif menuCF in ["I", "i"]:
        clear()
        blogo()
        settings["colorA"] = "gray"
        testlogo()
    elif menuCF in ["R", "r"]:
        colorsOnchainONLY()

def menuColorsSelectFrontClock(menuCF):
    if menuCF in ["A", "a"]:
        clear()
        blogo()
        settingsClock["colorA"] = "black"
        testClock()
    elif menuCF in ["B", "b"]:
        clear()
        blogo()
        settingsClock["colorA"] = "red"
        testClock()
    elif menuCF in ["C", "c"]:
        clear()
        blogo()
        settingsClock["colorA"] = "green"
        testClock()
    elif menuCF in ["D", "d"]:
        clear()
        blogo()
        settingsClock["colorA"] = "yellow"
        testClock()
    elif menuCF in ["E", "e"]:
        clear()
        blogo()
        settingsClock["colorA"] = "blue"
        testClock()
    elif menuCF in ["F", "f"]:
        clear()
        blogo()
        settingsClock["colorA"] = "magenta"
        testClock()
    elif menuCF in ["G", "g"]:
        clear()
        blogo()
        settingsClock["colorA"] = "cyan"
        testClock()
    elif menuCF in ["H", "h"]:
        clear()
        blogo()
        settingsClock["colorA"] = "white"
        testClock()
    elif menuCF in ["I", "i"]:
        clear()
        blogo()
        settingsClock["colorA"] = "gray"
        testClock()
    elif menuCF in ["R", "r"]:
        colors()

def menuColorsSelectFrontClockOnchainONLY(menuCF):
    if menuCF in ["A", "a"]:
        clear()
        blogo()
        settingsClock["colorA"] = "black"
        testClock()
    elif menuCF in ["B", "b"]:
        clear()
        blogo()
        settingsClock["colorA"] = "red"
        testClock()
    elif menuCF in ["C", "c"]:
        clear()
        blogo()
        settingsClock["colorA"] = "green"
        testClock()
    elif menuCF in ["D", "d"]:
        clear()
        blogo()
        settingsClock["colorA"] = "yellow"
        testClock()
    elif menuCF in ["E", "e"]:
        clear()
        blogo()
        settingsClock["colorA"] = "blue"
        testClock()
    elif menuCF in ["F", "f"]:
        clear()
        blogo()
        settingsClock["colorA"] = "magenta"
        testClock()
    elif menuCF in ["G", "g"]:
        clear()
        blogo()
        settingsClock["colorA"] = "cyan"
        testClock()
    elif menuCF in ["H", "h"]:
        clear()
        blogo()
        settingsClock["colorA"] = "white"
        testClock()
    elif menuCF in ["I", "i"]:
        clear()
        blogo()
        settingsClock["colorA"] = "gray"
        testClock()
    elif menuCF in ["R", "r"]:
        colorsOnchainONLY()

def menuColorsSelectBackClock(menuCF):
    if menuCF in ["A", "a"]:
        clear()
        blogo()
        settingsClock["colorB"] = "black"
        testClock()
    elif menuCF in ["B", "b"]:
        clear()
        blogo()
        settingsClock["colorB"] = "red"
        testClock()
    elif menuCF in ["C", "c"]:
        clear()
        blogo()
        settingsClock["colorB"] = "green"
        testClock()
    elif menuCF in ["D", "d"]:
        clear()
        blogo()
        settingsClock["colorB"] = "yellow"
        testClock()
    elif menuCF in ["E", "e"]:
        clear()
        blogo()
        settingsClock["colorB"] = "blue"
        testClock()
    elif menuCF in ["F", "f"]:
        clear()
        blogo()
        settingsClock["colorB"] = "magenta"
        testClock()
    elif menuCF in ["G", "g"]:
        clear()
        blogo()
        settingsClock["colorB"] = "cyan"
        testClock()
    elif menuCF in ["H", "h"]:
        clear()
        blogo()
        settingsClock["colorB"] = "white"
        testClock()
    elif menuCF in ["I", "i"]:
        clear()
        blogo()
        settingsClock["colorB"] = "gray"
        testClock()
    elif menuCF in ["R", "r"]:
        colors()

def menuColorsSelectBackClockOnchainONLY(menuCF):
    if menuCF in ["A", "a"]:
        clear()
        blogo()
        settingsClock["colorB"] = "black"
        testClock()
    elif menuCF in ["B", "b"]:
        clear()
        blogo()
        settingsClock["colorB"] = "red"
        testClock()
    elif menuCF in ["C", "c"]:
        clear()
        blogo()
        settingsClock["colorB"] = "green"
        testClock()
    elif menuCF in ["D", "d"]:
        clear()
        blogo()
        settingsClock["colorB"] = "yellow"
        testClock()
    elif menuCF in ["E", "e"]:
        clear()
        blogo()
        settingsClock["colorB"] = "blue"
        testClock()
    elif menuCF in ["F", "f"]:
        clear()
        blogo()
        settingsClock["colorB"] = "magenta"
        testClock()
    elif menuCF in ["G", "g"]:
        clear()
        blogo()
        settingsClock["colorB"] = "cyan"
        testClock()
    elif menuCF in ["H", "h"]:
        clear()
        blogo()
        settingsClock["colorB"] = "white"
        testClock()
    elif menuCF in ["I", "i"]:
        clear()
        blogo()
        settingsClock["colorB"] = "gray"
        testClock()
    elif menuCF in ["R", "r"]:
        colorsOnchainONLY()

def menuColorsSelectFrontClockRemote(menuCF):
    if menuCF in ["A", "a"]:
        clear()
        blogo()
        settingsClock["colorA"] = "black"
        testClockRemote()
    elif menuCF in ["B", "b"]:
        clear()
        blogo()
        settingsClock["colorA"] = "red"
        testClockRemote()
    elif menuCF in ["C", "c"]:
        clear()
        blogo()
        settingsClock["colorA"] = "green"
        testClockRemote()
    elif menuCF in ["D", "d"]:
        clear()
        blogo()
        settingsClock["colorA"] = "yellow"
        testClockRemote()
    elif menuCF in ["E", "e"]:
        clear()
        blogo()
        settingsClock["colorA"] = "blue"
        testClockRemote()
    elif menuCF in ["F", "f"]:
        clear()
        blogo()
        settingsClock["colorA"] = "magenta"
        testClockRemote()
    elif menuCF in ["G", "g"]:
        clear()
        blogo()
        settingsClock["colorA"] = "cyan"
        testClockRemote()
    elif menuCF in ["H", "h"]:
        clear()
        blogo()
        settingsClock["colorA"] = "white"
        testClockRemote()
    elif menuCF in ["I", "i"]:
        clear()
        blogo()
        settingsClock["colorA"] = "gray"
        testClockRemote()
    elif menuCF in ["R", "r"]:
        colors()

def menuColorsSelectBackClockRemote(menuCF):
    if menuCF in ["A", "a"]:
        clear()
        blogo()
        settingsClock["colorB"] = "black"
        testClockRemote()
    elif menuCF in ["B", "b"]:
        clear()
        blogo()
        settingsClock["colorB"] = "red"
        testClockRemote()
    elif menuCF in ["C", "c"]:
        clear()
        blogo()
        settingsClock["colorB"] = "green"
        testClockRemote()
    elif menuCF in ["D", "d"]:
        clear()
        blogo()
        settingsClock["colorB"] = "yellow"
        testClockRemote()
    elif menuCF in ["E", "e"]:
        clear()
        blogo()
        settingsClock["colorB"] = "blue"
        testClockRemote()
    elif menuCF in ["F", "f"]:
        clear()
        blogo()
        settingsClock["colorB"] = "magenta"
        testClockRemote()
    elif menuCF in ["G", "g"]:
        clear()
        blogo()
        settingsClock["colorB"] = "cyan"
        testClockRemote()
    elif menuCF in ["H", "h"]:
        clear()
        blogo()
        settingsClock["colorB"] = "white"
        testClockRemote()
    elif menuCF in ["I", "i"]:
        clear()
        blogo()
        settingsClock["colorB"] = "gray"
        testClockRemote()
    elif menuCF in ["R", "r"]:
        colors()

def menuDesign(menuDSN):
    if menuDSN in ["A", "a"]:
        clear()
        blogo()
        settings["design"] = "block"
        testlogo()
    elif menuDSN in ["B", "b"]:
        clear()
        blogo()
        settings['design'] = "slick"
        testlogo()
    elif menuDSN in ["C", "c"]:
        clear()
        blogo()
        settings['design'] = "tiny"
        testlogo()
    elif menuDSN in ["D", "d"]:
        clear()
        blogo()
        settings['design'] = "grid"
        testlogo()
    elif menuDSN in ["E", "e"]:
        clear()
        blogo()
        settings['design'] = "pallet"
        testlogo()
    elif menuDSN in ["F", "f"]:
        clear()
        blogo()
        settings['design'] = "shade"
        testlogo()
    elif menuDSN in ["G", "g"]:
        clear()
        blogo()
        settings['design'] = "chrome"
        testlogo()
    elif menuDSN in ["H", "h"]:
        clear()
        blogo()
        settings['design'] = "simple"
        testlogo()
    elif menuDSN in ["I", "i"]:
        clear()
        blogo()
        settings['design'] = "simpleBlock"
        testlogo()
    elif menuDSN in ["J", "j"]:
        clear()
        blogo()
        settings['design'] = "3d"
        testlogo()
    elif menuDSN in ["K", "k"]:
        clear()
        blogo()
        settings['design'] = "simple3d"
        testlogo()
    elif menuDSN in ["L", "l"]:
        clear()
        blogo()
        settings['design'] = "huge"
        testlogo()

def menuDesignOnchainONLY(menuDSN):
    if menuDSN in ["A", "a"]:
        clear()
        blogo()
        settings["design"] = "block"
        testlogo()
    elif menuDSN in ["B", "b"]:
        clear()
        blogo()
        settings['design'] = "slick"
        testlogo()
    elif menuDSN in ["C", "c"]:
        clear()
        blogo()
        settings['design'] = "tiny"
        testlogo()
    elif menuDSN in ["D", "d"]:
        clear()
        blogo()
        settings['design'] = "grid"
        testlogo()
    elif menuDSN in ["E", "e"]:
        clear()
        blogo()
        settings['design'] = "pallet"
        testlogo()
    elif menuDSN in ["F", "f"]:
        clear()
        blogo()
        settings['design'] = "shade"
        testlogo()
    elif menuDSN in ["G", "g"]:
        clear()
        blogo()
        settings['design'] = "chrome"
        testlogo()
    elif menuDSN in ["H", "h"]:
        clear()
        blogo()
        settings['design'] = "simple"
        testlogo()
    elif menuDSN in ["I", "i"]:
        clear()
        blogo()
        settings['design'] = "simpleBlock"
        testlogo()
    elif menuDSN in ["J", "j"]:
        clear()
        blogo()
        settings['design'] = "3d"
        testlogo()
    elif menuDSN in ["K", "k"]:
        clear()
        blogo()
        settings['design'] = "simple3d"
        testlogo()
    elif menuDSN in ["L", "l"]:
        clear()
        blogo()
        settings['design'] = "huge"
        testlogo()

#------------API---------------------

def mempoolmenuS(menuMem):
    if menuMem in ["A", "a"]:
        blocks()
    elif menuMem in ["B", "b"]:
        fee()
    elif menuMem in ["R", "r"]:
        menuSelection()

def mempoolmenuSOnchainONLY(menuMem):
    if menuMem in ["A", "a"]:
        blocks()
    elif menuMem in ["B", "b"]:
        fee()
    elif menuMem in ["R", "r"]:
        menuSelection()

def menuTallyCo(menuTLC):
    if menuTLC in ["A", "a"]:
        tallycoGetPayment()
    elif menuTLC in ["B", "b"]:
        tallycoDonateid()
    elif menuTLC in ["R", "r"]:
        menuSelection()

def menuTallyCoOnchainONLY(menuTLC):
    if menuTLC in ["A", "a"]:
        tallycoGetPayment()
    elif menuTLC in ["B", "b"]:
        tallycoDonateid()
    elif menuTLC in ["R", "r"]:
        menuSelection()

def menuTippinMe(menuTM):
    if menuTM in ["A", "a"]:
        tippinmeGetInvoice()
    elif menuTM in ["R", "r"]:
        menuSelection()

def menuTippinMeOnchainONLY(menuTM):
    if menuTM in ["A", "a"]:
        tippinmeGetInvoice()
    elif menuTM in ["R", "r"]:
        menuSelection()

def menuOpenNode(menuOP):
    if menuOP in ["A", "a"]:
        clear()
        blogo()
        OpenNodecreatecharge()
    elif menuOP in ["B", "b"]:
        clear()
        blogo()
        OpenNodeiniciatewithdrawal()
    elif menuOP in ["C", "c"]:
        clear()
        blogo()
        OpenNodelistfunds()
    elif menuOP in ["D", "d"]:
        clear()
        blogo()
        OpenNodeListPayments()
    elif menuOP in ["S", "s"]:
        clear()
        blogo()
        OpenNodeCheckStatus()
    elif menuOP in ["R", "r"]:
        menuSelection()

def menuOpenNodeOnchainONLY(menuOP):
    if menuOP in ["A", "a"]:
        clear()
        blogo()
        OpenNodecreatecharge()
    elif menuOP in ["B", "b"]:
        clear()
        blogo()
        OpenNodeiniciatewithdrawal()
    elif menuOP in ["C", "c"]:
        clear()
        blogo()
        OpenNodelistfunds()
    elif menuOP in ["D", "d"]:
        clear()
        blogo()
        OpenNodeListPayments()
    elif menuOP in ["S", "s"]:
        clear()
        blogo()
        OpenNodeCheckStatus()
    elif menuOP in ["R", "r"]:
        menuSelection()

def menuLNPAY(menuNW):
    if menuNW in ["A", "a"]:
        clear()
        blogo()
        lnpayCreateInvoice()
    elif menuNW in ["B", "b"]:
        clear()
        blogo()
        lnpayPayInvoice()
    elif menuNW in ["C", "c"]:
        clear()
        blogo()
        lnpayGetBalance()
    elif menuNW in ["D", "d"]:
        clear()
        blogo()
        lnpayGetTransactions()
    elif menuNW in ["E", "e"]:
        clear()
        blogo()
        lnpayTransBWallets()
    elif menuNW in ["R", "r"]:
        menuSelection()

def menuLNPAYOnchainONLY(menuNW):
    if menuNW in ["A", "a"]:
        clear()
        blogo()
        lnpayCreateInvoice()
    elif menuNW in ["B", "b"]:
        clear()
        blogo()
        lnpayPayInvoice()
    elif menuNW in ["C", "c"]:
        clear()
        blogo()
        lnpayGetBalance()
    elif menuNW in ["D", "d"]:
        clear()
        blogo()
        lnpayGetTransactions()
    elif menuNW in ["E", "e"]:
        clear()
        blogo()
        lnpayTransBWallets()
    elif menuNW in ["R", "r"]:
        menuSelection()

def menuLNBPI(menuLNQ):
    if menuLNQ in ["A", "a"]:
        clear()
        blogo()
        lnbitCreateNewInvoice()
    elif menuLNQ in ["B", "b"]:
        clear()
        blogo()
        lnbitPayInvoice()
    elif menuLNQ in ["C", "c"]:
        clear()
        blogo()
        lnbitCreatePayWall()
    elif menuLNQ in ["D", "d"]:
        clear()
        blogo()
        lnbitDeletePayWall()
    elif menuLNQ in ["E", "e"]:
        clear()
        blogo()
        lnbitListPawWall()
    elif menuLNQ in ["F", "f"]:
        clear()
        blogo()
        lnbitsLNURLw()
    elif menuLNQ in ["G", "g"]:
        clear()
        blogo()
        lnbitsLNURLwList()
    elif menuLNQ in ["R", "r"]:
        menuSelection()

def menuLNBPIOnchainONLY(menuLNQ):
    if menuLNQ in ["A", "a"]:
        clear()
        blogo()
        lnbitCreateNewInvoice()
    elif menuLNQ in ["B", "b"]:
        clear()
        blogo()
        lnbitPayInvoice()
    elif menuLNQ in ["C", "c"]:
        clear()
        blogo()
        lnbitCreatePayWall()
    elif menuLNQ in ["D", "d"]:
        clear()
        blogo()
        lnbitDeletePayWall()
    elif menuLNQ in ["E", "e"]:
        clear()
        blogo()
        lnbitListPawWall()
    elif menuLNQ in ["F", "f"]:
        clear()
        blogo()
        lnbitsLNURLw()
    elif menuLNQ in ["G", "g"]:
        clear()
        blogo()
        lnbitsLNURLwList()
    elif menuLNQ in ["R", "r"]:
        menuSelection()

def rateSXMenu(menuSX):
    if menuSX in ["A", "a"]:
        clear()
        blogo()
        rateSXList()
    elif menuSX in ["B", "b"]:
        clear()
        blogo()
        rateSXGraph()
    elif menuSX in ["R", "r"]:
        menuSelection()

def rateSXMenuOnchainONLY(menuSX):
    if menuSX in ["A", "a"]:
        clear()
        blogo()
        rateSXList()
    elif menuSX in ["B", "b"]:
        clear()
        blogo()
        rateSXGraph()
    elif menuSX in ["R", "r"]:
        menuSelection()

#---------------END API-----------


def runTheNumbersControl(menuNumbers):
    if menuNumbers in ["A", "a"]:
        clear()
        blogo()
        countdownblock()
    elif menuNumbers in ["B", "b"]:
        clear()
        blogo()
        localHalving()
    elif menuNumbers in ["C", "c"]:
        clear()
        blogo()
        calc = """
                    ----------------------------
                             PROCESSING
                            THE  NUMBERS
                    ----------------------------
         """
        comeback = """
                    ----------------------------
                       MAKE YOURSELF A COFFEE
                         AND COME BACK IN A
                               MOMENT
                    ----------------------------
        """
        cprint(comeback, 'yellow')
        cprint(calc, 'red', attrs=['blink'])
        runthenumbers()
    elif menuNumbers in ["D", "d"]:
        clear()
        blogo()
        blockTmpConn()
    elif menuNumbers in ["E", "e"]:
        clear()
        blogo()
        missingConn()
    elif menuNumbers in ["U", "u"]:
        clear()
        blogo()
        unspendableConn()

def runTheNumbersControlOnchainONLY(menuNumbers):
    if menuNumbers in ["A", "a"]:
        clear()
        blogo()
        countdownblock()
    elif menuNumbers in ["B", "b"]:
        clear()
        blogo()
        localHalving()
    elif menuNumbers in ["C", "c"]:
        clear()
        blogo()
        calc = """
                    ----------------------------
                             PROCESSING
                            THE  NUMBERS
                    ----------------------------
         """
        comeback = """
                    ----------------------------
                       MAKE YOURSELF A COFFEE
                         AND COME BACK IN A
                               MOMENT
                    ----------------------------
        """
        cprint(comeback, 'yellow')
        cprint(calc, 'red', attrs=['blink'])
        runthenumbers()
    elif menuNumbers in ["D", "d"]:
        clear()
        blogo()
        blockTmpConn()
    elif menuNumbers in ["E", "e"]:
        clear()
        blogo()
        missingConn()
    elif menuNumbers in ["U", "u"]:
        clear()
        blogo()
        unspendableConn()

def runTheNumbersControlConn(menuNumbersconn):
    if menuNumbersconn in ["A", "a"]:
        clear()
        blogo()
        countdownblockConn()
    elif menuNumbersconn in ["B", "b"]:
        clear()
        blogo()
        remoteHalving()
    elif menuNumbersconn in ["C", "c"]:
        clear()
        blogo()
        calc = """
                    ----------------------------
                             PROCESSING
                            THE  NUMBERS
                    ----------------------------
         """
        comeback = """
                    ----------------------------
                       MAKE YOURSELF A COFFEE
                         AND COME BACK IN A
                               MOMENT
                    ----------------------------
        """
        cprint(comeback, 'yellow')
        cprint(calc, 'red', attrs=['blink'])
        runthenumbersConn()
    elif menuNumbers in ["D", "d"]:
        clear()
        blogo()
        blockTmpConn()
    elif menuNumbers in ["E", "e"]:
        clear()
        blogo()
        missingConn()
    elif menuNumbers in ["U", "u"]:
        clear()
        blogo()
        unspendableConn()

def menuWeather(menuWD):
    if menuWD in ["A", "a"]:
        wttrDataV1()
    elif menuWD in ["B", "b"]:
        wttrDataV2()

def menuWeatherOnchainONLY(menuWD):
    if menuWD in ["A", "a"]:
        wttrDataV1()
    elif menuWD in ["B", "b"]:
        wttrDataV2()

def mainmenuLOCALcontrol(menuS): #Execution of the Main Menu options
    if menuS in ["A", "a"]:
        artist()
    elif menuS in ["B", "b"]:
        bitcoincoremenuLOCAL()
    elif menuS in ["L", "l"]:
        lightningnetworkLOCAL()
    elif menuS in ["S", "s"]:
        settings4Local()
    elif menuS in ["P", "p"]:
        APIMenuLOCAL()
    elif menuS in ["X", "x"]:
        dnt()
    elif menuS in ["Q", "q"]:
        os._exit(0)
        apisnd.close()
        donation.close()
        clone.close()
        logos.close()
        feed.close()
        sysinf.close()
        nodeconnection.close()
        exit()
    elif menuS in ["T", "t"]:
        clear()
        delay_print("\033[1;32;40mWake up, Neo...")
        t.sleep(2)
        clear()
        delay_print("The Matrix has you...")
        t.sleep(2)
        clear()
        delay_print("Follow the white rabbit.")
        t.sleep(3)
        clear()
        print("Knock, knock, Neo.\033[0;37;40m\n")
        t.sleep(2)
        clear()
        t.sleep(3)
        screensv()
    elif menuS in ["nym", "Nym", "NYM", "nYm", "nyM", "NYm", "NyM", "nYM"]:
        clear()
        blogo()
        robotNym()
    elif menuS in ["wt", "WT", "Wt", "wT"]:
        clear()
        blogo()
        callGitWardenTerminal()
    elif menuS in ["CA", "ca", "Ca", "cA"]:
        clear()
        blogo()
        callGitCashu()

def mainmenuLOCALcontrolOnchainONLYCROPPED(menuS): #Execution of the Main Menu options
    if menuS in ["A", "a"]:
        artist()
    elif menuS in ["B", "b"]:
        bitcoincoremenuLOCALOnchainONLY()
    elif menuS in ["S", "s"]:
        settings4LocalOnchainONLY()
    elif menuS in ["P", "p"]:
        APIMenuLOCALOnchainONLY()
    elif menuS in ["X", "x"]:
        dntOnchainONLY()
    elif menuS in ["Q", "q"]:
        os._exit(0)
        apisnd.close()
        donation.close()
        clone.close()
        logos.close()
        feed.close()
        sysinf.close()
        nodeconnection.close()
        exit()
    elif menuS in ["T", "t"]:
        clear()
        delay_print("\033[1;32;40mWake up, Neo...")
        t.sleep(2)
        clear()
        delay_print("The Matrix has you...")
        t.sleep(2)
        clear()
        delay_print("Follow the white rabbit.")
        t.sleep(3)
        clear()
        print("Knock, knock, Neo.\033[0;37;40m\n")
        t.sleep(2)
        clear()
        t.sleep(3)
        screensv()
    elif menuS in ["nym", "Nym", "NYM", "nYm", "nyM", "NYm", "NyM", "nYM"]:
        clear()
        blogo()
        robotNym()
    elif menuS in ["wt", "WT", "Wt", "wT"]:
        clear()
        blogo()
        callGitWardenTerminal()
    elif menuS in ["CA", "ca", "Ca", "cA"]:
        clear()
        blogo()
        callGitCashu()

def slushpoolLOCALOnchainONLYMenu(slush):
    if slush in ["A", "a"]:
        clear()
        blogo()
        slDIFFConn()
    elif slush in ["B", "b"]:
        clear()
        blogo()
        slHASHConn()
    elif slush in ["C", "c"]:
        clear()
        blogo()
        slPOOLConn()
    elif slush in ["D", "d"]:
        clear()
        blogo()
        slHISTConn()
    elif slush in ["E", "e"]:
        clear()
        blogo()
        getPoolSlushCheck()

def bitcoincoremenuLOCALcontrolA(bcore):
    if bcore in ["A", "a"]:
        while True:
            try:
                clear()
                blogo()
                sysinfo()
                close()
                console()
                t.sleep(5)
            except:
                break
    elif bcore in ["B", "b"]:
        clear()
        blogo()
        getgenesis()
        input("Continue...")
        menuSelection()
    elif bcore in ["C", "c"]:
        getblock()
    elif bcore in ["D", "d"]:
        runTheNumbersMenu()
    elif bcore in ["E", "e"]:
        decodeHex()
    elif bcore in ["F", "f"]:
        try:
            clear()
            blogo()
            sysinfo()
            close()
            decodeQR()
            input("Continue...")
        except:
            pass
    elif bcore in ["G", "g"]:
        getrawtx()
    elif bcore in ["H", "h"]:
        miscellaneousLOCAL()
    elif bcore in ["I", "i"]:
        callColdCore()
    elif bcore in ["J", "j"]:
        pdfconvert()
    elif bcore in ["M", "m"]:
        mtConn()
    elif bcore in ["O", "o"]:
        bitcoincoremenuLOCALOPRETURN()
    elif bcore in ["Z", "z"]:
        statsConn()
    elif bcore in ["Q", "q"]:
        miningConn()
    elif bcore in ["U", "u"]:
        untxsConn()
    elif bcore in ["S", "s"]:
        counttxs()

def bitcoincoremenuLOCALcontrolAOnchainONLY(bcore):
    if bcore in ["A", "a"]:
        while True:
            try:
                clear()
                blogo()
                sysinfo()
                close()
                console()
                t.sleep(5)
            except:
                break
    elif bcore in ["B", "b"]:
        clear()
        blogo()
        getgenesis()
        input("Continue...")
        menuSelection()
    elif bcore in ["C", "c"]:
        getblock()
    elif bcore in ["D", "d"]:
        runTheNumbersMenuOnchainONLY()
    elif bcore in ["E", "e"]:
        decodeHexOnchainONLY()
    elif bcore in ["F", "f"]:
        try:
            clear()
            blogo()
            sysinfo()
            close()
            decodeQR()
            input("Continue...")
        except:
            pass
    elif bcore in ["G", "g"]:
        getrawtx()
    elif bcore in ["H", "h"]:
        miscellaneousLOCALOnchainONLY()
    elif bcore in ["I", "i"]:
        callColdCore()
    elif bcore in ["J", "j"]:
        pdfconvert()
    elif bcore in ["M", "m"]:
        mtConn()
    elif bcore in ["O", "o"]:
        bitcoincoremenuLOCALOPRETURNOnchainONLY()
    elif bcore in ["W", "w"]:
        walletmenuLOCALOnchainONLY()
    elif bcore in ["Z", "z"]:
        statsConn()
    elif bcore in ["Q", "q"]:
        miningConn()
    elif bcore in ["U", "u"]:
        untxsConn()
    elif bcore in ["S", "s"]:
        searchTXS()

def walletmenuLOCALcontrolAOnchainONLY(walletmnu):
    if walletmnu in ["A", "a"]:
        getnewaddressOnchain()
    elif walletmnu in ["B", "b"]:
        gettransactionsOnchain()

def bitcoincoremenuLOCALcontrolO(oreturn):
    if oreturn in ["A", "a"]:
        clear()
        blogo()
        opreturn()
    elif oreturn in ["B", "b"]:
        clear()
        blogo()
        opreturn_view()
    elif oreturn in ["C", "c"]:
        clear()
        blogo()
        opretminer()

def bitcoincoremenuLOCALcontrolOOnchainONLY(oreturn):
    if oreturn in ["A", "a"]:
        clear()
        blogo()
        opreturnOnchainONLY()
    elif oreturn in ["B", "b"]:
        clear()
        blogo()
        opreturn_view()
    elif oreturn in ["C", "c"]:
        clear()
        blogo()
        opretminer()

def miscellaneousLOCALmenu(misce):
    if misce in ["A", "a"]:
        while True:
            try:
                clear()
                blogo()
                close()
                logoA()
                tmp()
                clear()
                blogo()
                close()
                logoB()
                tmp()
                clear()
                blogo()
                close()
                logoC()
                tmp()
            except:
                break
    elif misce in ["B", "b"]:
        clear()
        blogo()
        close()
        sysinfoDetail()
    elif misce in ["C", "c"]:
        clear()
        blogo()
        datesConn()
    elif misce in ["D", "d"]:
        clear()
        blogo()
        quotesConn()
    elif misce in ["P", "p"]:
        clear()
        blogo()
        pgpConn()
    elif misce in ["S", "s"]:
        clear()
        blogo()
        satoshiConn()
    elif misce in ["Z", "z"]:
        clear()
        blogo()
        decodeStrDat()
    elif misce in ["R", "r"]:
        menuSelection()

def miscellaneousLOCALmenuOnchainONLY(misce):
    if misce in ["A", "a"]:
        while True:
            try:
                clear()
                blogo()
                close()
                logoA()
                tmp()
                clear()
                blogo()
                close()
                logoB()
                tmp()
                clear()
                blogo()
                close()
                logoC()
                tmp()
            except:
                break
    elif misce in ["B", "b"]:
        clear()
        blogo()
        close()
        sysinfoDetail()
    elif misce in ["D", "d"]:
        clear()
        blogo()
        quotesConn()
    elif misce in ["C", "c"]:
        clear()
        blogo()
        datesConn()
    elif misce in ["P", "p"]:
        clear()
        blogo()
        pgpConn()
    elif misce in ["S", "s"]:
        clear()
        blogo()
        satoshiConn()
    elif misce in ["Z", "z"]:
        clear()
        blogo()
        decodeStrDat()
    elif misce in ["R", "r"]:
        menuSelection()

def decodeHexLOCAL(hexloc):
    if hexloc in ["A", "a"]:
        clear()
        blogo()
        close()
        try:
            readHexBlock()
            while True:
                r = input("Do you want to continue decoding? Y/n: ")
                if r not in ["Y", "y"]:
                    break
                clear()
                blogo()
                readHexBlock()
        except:
            pass
    elif hexloc in ["B", "b"]:
        clear()
        blogo()
        close()
        try:
            readHexTx()
            while True:
                r = input("Do you want to continue decoding? Y/n: ")
                if r not in ["Y", "y"]:
                    break
                clear()
                blogo()
                sysinfo()
                readHexTx()
        except:
            pass

def decodeHexLOCALOnchainONLY(hexloc):
    if hexloc in ["A", "a"]:
        clear()
        blogo()
        close()
        try:
            readHexBlock()
            while True:
                r = input("Do you want to continue decoding? Y/n: ")
                if r not in ["Y", "y"]:
                    break
                clear()
                blogo()
                readHexBlock()
        except:
            pass
    elif hexloc in ["B", "b"]:
        clear()
        blogo()
        close()
        try:
            readHexTx()
            while True:
                r = input("Do you want to continue decoding? Y/n: ")
                if r not in ["Y", "y"]:
                    break
                clear()
                blogo()
                sysinfo()
                readHexTx()
        except:
            pass

def lightningnetworkLOCALcontrol(lncore):
    if lncore in ["A", "a"]:
        clear()
        blogo()
        consoleLNC()
    elif lncore in ["B", "b"]:
        clear()
        blogo()
        localaddinvoiceC()
    elif lncore in ["C", "c"]:
        clear()
        blogo()
        localpayinvoiceC()
    elif lncore in ["D", "d"]:
        clear()
        blogo()
        localkeysendC()
    elif lncore in ["E", "e"]:
        clear()
        blogo()
        localnewaddressC()
    elif lncore in ["F", "f"]:
        clear()
        blogo()
        locallistinvoicesC()
    elif lncore in ["G", "g"]:
        clear()
        blogo()
        localchannelbalanceC()
    elif lncore in ["H", "h"]:
        clear()
        blogo()
        locallistchannelsC()
    elif lncore in ["I", "i"]:
        clear()
        blogo()
        localrebalancelndC()
    elif lncore in ["J", "j"]:
        clear()
        blogo()
        locallistpeersQQC()
    elif lncore in ["K", "k"]:
        clear()
        blogo()
        localconnectpeerC()
    elif lncore in ["L", "l"]:
        clear()
        blogo()
        localbalanceOCC()
    elif lncore in ["M", "m"]:
        clear()
        blogo()
        locallistchaintxnsC()
    elif lncore in ["N", "n"]:
        clear()
        blogo()
        localgetinfoC()
    elif lncore in ["O", "o"]:
        clear()
        blogo()
        localgetnetworkinfoC()
    elif lncore in ["P", "p"]:
        clear()
        blogo()
        chatConn()
    elif lncore in ["Z", "z"]:
        clear()
        blogo()
        stalnConn()
    elif lncore in ["T", "t"]:
        clear()
        blogo()
        ranConn()
    elif lncore in ["Q", "q"]:
        if os.path.isfile("lnbitSN.conf"):
            lnbitsLNURLwList()
    elif lncore in ["S", "s"]:
        if os.path.isfile("lnbitSN.conf"):
            lnbitsLNURLw()
    elif lncore in ["R", "r"]:
        menuSelection()

def chatConnA(menuch):
    if menuch in ["A", "a"]:
        pyCHATA()
    elif menuch in ["B", "b"]:
        pyCHATB()
    elif menuch in ["C", "c"]:
        pyCHATC()

def chatConnB(pyCHATA):
    if pyCHATA in ["A", "a"]:
        clear()
        blogo()
        localchatsendAC()
    elif pyCHATA in ["B", "b"]:
        clear()
        blogo()
        localchatnewAC()
    elif pyCHATA in ["C", "c"]:
        clear()
        blogo()
        localchatlistAC()

def chatConnC(pyCHATB):
    if pyCHATB in ["A", "a"]:
        clear()
        blogo()
        localchatsendBC()
    elif pyCHATB in ["B", "b"]:
        clear()
        blogo()
        localchatnewBC()
    elif pyCHATB in ["C", "c"]:
        clear()
        blogo()
        localchatlistBC()

def chatConnD(pyCHATC):
    if pyCHATC in ["A", "a"]:
        clear()
        blogo()
        localchatsendCC()
    elif pyCHATC in ["B", "b"]:
        clear()
        blogo()
        localchatnewCC()
    elif pyCHATC in ["C", "c"]:
        clear()
        blogo()
        localchatlistCC()

def platfformsLOCALcontrol(platf):
    if platf in ["A", "a"]:
        aaccPPiTippinMe()
    elif platf in ["B", "b"]:
        aaccPPiTallyCo()
    elif platf in ["C", "c"]:
        mempoolmenu()
    elif platf in ["D", "d"]:
        clear()
        blogo()
        CoingeckoPP()
    elif platf in ["E", "e"]:
        rateSX()
    elif platf in ["F", "f"]:
        bwtConn()
    elif platf in ["G", "g"]:
        aaccPPiLNBits()
    elif platf in ["H", "h"]:
        aaccPPiLNPay()
    elif platf in ["I", "i"]:
        aaccPPiOpenNode()
    elif platf in ["J", "j"]:
        satnodeMenu()
    elif platf in ["K", "k"]:
        weatherMenu()
    elif platf in ["L", "l"]:
        gameroom()
    elif platf in ["M", "m"]:
        whalalConn()
    elif platf in ["N", "n"]:
        nostrConn()
    elif platf in ["P", "p"]:
        kanopoolpoolLOCALOnchainONLY()
    elif platf in ["S", "s"]:
        slushpoolLOCALOnchainONLY()
    elif platf in ["W", "w"]:
        ckpoolpoolLOCALOnchainONLY()
    elif platf in ["R", "r"]:
        menuSelection()

def platfformsLOCALcontrolOnchainONLY(platf):
    if platf in ["A", "a"]:
        aaccPPiTippin()
    elif platf in ["B", "b"]:
        aaccPPiTallyCo()
    elif platf in ["C", "c"]:
        mempoolmenuOnchainONLY()
    elif platf in ["D", "d"]:
        clear()
        blogo()
        CoingeckoPP()
    elif platf in ["E", "e"]:
        rateSXOncainONLY()
    elif platf in ["F", "f"]:
        bwtConn()
    elif platf in ["G", "g"]:
        aaccPPiLNBits()
    elif platf in ["H", "h"]:
        aaccPPiLNPay()
    elif platf in ["I", "i"]:
        aaccPPiOpenNode()
    elif platf in ["J", "j"]:
        satnodeMenuOnchainONLY()
    elif platf in ["K", "k"]:
        weatherMenuOnchainONLY()
    elif platf in ["L", "l"]:
        gameroom()
    elif platf in ["M", "m"]:
        whalalConn()
    elif platf in ["N", "n"]:
        nostrConn()
    elif platf in ["P", "p"]:
        kanopoolpoolLOCALOnchainONLY()
    elif platf in ["S", "s"]:
        slushpoolLOCALOnchainONLY()
    elif platf in ["W", "w"]:
        ckpoolpoolLOCALOnchainONLY()
    elif platf in ["R", "r"]:
        menuSelection()

#----------------------------REMOTE MENUS

def mainmenuREMOTEcontrol(menuS): #Execution of the Main Menu options
    if menuS in ["A", "a"]:
        while True:
            try:
                clear()
                close()
                remotegetblock()
                tmp()
            except:
                break
    elif menuS in ["B", "b"]:
        bitcoincoremenuREMOTE()
    elif menuS in ["L", "l"]:
        lightningnetworkREMOTE()
    elif menuS in ["P", "p"]:
        APIMenuLOCAL()
    elif menuS in ["X", "x"]:
        dnt()
    elif menuS in ["S", "s"]:
        settings4Remote()
    elif menuS in ["Q", "q"]:
        os._exit(0)
        apisnd.close()
        donation.close()
        clone.close()
        logos.close()
        feed.close()
        sysinf.close()
        nodeconnection.close()
        exit()
    elif menuS in ["T", "t"]: #Test feature fast access
        clear()
        delay_print("\033[1;32;40mWake up, Neo...")
        t.sleep(2)
        clear()
        delay_print("The Matrix has you...")
        t.sleep(2)
        clear()
        delay_print("Follow the white rabbit.")
        t.sleep(3)
        clear()
        print("Knock, knock, Neo.\033[0;37;40m\n")
        t.sleep(2)
        clear()
        t.sleep(3)
        screensv()
    elif menuS in ["nym", "Nym", "NYM", "nYm", "nyM", "NYm", "NyM", "nYM"]:
        clear()
        blogo()
        robotNym()
    elif menuS in ["wt", "WT", "Wt", "wT"]:
        clear()
        blogo()
        callGitWardenTerminal()

def bitcoincoremenuREMOTEcontrol(bcore):
    if bcore in ["A", "a"]:
        while True:
            try:
                clear()
                blogo()
                sysinfo()
                close()
                remoteconsole()
                t.sleep(5)
            except:
                break
    elif bcore in ["B", "b"]:
        remotegetblockcount()
    elif bcore in ["C", "c"]:
        runTheNumbersMenuConn()
    elif bcore in ["D", "d"]:
        try:
            clear()
            blogo()
            sysinfo()
            close()
            decodeQR()
            input("Continue...")
        except:
            pass
    elif bcore in ["E", "e"]:
        miscellaneousLOCAL()
    elif bcore in ["O", "o"]:
        bitcoincoremenuREMOTEOPRETURN()
    elif bcore in ["Z", "z"]:
        statsConn()
    elif bcore in ["Q", "q"]:
        miningConn()
    elif bcore in ["U", "u"]:
        untxsConn()

def bitcoincoremenuREMOTEcontrolO(oreturn):
    if oreturn in ["A", "a"]:
        clear()
        blogo()
        opreturn()
    elif oreturn in ["B", "b"]:
        clear()
        blogo()
        opreturn_view()
    elif oreturn in ["C", "c"]:
        clear()
        blogo()
        opretminer()

def lightningnetworkREMOTEcontrol(lncore):
    if lncore in ["A", "a"]:
        clear()
        blogo()
        getnewinvoice()
    elif lncore in ["B", "b"]:
        clear()
        blogo()
        payinvoice()
    elif lncore in ["C", "c"]:
        clear()
        blogo()
        getnewaddress()
    elif lncore in ["D", "d"]:
        clear()
        blogo()
        listinvoice()
    elif lncore in ["E", "e"]:
        clear()
        blogo()
        channelbalance()
    elif lncore in ["F", "f"]:
        clear()
        blogo()
        channels()
    elif lncore in ["G", "g"]:
        clear()
        blogo()
        balanceOC()
    elif lncore in ["H", "h"]:
        clear()
        blogo()
        listonchaintxs()
    elif lncore in ["I", "i"]:
        clear()
        blogo()
        getinfo()
    elif lncore in ["Z", "z"]:
        clear()
        blogo()
        stalnConn()
    elif lncore in ["T", "t"]:
        clear()
        blogo()
        ranConn()
    elif lncore in ["Q", "q"]:
        if os.path.isfile("lnbitSN.conf"):
            lnbitsLNURLwList()
    elif lncore in ["S", "s"]:
        if os.path.isfile("lnbitSN.conf"):
            lnbitsLNURLw()
    elif lncore in ["R", "r"]:
        menuSelection()

def menuC(menuO): # Donation access Menu
    if menuO in ["A", "a"]:
        dntDev()
    elif menuO in ["B", "b"]:
        dntTst()
    elif menuO in ["R", "r"]:
        menuSelection()

def menuCOnchainONLY(menuO): # Donation access Menu
    if menuO in ["A", "a"]:
        dntDevOnchainONLY()
    elif menuO in ["B", "b"]:
        dntTstOnchainONLY()
    elif menuO in ["R", "r"]:
        menuSelection()

def menuD(menuN): # Satnode access Menu
    if menuN in ["A", "a"]:
        satnode()
    elif menuN in ["B", "b"]:
        readFile()
    elif menuN in ["S", "s"]:
        try:
            clear()
            blogo()
            close()
            message = input("\n\033[0;37;40mYour message it's a \033[1;34;40mF\033[0;37;40mile or a plain \033[1;32;40mT\033[0;37;40mext? \033[1;34;40mF\033[0;37;40m/\033[1;32;40mT\033[0;37;40m: ")
            if message in ["F", "f"]:
                try:
                    clear()
                    blogo()
                    close()
                    apisenderFile()
                    t.sleep(30)
                    menuSelection()
                except:
                    menuSelection()
            elif message in ["T", "t"]:
                try:
                    clear()
                    blogo()
                    close()
                    apisender()
                    t.sleep(30)
                    menuSelection()
                except:
                    menuSelection()
        except:
            menuSelection()
    elif menuN in ["C", "c"]:
        try:
            print("\n\t This only will work on Linux or Unix systems.\n")
            a = input("Do we continue? Y/n: ")
            if a in ["Y", "y"]:
                gitclone()
            else:
                menuSelection()
        except:
            pass
    elif menuN in ["R", "r"]:
        menuSelection()

def menuE(menuQ): # Dev Donation access Menu
    if menuQ in ["A", "a"]:
        try:
            clear()
            blogo()
            close()
            donationPayNym()
            t.sleep(50)
            menuSelection()
        except:
            menuSelection()
    elif menuQ in ["B", "b"]:
        try:
            clear()
            blogo()
            close()
            donationAddr()
            t.sleep(50)
            menuSelection()
        except:
            menuSelection()
    elif menuQ in ["C", "c"]:
        try:
            clear()
            blogo()
            close()
            donationLN()
            t.sleep(50)
            menuSelection()
        except:
            menuSelection()
    elif menuQ in ["R", "r"]:
        menuSelection()

def menuEOnchainONLY(menuQ): # Dev Donation access Menu
    if menuQ in ["A", "a"]:
        try:
            clear()
            blogo()
            close()
            donationPayNym()
            t.sleep(50)
            menuSelection()
        except:
            menuSelection()
    elif menuQ in ["B", "b"]:
        try:
            clear()
            blogo()
            close()
            donationAddr()
            t.sleep(50)
            menuSelection()
        except:
            menuSelection()
    elif menuQ in ["C", "c"]:
        try:
            clear()
            blogo()
            close()
            donationLN()
            t.sleep(50)
            menuSelection()
        except:
            menuSelection()
    elif menuQ in ["R", "r"]:
        menuSelection()

def menuF(menuV): # Tester Donation access Menu
    if menuV in ["A", "a"]:
        try:
            clear()
            blogo()
            close()
            donationAddrTst()
            t.sleep(50)
            menuSelection()
        except:
            menuSelection()
    elif menuV in ["B", "b"]:
        try:
            clear()
            blogo()
            close()
            donationLNTst()
            t.sleep(50)
            menuSelection()
        except:
            menuSelection()
    elif menuV in ["R", "r"]:
        menuSelection()

def menuFOnchainONLY(menuV): # Tester Donation access Menu
    if menuV in ["A", "a"]:
        try:
            clear()
            blogo()
            close()
            donationAddrTst()
            t.sleep(50)
            menuSelection()
        except:
            menuSelection()
    elif menuV in ["B", "b"]:
        try:
            clear()
            blogo()
            close()
            donationLNTst()
            t.sleep(50)
            menuSelection()
        except:
            menuSelection()
    elif menuV in ["R", "r"]:
        menuSelection()
#---------------------------------------------------------------------------------

def nostrmenu(menunos):
    if menunos in ["A", "a"]:
        callGitNostrLinTerminal()
    elif menunos in ["B", "b"]:
        callGitNostrWinTerminal()
    elif menunos in ["C", "c"]:
        callGitNostrMacTerminal()
    elif menunos in ["S", "s"]:
        callGitNostrSeedTerminal()

def testClockRemote():
    b = rpc('getblockcount')
    c = str(b)
    a = c
    output = render(
        c,
        colors=[settingsClock['colorA'], settingsClock['colorB']],
        align='left',
    )

    print(output)
    print("""

    -------------------------
        Front Color: {}
        Back Color:  {}
    -------------------------

    """.format(settingsClock['colorA'], settingsClock['colorB']))
    try:
        print("<<< Cancel Control + C")
        input("Enter To Apply...")
        settingsClock["gradient"] = "color"
        pickle.dump(settingsClock, open("pyblocksettingsClock.conf", "wb"))
    except:
        pass
