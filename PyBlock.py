#Developer: Curly60e
#PyBLOCK its a clock of the Bitcoin blockchain.
#Version: 0.5.0

import os
import os.path
import time as t
import pickle
import psutil
import qrcode
import random
from clone import *
from donation import *
from feed import *
from art import *
from logos import *
from sysinf import *
from pblogo import *
from apisnd import *
from ppi import *
from nodeconnection import *
from terminal_matrix.matrix import *



def sysinfo():  #Cpu and memory usage
    print("   \033[0;37;40m----------------------")
    print("   \033[3;33;40mCPU Usage: \033[1;32;40m" + str(psutil.cpu_percent()) + "%\033[0;37;40m")
    print("   \033[3;33;40mMemory Usage: \033[1;32;40m" "{}% \033[0;37;40m".format(int(psutil.virtual_memory().percent)))
    print("   \033[0;37;40m----------------------")



def getblock(): # get access to bitcoin-cli with the command getblockchaininfo
    bitcoincli = " getblockchaininfo"
    a = os.popen(path['bitcoincli'] + bitcoincli).read()
    b = json.loads(a)
    d = b
    print(d)
    clear()
    print("\033[1;32;40m")
    blogo()
    print("\033[0;37;40m")
    print("<<< Back to the Main Menu Press Control + C.\n\n")
    print("\n----------------------------------------------------------------------------------------------------------------")
    print("""
    Chain: {}
    Blocks: {}
    Best BlockHash: {}
    Difficulty: {}
    Verification Progress: {}
    Size on Disk: {}
    Pruned: {}
    """.format(d['chain'], d['blocks'], d['bestblockhash'], d['difficulty'], d['verificationprogress'], d['size_on_disk'], d['pruned']))
    print("----------------------------------------------------------------------------------------------------------------\n")

def getblockcount(): # get access to bitcoin-cli with the command getblockcount
    bitcoincli = " getblockcount"
    os.system(path['bitcoincli'] + bitcoincli)

def clear(): # clear the screen
    os.system('cls' if os.name=='nt' else 'clear')

def getgenesis(): # get and decode Genesis block
    bitcoincli = " getblock 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f 0 | xxd -r -p | hexyl -n 256"
    os.system(path['bitcoincli'] + bitcoincli)

def close():
    print("<<< Back to the Main Menu Press Control + C.\n\n")

def readHexBlock(): # Hex Decoder using Hexyl on local node
    hexa = input("Add the Block Hash you want to decode: ")
    blocknumber = input("Add the Block number: ")
    decodeBlock = path['bitcoincli'] + " getblock {} {}".format(hexa, blocknumber) + " | xxd -r -p | hexyl -n 256"
    os.system(decodeBlock)

def readHexTx(): # Hex Decoder using Hexyl on an external node
    hexa = input("Add the Transaction ID. you want to decode: ")
    decodeTX = path['bitcoincli'] + " getrawtransaction {}".format(hexa) + " | xxd -r -p | hexyl -n 256"
    os.system(decodeTX)

def prt():
    print("\033[1;32;40m")
    blogo()
    print("\033[0;37;40m")

def tmp():
    t.sleep(15)

def console(): # get into the console from bitcoin-cli
    print("\t\033[0;37;40mThis is \033[1;33;40mBitcoin-cli's \033[0;37;40mconsole. Type your respective commands you want to display.\n\n")
    while True:
        cle = input("\033[1;32;40mconsole $>: \033[0;37;40m")
        lsd = os.popen(path['bitcoincli'] + " " + cle)
        lsd0 = lsd.read()
        lsd1 = str(lsd0)
        print(lsd1)
        lsd.close()

def screensv():
    try:
        doit()
    except (KeyboardInterrupt, SystemExit):
        matrix.close()
        clear()
        ptr()
        menu()
#------------------------------------------------------

def connected(info): # here we complete the connection to the external node
    if info == "Y" or info == "y":
        clear()
        prt()
        print("\nAdd your node information\n")
        menuUserConn()
    else:
        menu()


def nodeinfo():
    print("\n\033[1;31;40mWARNING! This is not a safe method of connection. The best method is doing this locally.\n")
    connected(input("WARNING! Are you sure you want to connect to a node? Y/n: \033[0;37;40m")) # call 'connected' function to make the connection with the node information


def artist(): # here we convert the result of the command 'getblockcount' on a random art design
    custom = input("Do you want random designs? Y/n: ")
    if custom == "Y" or custom == "y":
        while True:
            try:
                clear()
                close()
                design()
                tmp()
            except (KeyboardInterrupt, SystemExit):
                menu()
                raise
    else:
        while True:
            try:
                clear()
                close()
                getblockcount()
                tmp()
            except (KeyboardInterrupt, SystemExit):
                menu()
                raise

def design():
    bitcoinclient = path['bitcoincli'] + " getblockcount"
    block = os.popen(str(bitcoinclient)).read() # 'getblockcount' convert to string
    b = block
    print("\033[1;32;40m")
    tprint(b, font="rnd-large")
    print("\033[0;37;40m")


#--------------------------------- Hex Block Decoder Functions -------------------------------------

def getrawtx(): # show confirmatins from transactions
    tx = input("Insert your TxID: ")
    while True:
        try:
            clear()
            prt()
            close()
            bitcoincli = " getrawtransaction "
            if tx == "4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b":
                print("""\t\t\n\033[1;35;40mThis transaction it's the first one of the Bitcoin Blockchain on Block 0 by Satoshi Nakamoto.
You can decode that block in HEX and see what's inside.\033[0;37;40m""")
                t.sleep(10)
            else:
                lsd = os.popen(path['bitcoincli'] + bitcoincli + tx + " 1")
                lsd0 = lsd.read()
                lsd1 = str(lsd0)
                lsda = lsd1.split(',')
                lsdb = lsda[-3]
                lsdc = str(lsdb)
                print("\033[0;37;40mTransaction " + "\033[1;31;40m{}\033[0;37;40m".format(tx) + " has:\n" + "\033[1;31;40m{}\033[0;37;40m".format(lsdc))
                tmp()
                lsd.close()
        except (KeyboardInterrupt, SystemExit):
            menu()
#--------------------------------- End Hex Block Decoder Functions -------------------------------------

#--------------------------------- Menu section -----------------------------------

def menu(): #Main Menu
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m Menu
    Local Node
    Version 0.5.0

    \033[1;31;40mA.\033[0;37;40m Run PyBLOCK
    \033[1;32;40mB.\033[0;37;40m Show Blockchain information
    \033[1;32;40mC.\033[0;37;40m Show the Genesis Block
    \033[1;32;40mD.\033[0;37;40m Decode in HEX any block
    \033[1;32;40mE.\033[0;37;40m Decode in HEX any transaction
    \033[1;32;40mF.\033[0;37;40m Show confirmations from a transaction
    \033[1;32;40mH.\033[0;37;40m Advanced
    \033[1;33;40mL.\033[0;37;40m Lightning Network
    \033[1;34;40mS.\033[0;37;40m SatNode
    \033[3;33;40mP.\033[0;37;40m Premium
    \033[1;35;40mX.\033[0;37;40m Donate
    \033[1;33;40mQ.\033[0;37;40m Exit
    \n\n""")
    menuA(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def menuUserConn(): #Menu before connection over ssh
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m Menu
    Remote Node RPC
    Version 0.5.0

    \033[1;31;40mA.\033[0;37;40m Run PyBLOCK
    \033[1;32;40mB.\033[0;37;40m Show Blockchain information
    \033[1;33;40mL.\033[0;37;40m Lightning Network
    \033[1;32;40mH.\033[0;37;40m Advanced
    \033[1;34;40mS.\033[0;37;40m SatNode
    \033[3;33;40mP.\033[0;37;40m Premium
    \033[1;35;40mX.\033[0;37;40m Donate
    \033[1;33;40mQ.\033[0;37;40m Exit
    \n\n""")
    menuRemote(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def advanceMenu(): # Advanced Menu
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m Menu
    Version 0.5.0

    \033[1;32;40mA.\033[0;37;40m Bitconi-cli Console
    \033[1;32;40mB.\033[0;37;40m FunB
    \033[1;32;40mC.\033[0;37;40m Show QR from a Bitcoin Address
    \033[1;32;40mS.\033[0;37;40m Sysinfo
    \033[1;36;40mR.\033[0;37;40m Return Main Menu
    \n\n""")
    menuB(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def remoteadvanceMenu(): # Advanced Menu
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m Menu
    Version 0.5.0

    \033[1;32;40mA.\033[0;37;40m Bitconi-cli Console
    \033[1;32;40mB.\033[0;37;40m FunB
    \033[1;32;40mC.\033[0;37;40m Show QR from a Bitcoin Address
    \033[1;32;40mS.\033[0;37;40m Sysinfo
    \033[1;36;40mR.\033[0;37;40m Return Main Menu
    \n\n""")
    menuBA(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def dnt(): # Donation selection menu
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m Menu
    Version 0.5.0

    \033[1;32;40mA.\033[0;37;40m Developers Donation
    \033[1;32;40mB.\033[0;37;40m Testers Donation
    \033[1;36;40mR.\033[0;37;40m Return Main Menu
    \n\n""")
    menuC(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def dntDev(): # Dev Donation Menu
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m Menu
    Version 0.5.0

    \033[1;32;40mA.\033[0;37;40m PayNym
    \033[1;32;40mB.\033[0;37;40m Bitcoin Address
    \033[1;32;40mC.\033[0;37;40m Lightning Network
    \033[1;36;40mR.\033[0;37;40m Return Main Menu
    \n\n""")
    menuE(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def dntTst(): # Tester Donation Menu
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m Menu
    Version 0.5.0

    \033[1;32;40mA.\033[0;37;40m Bitcoin Address
    \033[1;32;40mB.\033[0;37;40m Lightning Network
    \033[1;36;40mR.\033[0;37;40m Return Main Menu
    \n\n""")
    menuF(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def satnodeMenu(): # Satnode Menu
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m Menu
    Version 0.4.0

    \033[1;32;40mA.\033[0;37;40m Start SatNode
    \033[1;32;40mB.\033[0;37;40m Feed
    \033[1;32;40mC.\033[0;37;40m Setup
    \033[1;34;40mS.\033[0;37;40m Send a Message to Space
    \033[1;36;40mD.\033[0;37;40m Return Main Menu
    \n\n""")
    menuD(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def menuLND():
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m Lightning Network Menu
    Remote node connection
    Version 0.5.0

    \033[1;32;40mI.\033[0;37;40m New Invoice
    \033[1;31;40mP.\033[0;37;40m Pay Invoice
    \033[1;32;40mQ.\033[0;37;40m Channel Balance
    \033[1;31;40mL.\033[0;37;40m List Invoices
    \033[1;32;40mC.\033[0;37;40m Show Channels
    \033[1;33;40mB.\033[0;37;40m New Bitcoin Address
    \033[1;33;40mX.\033[0;37;40m List Onchain Transactions
    \033[1;32;40mN.\033[0;37;40m Get Node Info
    \033[1;32;40mO.\033[0;37;40m Onchain Balance
    \033[1;36;40mR.\033[0;37;40m Return Main Menu
    \n\n""")
    menuLN(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def menuLNDLOCAL():
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m Lightning Network Menu
    Local node connection
    Version 0.5.0

    \033[1;32;40mI.\033[0;37;40m New Invoice
    \033[1;31;40mP.\033[0;37;40m Pay Invoice
    \033[1;32;40mK.\033[0;37;40m Make a KeySend Payment
    \033[1;31;40mL.\033[0;37;40m List Invoices
    \033[1;32;40mQ.\033[0;37;40m Channel Balance
    \033[1;32;40mC.\033[0;37;40m Show Channels
    \033[1;32;40mN.\033[0;37;40m Get Node Info
    \033[1;32;40mW.\033[0;37;40m Get Network Information
    \033[1;32;40mJ.\033[0;37;40m Lncli Console
    \033[1;33;40mB.\033[0;37;40m New Bitcoin Address
    \033[1;33;40mX.\033[0;37;40m List Onchain Transactions
    \033[1;32;40mO.\033[0;37;40m Onchain Balance
    \033[1;36;40mR.\033[0;37;40m Return Main Menu
    \n\n""")
    menuLNlocal(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def APIMenu():
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m API \033[1;34;40mPremium\033[0;37;40m Menu
    Version 0.5.0

    \033[1;32;40mA.\033[0;37;40m TippinMe FREE
    \033[1;32;40mB.\033[0;37;40m LNBits   \033[3;35;40m{lnbitspaid}\033[0;37;40m
    \033[1;32;40mC.\033[0;37;40m LNPay    \033[3;35;40m{lnpaypaid}\033[0;37;40m
    \033[1;32;40mD.\033[0;37;40m OpenNode \033[3;35;40m{opennodepaid}\033[0;37;40m
    \033[1;36;40mR.\033[0;37;40m Return Main Menu
    \n\n""".format(lnbitspaid = "PAID" if os.path.isfile("lnbitSN.conf") else "PREMIUM", lnpaypaid = "PAID" if os.path.isfile("lnpaySN.conf") else "PREMIUM", opennodepaid = "PAID" if os.path.isfile("opennodeSN.conf") else "PREMIUM"))
    menuPI(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def APILnbit():
    bitLN = {"NN":"","pd":""}
    if os.path.isfile('lnbitSN.conf'): # Check if the file 'bclock.conf' is in the same folder
        bitData= pickle.load(open("lnbitSN.conf", "rb")) # Load the file 'bclock.conf'
        bitLN = bitData # Copy the variable pathv to 'path'
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m LNBits SN:{} \033[1;34;40mPremium\033[0;37;40m Menu
    Version 0.5.0

    \033[1;32;40mA.\033[0;37;40m New Invoice
    \033[1;32;40mB.\033[0;37;40m Pay Invoice
    \033[1;32;40mC.\033[0;37;40m New PayWall
    \033[1;32;40mD.\033[0;37;40m Delete PayWall
    \033[1;32;40mE.\033[0;37;40m List PayWalls
    \033[1;36;40mR.\033[0;37;40m Return Main Menu
    \n\n""".format(bitLN['NN']))
    menuLNBPI(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def APILnPay():
    bitLN = {"NN":"","pd":""}
    if os.path.isfile('lnpaySN.conf'): # Check if the file 'bclock.conf' is in the same folder
        bitData= pickle.load(open("lnpaySN.conf", "rb")) # Load the file 'bclock.conf'
        bitLN = bitData # Copy the variable pathv to 'path'
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m LNPay SN:{} \033[1;34;40mPremium\033[0;37;40m Menu
    Version 0.5.0

    \033[1;32;40mA.\033[0;37;40m New Invoice
    \033[1;32;40mB.\033[0;37;40m Pay Invoice
    \033[1;32;40mC.\033[0;37;40m Wallet Balance
    \033[1;32;40mD.\033[0;37;40m List Invoices
    \033[1;32;40mE.\033[0;37;40m Transfer Between Wallets
    \033[1;36;40mR.\033[0;37;40m Return Main Menu
    \n\n""".format(bitLN['NN']))
    menuLNPAY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def APIOpenNode():
    bitLN = {"NN":"","pd":""}
    if os.path.isfile('opennodeSN.conf'): # Check if the file 'bclock.conf' is in the same folder
        bitData= pickle.load(open("opennodeSN.conf", "rb")) # Load the file 'bclock.conf'
        bitLN = bitData # Copy the variable pathv to 'path'
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m OpenNode SN:{} \033[1;34;40mPremium\033[0;37;40m Menu
    Version 0.5.0

    \033[1;32;40mA.\033[0;37;40m New Invoice
    \033[1;32;40mB.\033[0;37;40m Pay Invoice
    \033[1;32;40mC.\033[0;37;40m Wallet Balance
    \033[1;32;40mD.\033[0;37;40m List Payments
    \033[1;36;40mR.\033[0;37;40m Return Main Menu
    \n\n""".format(bitLN['NN']))
    menuOpenNode(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def APITippinMe():
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m TippinMe \033[1;34;40mFree\033[0;37;40m Menu
    Version 0.5.0

    \033[1;32;40mA.\033[0;37;40m New Invoice
    \033[1;36;40mR.\033[0;37;40m Return Main Menu
    \n\n""")
    menuTippinMe(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def menuSelection():
    path = {"ip_port":"", "rpcuser":"", "rpcpass":"", "bitcoincli":""}
    pathv = pickle.load(open("bclock.conf", "rb")) # Load the file 'bclock.conf'
    path = pathv # Copy the variable pathv to 'path'
    if path['bitcoincli']:
        menu()
    else:
        menuUserConn()

def menuSelectionLN():
    lndconnectload = {"ip_port":"", "tls":"", "macaroon":"", "lncli":""}
    lndconnectData = pickle.load(open("blndconnect.conf", "rb")) # Load the file 'bclock.conf'
    lndconnectload = lndconnectData # Copy the variable pathv to 'path'
    if lndconnectload['ln']:
        menuLNDLOCAL()
    else:
        menuLND()

def aaccPPiLNBits():
    bitLN = {"NN":"","pd":""}
    if os.path.isfile('lnbitSN.conf'):
        bitData= pickle.load(open("lnbitSN.conf", "rb"))
        bitLN = bitData
        APILnbit()
    else:
        qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        )
        curl = 'curl -X POST https://lnbits.com/api/v1/payments -d ' + "'{" + """"out": false, "amount": 100000, "memo": "LNBits on PyBLOCK" """ + "}'" + """ -H "X-Api-Key: 1d646820055e4e2da218e801eaacfc94 " -H "Content-type: application/json" """
        sh = os.popen(curl).read()
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
            print("Lightning Invoice: " + c)
            dn = str(d['checking_id'])
            t.sleep(10)
            checkcurl = 'curl -X GET https://lnbits.com/api/v1/payments/' + dn + """ -H "X-Api-Key: 1d646820055e4e2da218e801eaacfc94" -H "Content-type: application/json" """
            rsh = os.popen(checkcurl).read()
            clear()
            blogo()
            nn = str(rsh)
            dd = json.loads(nn)
            db = dd['paid']
            if db == True:
                clear()
                blogo()
                tick()
                bitLN['NN'] = randrange(10000000)
                bitLN['pd'] = "PAID"
                pickle.dump(bitLN, open("lnbitSN.conf", "wb"))
                createFileConnLNBits()
                break
            else:
                continue

def aaccPPiLNPay():
    bitLN = {"NN":"","pd":""}
    if os.path.isfile('lnpaySN.conf'): # Check if the file 'bclock.conf' is in the same folder
        bitData= pickle.load(open("lnpaySN.conf", "rb")) # Load the file 'bclock.conf'
        bitLN = bitData # Copy the variable pathv to 'path'
        APILnPay()
    else:
        qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        )
        curl = 'curl -X POST https://lnbits.com/api/v1/payments -d ' + "'{" + """"out": false, "amount": 100000, "memo": "LNPay on PyBLOCK" """ + "}'" + """ -H "X-Api-Key: 1d646820055e4e2da218e801eaacfc94 " -H "Content-type: application/json" """
        sh = os.popen(curl).read()
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
            print("Lightning Invoice: " + c)
            dn = str(d['checking_id'])
            t.sleep(10)
            checkcurl = 'curl -X GET https://lnbits.com/api/v1/payments/' + dn + """ -H "X-Api-Key: 1d646820055e4e2da218e801eaacfc94" -H "Content-type: application/json" """
            rsh = os.popen(checkcurl).read()
            clear()
            blogo()
            nn = str(rsh)
            dd = json.loads(nn)
            db = dd['paid']
            if db == True:
                clear()
                blogo()
                tick()
                bitLN['NN'] = randrange(10000000)
                bitLN['pd'] = "PAID"
                pickle.dump(bitLN, open("lnpaySN.conf", "wb"))
                createFileConnLNPay()
                break
            else:
                continue

def aaccPPiOpenNode():
    bitLN = {"NN":"","pd":""}
    if os.path.isfile('opennodeSN.conf'): # Check if the file 'bclock.conf' is in the same folder
        bitData= pickle.load(open("opennodeSN.conf", "rb")) # Load the file 'bclock.conf'
        bitLN = bitData # Copy the variable pathv to 'path'
        APIOpenNode()
    else:
        qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        )
        curl = 'curl -X POST https://lnbits.com/api/v1/payments -d ' + "'{" + """"out": false, "amount": 100000, "memo": "OpenNode on PyBLOCK" """ + "}'" + """ -H "X-Api-Key: 1d646820055e4e2da218e801eaacfc94 " -H "Content-type: application/json" """
        sh = os.popen(curl).read()
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
            print("Lightning Invoice: " + c)
            dn = str(d['checking_id'])
            t.sleep(10)
            checkcurl = 'curl -X GET https://lnbits.com/api/v1/payments/' + dn + """ -H "X-Api-Key: 1d646820055e4e2da218e801eaacfc94" -H "Content-type: application/json" """
            rsh = os.popen(checkcurl).read()
            clear()
            blogo()
            nn = str(rsh)
            dd = json.loads(nn)
            db = dd['paid']
            if db == True:
                clear()
                blogo()
                tick()
                bitLN['NN'] = randrange(10000000)
                bitLN['pd'] = "PAID"
                pickle.dump(bitLN, open("opennodeSN.conf", "wb"))
                createFileConnOpenNode()
                break
            else:
                continue

def aaccPPiTippinMe():
    bitLN = {"NN":"","pd":""}
    if os.path.isfile('tippinme.conf'): # Check if the file 'bclock.conf' is in the same folder
        bitData= pickle.load(open("tippinme.conf", "rb")) # Load the file 'bclock.conf'
        bitLN = bitData # Copy the variable pathv to 'path'
        APITippinMe()
    else:
        loadFileTippinMe()
#--------------------------------- End Menu section -----------------------------------
#--------------------------------- Main Menu execution --------------------------------

def menuPI(menuWN):
    if menuWN == "A" or menuWN == "a":
        aaccPPiTippinMe()
    if menuWN == "B" or menuWN == "b":
        aaccPPiLNBits()
    if menuWN == "C" or menuWN == "c":
        aaccPPiLNPay()
    if menuWN == "D" or menuWN == "d":
        aaccPPiOpenNode()

def menuTippinMe(menuTM):
    if menuTM == "A" or menuTM == "a":
        tippinmeGetInvoice()
    if menuTM == "R" or menuTM == "r":
        APIMenu()

def menuOpenNode(menuOP):
    if menuOP == "A" or menuOP == "a":
        clear()
        prt()
        OpenNodecreatecharge()
    if menuOP == "B" or menuOP == "b":
        clear()
        prt()
        OpenNodeiniciatewithdrawal()
    if menuOP == "C" or menuOP == "c":
        clear()
        prt()
        OpenNodelistfunds()
    if menuOP == "D" or menuOP == "d":
        clear()
        prt()
        OpenNodeListPayments()
    if menuOP == "R" or menuOP == "r":
        APIMenu()

def menuLNPAY(menuNW):
    if menuNW == "A" or menuNW == "a":
        clear()
        prt()
        lnpayCreateInvoice()
    if menuNW == "B" or menuNW == "b":
        clear()
        prt()
        lnpayPayInvoice()
    if menuNW == "C" or menuNW == "c":
        clear()
        prt()
        lnpayGetBalance()
    if menuNW == "D" or menuNW == "d":
        clear()
        prt()
        lnpayGetTransactions()
    if menuNW == "E" or menuNW == "e":
        clear()
        prt()
        lnpayTransBWallets()
    if menuNW == "R" or menuNW == "r":
        APIMenu()

def menuLNBPI(menuLNQ):
    if menuLNQ == "A" or menuLNQ == "a":
        clear()
        prt()
        lnbitCreateNewInvoice()
    if menuLNQ == "B" or menuLNQ == "b":
        clear()
        prt()
        lnbitPayInvoice()
    if menuLNQ == "C" or menuLNQ == "c":
        clear()
        prt()
        lnbitCreatePayWall()
    if menuLNQ == "D" or menuLNQ == "d":
        clear()
        prt()
        lnbitDeletePayWall()
    if menuLNQ == "E" or menuLNQ == "e":
        clear()
        prt()
        lnbitListPawWall()
    if menuLNQ == "R" or menuLNQ == "r":
        APIMenu()

def menuA(menuS): #Execution of the Main Menu options
    if menuS == "A" or menuS == "a":
        artist()
    elif menuS == "B" or menuS == "b":
        while True:
            try:
                clear()
                close()
                getblock()
                tmp()
            except:
                break
                menuSelection()
    elif menuS == "C" or menuS == "c":
        clear()
        prt()
        getgenesis()
        a = input("Do you want to return to the Main Menu? Y/n: ")
        if a == "Y" or a == "y":
            menuSelection()
        else:
            b = input("Do you want to exit? Y/n: ")
            if b == "Y" or b == "y":
                os._exit(0)
                apisnd.close()
                donation.close()
                clone.close()
                logos.close()
                feed.close()
                sysinf.close()
                nodeconnection.close()
                exit()
            else:
                menuSelection()
    elif menuS == "D" or menuS == "d":
        clear()
        prt()
        readHexBlock()
        while True:
            r = input("Do you want to continue decoding? Y/n: ")
            if r == "Y" or r == "y":
                clear()
                prt()
                readHexBlock()
            else:
                break
                menuSelection()
    elif menuS == "E" or menuS == "e":
        clear()
        prt()
        readHexTx()
        while True:
            r = input("Do you want to continue decoding? Y/n: ")
            if r == "Y" or r == "y":
                clear()
                prt()
                sysinfo()
                readHexTx()
            else:
                break
                menuSelection()
    elif menuS == "F" or menuS == "f":
        getrawtx()
    elif menuS == "H" or menuS == "h":
        advanceMenu()
    elif menuS == "L" or menuS == "l":
        clear()
        prt()
        menuSelectionLN()
    elif menuS == "Q" or menuS == "q":
        os._exit(0)
        apisnd.close()
        donation.close()
        clone.close()
        logos.close()
        feed.close()
        sysinf.close()
        nodeconnection.close()
        exit()
    elif menuS == "S" or menuS == "s":
        clear()
        prt()
        satnodeMenu()
    elif menuS == "G" or menuS == "g":
        nodeinfo()
    elif menuS == "P" or menuS == "p":
        APIMenu()
    elif menuS == "X" or menuS == "x":
        dnt()
    elif menuS == "T" or menuS == "t": #Test feature fast access
        print("This is a test access. \n")
        screensv()

def menuRemote(menuS): #Execution of the Main Menu options
    if menuS == "A" or menuS == "a":
        while True:
            try:
                clear()
                close()
                remotegetblock()
                tmp()
            except:
                break
                menuUserConn()
    elif menuS == "B" or menuS == "b":
        while True:
            try:
                clear()
                close()
                remotegetblockcount()
                tmp()
            except:
                break
                menuUserConn()
    elif menuS == "H" or menuS == "h":
        remoteadvanceMenu()
    elif menuS == "L" or menuS == "l":
        clear()
        prt()
        menuSelectionLN()
    elif menuS == "Q" or menuS == "q":
        os._exit(0)
        apisnd.close()
        donation.close()
        clone.close()
        logos.close()
        feed.close()
        sysinf.close()
        nodeconnection.close()
        exit()
    elif menuS == "S" or menuS == "s":
        clear()
        prt()
        satnodeMenu()
    elif menuS == "P" or menuS == "p":
        APIMenu()
    elif menuS == "G" or menuS == "g":
        nodeinfo()
    elif menuS == "X" or menuS == "x":
        dnt()
    elif menuS == "T" or menuS == "t": #Test feature fast access
        print("This is a test access. \n")
        screensv()
#------------------------------------------REMOTE
def menuLN(menuLL):
    if menuLL == "I" or menuLL == "i":
        clear()
        prt()
        getnewinvoice()
    elif menuLL == "P" or menuLL == "p":
        clear()
        prt()
        payinvoice()
    elif menuLL == "Q" or menuLL == "q":
        clear()
        prt()
        channelbalance()
    elif menuLL == "L" or menuLL == "l":
        clear()
        prt()
        listinvoice()
    elif menuLL == "X" or menuLL == "x":
        clear()
        prt()
        listonchaintxs()
    elif menuLL == "C" or menuLL == "c":
        clear()
        prt()
        channels()
    elif menuLL == "B" or menuLL == "b":
        clear()
        prt()
        getnewaddress()
    elif menuLL == "N" or menuLL == "n":
        clear()
        prt()
        getinfo()
    elif menuLL == "O" or menuLL == "o":
        clear()
        prt()
        balanceOC()
    elif menuLL == "R" or menuLL == "r":
        menuUserConn()

#------------------------------------------END REMOTE

#------------------------------------------LOCAL
def menuLNlocal(menuLL):
    if menuLL == "I" or menuLL == "i":
        clear()
        prt()
        localaddinvoice()
    elif menuLL == "P" or menuLL == "p":
        clear()
        prt()
        localpayinvoice()
    elif menuLL == "Q" or menuLL == "q":
        clear()
        prt()
        localchannelbalance()
    elif menuLL == "L" or menuLL == "l":
        clear()
        prt()
        locallistinvoices()
    elif menuLL == "X" or menuLL == "x":
        clear()
        prt()
        locallistchaintxns()
    elif menuLL == "C" or menuLL == "c":
        clear()
        prt()
        locallistchannels()
    elif menuLL == "B" or menuLL == "b":
        clear()
        prt()
        localnewaddress()
    elif menuLL == "N" or menuLL == "n":
        clear()
        prt()
        localgetinfo()
    elif menuLL == "O" or menuLL == "o":
        clear()
        prt()
        localbalanceOC()
    elif menuLL == "W" or menuLL == "w":
        clear()
        prt()
        localgetnetworkinfo()
    elif menuLL == "J" or menuLL == "j":
        while True:
            try:
                clear()
                prt()
                sysinfo()
                close()
                consoleLN()
                t.sleep(5)
            except:
                break
                menu()
    elif menuLL == "K" or menuLL == "k":
        clear()
        prt()
        localkeysend()
    elif menuLL == "R" or menuLL == "r":
        menuSelection()

#------------------------------------------END LOCAL

def menuB(menuR): # Advanced access Menu
    if menuR == "A" or menuR == "a":
        while True:
            try:
                clear()
                prt()
                sysinfo()
                close()
                console()
                t.sleep(5)
            except:
                break
                advanceMenu()
    elif menuR == "B" or menuR == "b":
        while True:
            try:
                clear()
                prt()
                close()
                logoA()
                tmp()
                clear()
                prt()
                close()
                logoB()
                tmp()
                clear()
                prt()
                close()
                logoC()
                tmp()
            except:
                break
                advanceMenu()
    elif menuR == "C" or menuR == "c":
        while True:
            try:
                clear()
                prt()
                sysinfo()
                close()
                decodeQR()
                t.sleep(50)
            except:
                break
                advanceMenu()
    elif menuR == "S" or menuR == "s":
        while True:
            try:
                clear()
                prt()
                close()
                sysinfoDetail()
                t.sleep(1)
            except:
                break
                advanceMenu()
    elif menuR == "R" or menuR == "r":
        try:
            menuSelection()
        except:
            os._exit(0)
            apisnd.close()
            donation.close()
            clone.close()
            logos.close()
            feed.close()
            sysinf.close()
            exit()

def menuBA(menuR): # Advanced access Menu
    if menuR == "A" or menuR == "a":
        while True:
            try:
                clear()
                prt()
                sysinfo()
                close()
                remoteconsole()
                t.sleep(5)
            except:
                break
                advanceMenu()
    elif menuR == "B" or menuR == "b":
        while True:
            try:
                clear()
                prt()
                close()
                logoA()
                tmp()
                clear()
                prt()
                close()
                logoB()
                tmp()
                clear()
                prt()
                close()
                logoC()
                tmp()
            except:
                break
                advanceMenu()
    elif menuR == "C" or menuR == "c":
        while True:
            try:
                clear()
                prt()
                sysinfo()
                close()
                decodeQR()
                t.sleep(50)
            except:
                break
                advanceMenu()
    elif menuR == "S" or menuR == "s":
        while True:
            try:
                clear()
                prt()
                close()
                sysinfoDetail()
                t.sleep(1)
            except:
                break
                advanceMenu()
    elif menuR == "R" or menuR == "r":
        try:
            menuSelection()
        except:
            os._exit(0)
            apisnd.close()
            donation.close()
            clone.close()
            logos.close()
            feed.close()
            sysinf.close()
            exit()

def menuC(menuO): # Donation access Menu
    if menuO == "A" or menuO == "a":
        dntDev()
    elif menuO == "B" or menuO == "b":
        dntTst()
    elif menuO == "R" or menuO == "r":
        menuSelection()

def menuD(menuN): # Satnode access Menu
    if menuN == "A" or menuN == "a":
        satnode()
    elif menuN == "B" or menuN == "b":
        readFile()
    elif menuN == "S" or menuN == "s":
        try:
            close()
            message = input("\n\033[0;37;40mYour message it's a \033[1;34;40mF\033[0;37;40mile or a plain \033[1;32;40mT\033[0;37;40mext? \033[1;34;40mF\033[0;37;40m/\033[1;32;40mT\033[0;37;40m: ")
            if message == "F" or message == "f":
                try:
                    clear()
                    prt()
                    close()
                    apisenderFile()
                    t.sleep(30)
                    menuSelection()
                except:
                    menuSelection()
            elif message == "T" or message == "t":
                try:
                    clear()
                    prt()
                    close()
                    apisender()
                    t.sleep(30)
                    menuSelection()
                except:
                    menuSelection()
        except:
            menuSelection()
    elif menuN == "C" or menuN == "c":
        print("\n\t This only will work on Linux or Unix systems.\n")
        a = input("Do we continue? Y/n: ")
        if a == "Y" or a == "y":
            gitclone()
        else:
            menuSelection()
    elif menuN == "D" or menuN == "d":
        menuSelection()

def menuE(menuQ): # Dev Donation access Menu
    if menuQ == "A" or menuQ == "a":
        try:
            clear()
            prt()
            close()
            donationPN()
            t.sleep(50)
            menuSelection()
        except:
            menuSelection()
    elif menuQ == "B" or menuQ == "b":
        try:
            clear()
            prt()
            close()
            donationAddr()
            t.sleep(50)
            menuSelection()
        except:
            menuSelection()
    elif menuQ == "C" or menuQ == "c":
        try:
            clear()
            prt()
            close()
            donationLN()
            t.sleep(50)
            menuSelection()
        except:
            menuSelection()
    elif menuQ == "R" or menuQ == "r":
        menuSelection()

def menuF(menuV): # Tester Donation access Menu
    if menuV == "A" or menuV == "a":
        try:
            clear()
            prt()
            close()
            donationAddrTst()
            t.sleep(50)
            menuSelection()
        except:
            menuSelection()
    elif menuV == "B" or menuV == "b":
        try:
            clear()
            prt()
            close()
            donationLNTst()
            t.sleep(50)
            menuSelection()
        except:
            menuSelection()
    elif menuV == "R" or menuV == "r":
        menuSelection()

#--------------------------------- End Main Menu execution --------------------------------

while True: # Loop
    clear()
    path = {"ip_port":"", "rpcuser":"", "rpcpass":"", "bitcoincli":""}

    if os.path.isfile('bclock.conf') or os.path.isfile('blnclock.conf'): # Check if the file 'bclock.conf' is in the same folder
        pathv = pickle.load(open("bclock.conf", "rb")) # Load the file 'bclock.conf'
        path = pathv # Copy the variable pathv to 'path'
        menuSelection()
    else:
        prt()
        print("Welcome to \033[1;31;40mPyBLOCK\033[0;37;40m\n\n")
        print("\n\tIf you are going to use your local node leave IP:PORT/USER/PASSWORD in blank.\n")
        path['ip_port'] = "http://{}".format(input("Insert IP:PORT to access your remote Bitcoin-Cli node: "))
        path['rpcuser'] = input("RPC User: ")
        path['rpcpass'] = input("RPC Password: ")
        print("\n\tLocal Bitcoin Core Node connection.\n")
        path['bitcoincli']= input("Insert the Path to Bitcoin-Cli: ")
        pickle.dump(path, open("bclock.conf", "wb"))
        menuSelection()
