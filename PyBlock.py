#Developer: Curly60e
#PyBLOCK its a clock of the Bitcoin blockchain.

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
from cfonts import render, say
from clone import *
from donation import *
from feed import *
from art import *
from logos import *
from sysinf import *
from pblogo import *
from apisnd import *
from ppi import *
from termcolor import colored, cprint
from nodeconnection import *
from terminal_matrix.matrix import *


version = "0.6.9"

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
    print("\n----------------------------------------------------------------------------------------------------")
    print("""
    Chain: {}
    Blocks: {}
    Best BlockHash: {}
    Difficulty: {}
    Verification Progress: {}
    Size on Disk: {}
    Pruned: {}
    """.format(d['chain'], d['blocks'], d['bestblockhash'], d['difficulty'], d['verificationprogress'], d['size_on_disk'], d['pruned']))
    print("----------------------------------------------------------------------------------------------------\n")

def getblockcount(): # get access to bitcoin-cli with the command getblockcount
    bitcoincli = " getblockcount"
    os.system(path['bitcoincli'] + bitcoincli)

def clear(): # clear the screen
    os.system('cls' if os.name=='nt' else 'clear')

def getgenesis(): # get and decode Genesis block
    bitcoincli = " getblock 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f 0 | xxd -r -p | hexyl -n 256"
    os.system(path['bitcoincli'] + bitcoincli)

def close():
    print("<<< Back Control + C.\n\n")

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
    blogo()

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

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.25)
#------------------------------------------------------

def connected(info): # here we complete the connection to the external node
    if info in ["Y", "y"]:
        clear()
        prt()
        print("\nAdd your node information\n")
        menuUserConn()
    else:
        menu()

def artist(): # here we convert the result of the command 'getblockcount' on a random art design
    custom = input("Do you want random designs? Y/n: ")
    if custom in ["Y", "y"]:
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
            if tx == "4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b":
                print("""\t\t\n\033[1;35;40mThis transaction it's the first one of the Bitcoin Blockchain on Block 0 by Satoshi Nakamoto.
You can decode that block in HEX and see what's inside.\033[0;37;40m""")
                t.sleep(10)
            else:
                bitcoincli = " getrawtransaction "
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

def runthenumbers():
    bitcoincli = " gettxoutsetinfo"
    os.system(path['bitcoincli'] + bitcoincli)
    input("\nContinue...")

#--------------------------------- End Hex Block Decoder Functions -------------------------------------

#--------------------------------- Menu section -----------------------------------

def menu(): #Main Menu
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m Menu
    Local Node
    Version {}

    \033[1;31;40mA.\033[0;37;40m Run PyBLOCK
    \033[1;32;40mB.\033[0;37;40m Show Blockchain information
    \033[1;32;40mC.\033[0;37;40m Show the Genesis Block
    \033[1;32;40mD.\033[0;37;40m Decode in HEX any block
    \033[1;32;40mE.\033[0;37;40m Decode in HEX any transaction
    \033[1;32;40mF.\033[0;37;40m Show confirmations from a transaction
    \033[1;32;40mG.\033[0;37;40m Run the Numbers
    \033[1;32;40mH.\033[0;37;40m Advanced
    \033[1;33;40mL.\033[0;37;40m Lightning Network
    \033[1;34;40mS.\033[0;37;40m SatNode
    \033[3;33;40mP.\033[0;37;40m Premium
    \033[1;32;40mN.\033[0;37;40m Settings
    \033[1;35;40mX.\033[0;37;40m Donate
    \033[1;33;40mQ.\033[0;37;40m Exit
    \n\n""".format(version, checkupdate()))
    menuA(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def menuUserConn(): #Menu before connection over ssh
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m Menu
    Remote Node RPC
    Version {}

    \033[1;31;40mA.\033[0;37;40m Run PyBLOCK
    \033[1;32;40mB.\033[0;37;40m Show Blockchain information
    \033[1;32;40mC.\033[0;37;40m Run the Numbers
    \033[1;32;40mH.\033[0;37;40m Advanced
    \033[1;33;40mL.\033[0;37;40m Lightning Network
    \033[1;34;40mS.\033[0;37;40m SatNode
    \033[3;33;40mP.\033[0;37;40m Premium
    \033[1;32;40mG.\033[0;37;40m Settings
    \033[1;35;40mX.\033[0;37;40m Donate
    \033[1;33;40mQ.\033[0;37;40m Exit
    \n\n""".format(version, checkupdate()))
    menuRemote(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def advanceMenu(): # Advanced Menu
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m Menu
    Version {}

    \033[1;32;40mA.\033[0;37;40m Bitconi-cli Console
    \033[1;32;40mB.\033[0;37;40m FunB
    \033[1;32;40mC.\033[0;37;40m Show QR from a Bitcoin Address
    \033[1;32;40mS.\033[0;37;40m Sysinfo
    \033[1;36;40mR.\033[0;37;40m Return Main Menu
    \n\n""".format(version))
    menuB(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def remoteadvanceMenu(): # Advanced Menu
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m Menu
    Version {}

    \033[1;32;40mA.\033[0;37;40m Bitconi-cli Console
    \033[1;32;40mB.\033[0;37;40m FunB
    \033[1;32;40mC.\033[0;37;40m Show QR from a Bitcoin Address
    \033[1;32;40mS.\033[0;37;40m Sysinfo
    \033[1;36;40mR.\033[0;37;40m Return Main Menu
    \n\n""".format(version))
    menuBA(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def dnt(): # Donation selection menu
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m Menu
    Version {}

    \033[1;32;40mA.\033[0;37;40m Developers Donation
    \033[1;32;40mB.\033[0;37;40m Testers Donation
    \033[1;36;40mR.\033[0;37;40m Return Main Menu
    \n\n""".format(version))
    menuC(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def dntDev(): # Dev Donation Menu
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m Menu
    Version {}

    \033[1;32;40mA.\033[0;37;40m PayNym
    \033[1;32;40mB.\033[0;37;40m Bitcoin Address
    \033[1;32;40mC.\033[0;37;40m Lightning Network
    \033[1;36;40mR.\033[0;37;40m Return Main Menu
    \n\n""".format(version))
    menuE(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def dntTst(): # Tester Donation Menu
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m Menu
    Version {}

    \033[1;32;40mA.\033[0;37;40m Bitcoin Address
    \033[1;32;40mB.\033[0;37;40m Lightning Network
    \033[1;36;40mR.\033[0;37;40m Return Main Menu
    \n\n""".format(version))
    menuF(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def satnodeMenu(): # Satnode Menu
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m Menu
    Version {}

    \033[1;32;40mA.\033[0;37;40m Start SatNode
    \033[1;32;40mB.\033[0;37;40m Feed
    \033[1;32;40mC.\033[0;37;40m Setup
    \033[1;34;40mS.\033[0;37;40m Send a Message to Space
    \033[1;36;40mD.\033[0;37;40m Return Main Menu
    \n\n""".format(version))
    menuD(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def menuLND():
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m Lightning Network Menu
    Remote node connection
    Version {}

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
    \n\n""".format(version))
    menuLN(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def settings4():
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m Settings Menu
    Remote node connection
    Version {}

    \033[1;32;40mA.\033[0;37;40m Change Logo Design
    \033[1;31;40mB.\033[0;37;40m Change Logo Colors
    \033[1;36;40mR.\033[0;37;40m Return Main Menu
    \n\n""".format(version))
    menuSettings(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def designQ():
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m Settings > Design Menu
    Remote node connection
    Version {}

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
    \033[1;36;40mR.\033[0;37;40m Return Main Menu
    \n\n""".format(version))
    menuDesign(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colors():
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m Settings > Colors Menu
    Remote node connection
    Version {}

    \033[1;32;40mA.\033[0;37;40m Front Color
    \033[1;31;40mB.\033[0;37;40m Back Color
    \033[1;31;40mC.\033[0;37;40m Rainbow
    \033[1;36;40mR.\033[0;37;40m Return Main Menu
    \n\n""".format(version))
    menuColors(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colorsSelectFront():
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m Settings > Colors > Front Color Menu
    Remote node connection
    Version {}

    \033[1;32;40mA.\033[0;37;40m Black
    \033[1;31;40mB.\033[0;37;40m Red
    \033[1;31;40mC.\033[0;37;40m Green
    \033[1;31;40mD.\033[0;37;40m Yellow
    \033[1;31;40mE.\033[0;37;40m Blue
    \033[1;31;40mF.\033[0;37;40m Magenta
    \033[1;31;40mG.\033[0;37;40m Cyan
    \033[1;31;40mH.\033[0;37;40m White
    \033[1;31;40mI.\033[0;37;40m Gray
    \033[1;36;40mR.\033[0;37;40m Return Main Menu
    \n\n""".format(version))
    menuColorsSelectFront(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colorsSelectBack():
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m Settings > Colors > Back Color Menu
    Remote node connection
    Version {}

    \033[1;32;40mA.\033[0;37;40m Black
    \033[1;31;40mB.\033[0;37;40m Red
    \033[1;31;40mC.\033[0;37;40m Green
    \033[1;31;40mD.\033[0;37;40m Yellow
    \033[1;31;40mE.\033[0;37;40m Blue
    \033[1;31;40mF.\033[0;37;40m Magenta
    \033[1;31;40mG.\033[0;37;40m Cyan
    \033[1;31;40mH.\033[0;37;40m White
    \033[1;31;40mI.\033[0;37;40m Gray
    \033[1;36;40mR.\033[0;37;40m Return Main Menu
    \n\n""".format(version))
    menuColorsSelectBack(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colorsSelectRainbow():
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m Settings > Colors > Rainbow Menu
    Remote node connection
    Version {}

    \033[1;32;40mA.\033[0;37;40m Start Color
    \033[1;31;40mB.\033[0;37;40m End Color
    \033[1;36;40mR.\033[0;37;40m Return Main Menu
    \n\n""".format(version))
    menuColorsSelectRainbow(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colorsSelectRainbowStart():
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m Settings > Colors > Rainbow Start Color Menu
    Remote node connection
    Version {}

    \033[1;32;40mA.\033[0;37;40m Black
    \033[1;31;40mB.\033[0;37;40m Red
    \033[1;31;40mC.\033[0;37;40m Green
    \033[1;31;40mD.\033[0;37;40m Yellow
    \033[1;31;40mE.\033[0;37;40m Blue
    \033[1;31;40mF.\033[0;37;40m Magenta
    \033[1;31;40mG.\033[0;37;40m Cyan
    \033[1;31;40mH.\033[0;37;40m White
    \033[1;31;40mI.\033[0;37;40m Gray
    \033[1;36;40mR.\033[0;37;40m Return Main Menu
    \n\n""".format(version))
    menuColorsSelectRainbowStart(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colorsSelectRainbowEnd():
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m Settings > Colors > Rainbow End Color Menu
    Remote node connection
    Version {}

    \033[1;32;40mA.\033[0;37;40m Black
    \033[1;31;40mB.\033[0;37;40m Red
    \033[1;31;40mC.\033[0;37;40m Green
    \033[1;31;40mD.\033[0;37;40m Yellow
    \033[1;31;40mE.\033[0;37;40m Blue
    \033[1;31;40mF.\033[0;37;40m Magenta
    \033[1;31;40mG.\033[0;37;40m Cyan
    \033[1;31;40mH.\033[0;37;40m White
    \033[1;31;40mI.\033[0;37;40m Gray
    \033[1;36;40mR.\033[0;37;40m Return Main Menu
    \n\n""".format(version))
    menuColorsSelectRainbowEnd(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def menuLNDLOCAL():
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m Lightning Network Menu
    Local node connection
    Version {}

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
    \n\n""".format(version))
    menuLNlocal(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def APIMenu():
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m API \033[1;34;40mPremium\033[0;37;40m Menu
    Version {}

    \033[1;32;40mA.\033[0;37;40m TippinMe   FREE
    \033[1;32;40mB.\033[0;37;40m Tallycoin  FREE
    \033[1;32;40mC.\033[0;37;40m Mempool    FREE
    \033[1;32;40mD.\033[0;37;40m LNBits     \033[3;35;40m{lnbitspaid}\033[0;37;40m
    \033[1;32;40mE.\033[0;37;40m LNPay      \033[3;35;40m{lnpaypaid}\033[0;37;40m
    \033[1;32;40mF.\033[0;37;40m OpenNode   \033[3;35;40m{opennodepaid}\033[0;37;40m
    \033[1;36;40mR.\033[0;37;40m Return Main Menu
    \n\n""".format(version,lnbitspaid = "PAID" if os.path.isfile("lnbitSN.conf") else "PREMIUM", lnpaypaid = "PAID" if os.path.isfile("lnpaySN.conf") else "PREMIUM", opennodepaid = "PAID" if os.path.isfile("opennodeSN.conf") else "PREMIUM"))
    menuPI(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def mempoolmenu():
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m Mempool.space \033[1;34;40mFree\033[0;37;40m Menu
    Version {}

    \033[1;32;40mA.\033[0;37;40m Blocks
    \033[1;32;40mB.\033[0;37;40m Recommended Fee
    \033[1;36;40mR.\033[0;37;40m Return Main Menu
    \n\n""".format(version))
    mempoolmenuS(input("\033[1;32;40mSelect option: \033[0;37;40m"))

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
    Version {}

    \033[1;32;40mA.\033[0;37;40m New Invoice
    \033[1;32;40mB.\033[0;37;40m Pay Invoice
    \033[1;32;40mC.\033[0;37;40m New PayWall
    \033[1;32;40mD.\033[0;37;40m Delete PayWall
    \033[1;32;40mE.\033[0;37;40m List PayWalls
    \033[1;36;40mR.\033[0;37;40m Return Main Menu
    \n\n""".format(version,bitLN['NN']))
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
    Version {}

    \033[1;32;40mA.\033[0;37;40m New Invoice
    \033[1;32;40mB.\033[0;37;40m Pay Invoice
    \033[1;32;40mC.\033[0;37;40m Wallet Balance
    \033[1;32;40mD.\033[0;37;40m List Invoices
    \033[1;32;40mE.\033[0;37;40m Transfer Between Wallets
    \033[1;36;40mR.\033[0;37;40m Return Main Menu
    \n\n""".format(version,bitLN['NN']))
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
    Version {}

    \033[1;32;40mA.\033[0;37;40m New Invoice
    \033[1;32;40mB.\033[0;37;40m Pay Invoice
    \033[1;32;40mC.\033[0;37;40m Wallet Balance
    \033[1;32;40mD.\033[0;37;40m List Payments
    \033[1;32;40mS.\033[0;37;40m Status
    \033[1;36;40mR.\033[0;37;40m Return Main Menu
    \n\n""".format(version,bitLN['NN']))
    menuOpenNode(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def APITippinMe():
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m TippinMe \033[1;34;40mFree\033[0;37;40m Menu
    Version {}

    \033[1;32;40mA.\033[0;37;40m New Invoice
    \033[1;36;40mR.\033[0;37;40m Return Main Menu
    \n\n""".format(version))
    menuTippinMe(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def APITallyCo():
    clear()
    prt()
    sysinfo()
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m TallyCoin \033[1;34;40mFree\033[0;37;40m Menu
    Version {}

    \033[1;32;40mA.\033[0;37;40m Get Payment
    \033[1;32;40mB.\033[0;37;40m Tip User
    \033[1;36;40mR.\033[0;37;40m Return Main Menu
    \n\n""".format(version))
    menuTallyCo(input("\033[1;32;40mSelect option: \033[0;37;40m"))

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
    try:
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
            bitLN['NN'] = randrange(10000000)
            curl = 'curl -X POST https://lnbits.com/api/v1/payments -d ' + "'{" + """"out": false, "amount": 100000, "memo": "LNBits on PyBLOCK {}" """.format(bitLN['NN']) + "}'" + """ -H "X-Api-Key: 1d646820055e4e2da218e801eaacfc94 " -H "Content-type: application/json" """
            sh = os.popen(curl).read()
            clear()
            prt()
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
                if db is True:
                    clear()
                    blogo()
                    tick()
                    bitLN['pd'] = "PAID"
                    pickle.dump(bitLN, open("lnbitSN.conf", "wb"))
                    createFileConnLNBits()
                    break
                else:
                    continue

    except:
        clear()
        blogo()
        print("\n\tSERIAL NUMBER NOT FOUND\n")
        input("Continue...")

def aaccPPiLNPay():
    try:
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
            bitLN['NN'] = randrange(10000000)
            curl = 'curl -X POST https://lnbits.com/api/v1/payments -d ' + "'{" + """"out": false, "amount": 100000, "memo": "LNPay on PyBLOCK {}" """.format(bitLN['NN']) + "}'" + """ -H "X-Api-Key: 1d646820055e4e2da218e801eaacfc94 " -H "Content-type: application/json" """
            sh = os.popen(curl).read()
            clear()
            prt()
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
                if db is True:
                    clear()
                    blogo()
                    tick()
                    bitLN['pd'] = "PAID"
                    pickle.dump(bitLN, open("lnpaySN.conf", "wb"))
                    createFileConnLNPay()
                    break
                else:
                    continue

    except:
        clear()
        blogo()
        print("\n\tSERIAL NUMBER NOT FOUND\n")
        input("Continue...")

def aaccPPiOpenNode():
    try:
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
            bitLN['NN'] = randrange(10000000)
            curl = 'curl -X POST https://lnbits.com/api/v1/payments -d ' + "'{" + """"out": false, "amount": 100000, "memo": "OpenNode on PyBLOCK {}" """.format(bitLN['NN']) + "}'" + """ -H "X-Api-Key: 1d646820055e4e2da218e801eaacfc94 " -H "Content-type: application/json" """
            sh = os.popen(curl).read()
            clear()
            prt()
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
                if db is True:
                    clear()
                    blogo()
                    tick()
                    bitLN['pd'] = "PAID"
                    pickle.dump(bitLN, open("opennodeSN.conf", "wb"))
                    createFileConnOpenNode()
                    break
                else:
                    continue

    except:
        clear()
        blogo()
        print("\n\tSERIAL NUMBER NOT FOUND\n")
        input("Continue...")

def aaccPPiTippinMe():
    if os.path.isfile('tippinme.conf'): # Check if the file 'bclock.conf' is in the same folder
        APITippinMe()
    else:
        createFileTippinMe()

def aaccPPiTallyCo():
    if os.path.isfile('tallyco.conf'): # Check if the file 'bclock.conf' is in the same folder
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
        print("\n---------------------------------------------------")
        q = print("\n    \033[1;31;40mNew version available\033[0;37;40m > Press U to Upgrade\n")
        print("---------------------------------------------------")

def upgrade():
    gitfetch = "git fetch"
    gitchekcout = "git checkout origin/master -- PyBlock.py ppi.py pblogo.py sysinf.py apisnd.py clone.py donation.py feed.py logos.py nodeconnection.py"
    clear()
    blogo()
    b = os.popen(gitfetch).read()
    a = os.popen(gitchekcout).read()
    print(b)
    print(a)
    print("\n---------------------------------------------------")
    print("\n\t\033[1;31;40mYou'll need to restart PyBLOCK\033[0;37;40m\n")
    print("---------------------------------------------------\n")
    input("Continue...")

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
        pickle.dump(settings, open("pyblocksettings.conf", "wb"))
    except:
        settings4()

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
        pickle.dump(settings, open("pyblocksettings.conf", "wb"))
    except:
        settings4()


#--------------------------------- End Menu section -----------------------------------
#--------------------------------- Main Menu execution --------------------------------

def menuSettings(menuSTT):
    if menuSTT in ["A", "a"]:
        clear()
        prt()
        designQ()
    elif menuSTT in ["B", "b"]:
        clear()
        prt()
        colors()

def menuColors(menuCLS):
    if menuCLS in ["A", "a"]:
        colorsSelectFront()
    elif menuCLS in ["B", "b"]:
        colorsSelectBack()
    elif menuCLS in ["C", "c"]:
        colorsSelectRainbow()
    elif menuCLS in ["F", "f"]:
        colors()

def menuColorsSelectRainbow(menuRF):
    if menuRF in ["A", "a"]:
        colorsSelectRainbowStart()
    elif menuRF in ["B", "b"]:
        colorsSelectRainbowEnd()
    elif menuRF in ["F", "f"]:
        colors()

def menuColorsSelectRainbowEnd(menuCF):
    if menuCF in ["A", "a"]:
        clear()
        prt()
        settings["colorB"] = "black"
        testlogoRB()
    elif menuCF in ["B", "b"]:
        clear()
        prt()
        settings["colorB"] = "red"
        testlogoRB()
    elif menuCF in ["C", "c"]:
        clear()
        prt()
        settings["colorB"] = "green"
        testlogoRB()
    elif menuCF in ["D", "d"]:
        clear()
        prt()
        settings["colorB"] = "yellow"
        testlogo()
    elif menuCF in ["E", "e"]:
        clear()
        prt()
        settings["colorB"] = "blue"
        testlogoRB()
    elif menuCF in ["F", "f"]:
        clear()
        prt()
        settings["colorB"] = "magenta"
        testlogoRB()
    elif menuCF in ["G", "g"]:
        clear()
        prt()
        settings["colorB"] = "cyan"
        testlogoRB()
    elif menuCF in ["H", "h"]:
        clear()
        prt()
        settings["colorB"] = "white"
        testlogoRB()
    elif menuCF in ["I", "i"]:
        clear()
        prt()
        settings["colorB"] = "gray"
        testlogoRB()
    elif menuCF in ["R", "r"]:
        colors()

def menuColorsSelectRainbowStart(menuCF):
    if menuCF in ["A", "a"]:
        clear()
        prt()
        settings["colorA"] = "black"
        testlogoRB()
    elif menuCF in ["B", "b"]:
        clear()
        prt()
        settings["colorA"] = "red"
        testlogoRB()
    elif menuCF in ["C", "c"]:
        clear()
        prt()
        settings["colorA"] = "green"
        testlogoRB()
    elif menuCF in ["D", "d"]:
        clear()
        prt()
        settings["colorA"] = "yellow"
        testlogoRB()
    elif menuCF in ["E", "e"]:
        clear()
        prt()
        settings["colorA"] = "blue"
        testlogoRB()
    elif menuCF in ["F", "f"]:
        clear()
        prt()
        settings["colorA"] = "magenta"
        testlogoRB()
    elif menuCF in ["G", "g"]:
        clear()
        prt()
        settings["colorA"] = "cyan"
        testlogoRB()
    elif menuCF in ["H", "h"]:
        clear()
        prt()
        settings["colorA"] = "white"
        testlogoRB()
    elif menuCF in ["I", "i"]:
        clear()
        prt()
        settings["colorA"] = "gray"
        testlogoRB()
    elif menuCF in ["R", "r"]:
        colors()

def menuColorsSelectBack(menuCF):
    if menuCF in ["A", "a"]:
        clear()
        prt()
        settings["colorB"] = "black"
        testlogo()
    elif menuCF in ["B", "b"]:
        clear()
        prt()
        settings["colorB"] = "red"
        testlogo()
    elif menuCF in ["C", "c"]:
        clear()
        prt()
        settings["colorB"] = "green"
        testlogo()
    elif menuCF in ["D", "d"]:
        clear()
        prt()
        settings["colorB"] = "yellow"
        testlogo()
    elif menuCF in ["E", "e"]:
        clear()
        prt()
        settings["colorB"] = "blue"
        testlogo()
    elif menuCF in ["F", "f"]:
        clear()
        prt()
        settings["colorB"] = "magenta"
        testlogo()
    elif menuCF in ["G", "g"]:
        clear()
        prt()
        settings["colorB"] = "cyan"
        testlogo()
    elif menuCF in ["H", "h"]:
        clear()
        prt()
        settings["colorB"] = "white"
        testlogo()
    elif menuCF in ["I", "i"]:
        clear()
        prt()
        settings["colorB"] = "gray"
        testlogo()
    elif menuCF in ["R", "r"]:
        colors()

def menuColorsSelectFront(menuCF):
    if menuCF in ["A", "a"]:
        clear()
        prt()
        settings["colorA"] = "black"
        testlogo()
    elif menuCF in ["B", "b"]:
        clear()
        prt()
        settings["colorA"] = "red"
        testlogo()
    elif menuCF in ["C", "c"]:
        clear()
        prt()
        settings["colorA"] = "green"
        testlogo()
    elif menuCF in ["D", "d"]:
        clear()
        prt()
        settings["colorA"] = "yellow"
        testlogo()
    elif menuCF in ["E", "e"]:
        clear()
        prt()
        settings["colorA"] = "blue"
        testlogo()
    elif menuCF in ["F", "f"]:
        clear()
        prt()
        settings["colorA"] = "magenta"
        testlogo()
    elif menuCF in ["G", "g"]:
        clear()
        prt()
        settings["colorA"] = "cyan"
        testlogo()
    elif menuCF in ["H", "h"]:
        clear()
        prt()
        settings["colorA"] = "white"
        testlogo()
    elif menuCF in ["I", "i"]:
        clear()
        prt()
        settings["colorA"] = "gray"
        testlogo()
    elif menuCF in ["R", "r"]:
        colors()

def menuDesign(menuDSN):
    if menuDSN in ["A", "a"]:
        clear()
        prt()
        settings["design"] = "block"
        testlogo()
    elif menuDSN in ["B", "b"]:
        clear()
        prt()
        settings['design'] = "slick"
        testlogo()
    elif menuDSN in ["C", "c"]:
        clear()
        prt()
        settings['design'] = "tiny"
        testlogo()
    elif menuDSN in ["D", "d"]:
        clear()
        prt()
        settings['design'] = "grid"
        testlogo()
    elif menuDSN in ["E", "e"]:
        clear()
        prt()
        settings['design'] = "pallet"
        testlogo()
    elif menuDSN in ["F", "f"]:
        clear()
        prt()
        settings['design'] = "shade"
        testlogo()
    elif menuDSN in ["G", "g"]:
        clear()
        prt()
        settings['design'] = "chrome"
        testlogo()
    elif menuDSN in ["H", "h"]:
        clear()
        prt()
        settings['design'] = "simple"
        testlogo()
    elif menuDSN in ["I", "i"]:
        clear()
        prt()
        settings['design'] = "simpleBlock"
        testlogo()
    elif menuDSN in ["J", "j"]:
        clear()
        prt()
        settings['design'] = "3d"
        testlogo()
    elif menuDSN in ["K", "k"]:
        clear()
        prt()
        settings['design'] = "simple3d"
        testlogo()
    elif menuDSN in ["L", "l"]:
        clear()
        prt()
        settings['design'] = "huge"
        testlogo()

def menuPI(menuWN):
    if menuWN in ["A", "a"]:
        aaccPPiTippinMe()
    elif menuWN in ["B", "b"]:
        aaccPPiTallyCo()
    elif menuWN in ["C", "c"]:
        mempoolmenu()
    elif menuWN in ["D", "d"]:
        aaccPPiLNBits()
    elif menuWN in ["E", "e"]:
        aaccPPiLNPay()
    elif menuWN in ["F", "f"]:
        aaccPPiOpenNode()

def mempoolmenuS(menuMem):
    if menuMem in ["A", "a"]:
        blocks()
    elif menuMem in ["B", "b"]:
        fee()
    elif menuMem in ["R", "r"]:
        APIMenu()

def menuTallyCo(menuTLC):
    if menuTLC in ["A", "a"]:
        tallycoGetPayment()
    elif menuTLC in ["B", "b"]:
        tallycoDonateid()
    elif menuTLC in ["R", "r"]:
        APIMenu()

def menuTippinMe(menuTM):
    if menuTM in ["A", "a"]:
        tippinmeGetInvoice()
    elif menuTM in ["R", "r"]:
        APIMenu()

def menuOpenNode(menuOP):
    if menuOP in ["A", "a"]:
        clear()
        prt()
        OpenNodecreatecharge()
    elif menuOP in ["B", "b"]:
        clear()
        prt()
        OpenNodeiniciatewithdrawal()
    elif menuOP in ["C", "c"]:
        clear()
        prt()
        OpenNodelistfunds()
    elif menuOP in ["D", "d"]:
        clear()
        prt()
        OpenNodeListPayments()
    elif menuOP in ["S", "s"]:
        clear()
        prt()
        OpenNodeCheckStatus()
    elif menuOP in ["R", "r"]:
        APIMenu()

def menuLNPAY(menuNW):
    if menuNW in ["A", "a"]:
        clear()
        prt()
        lnpayCreateInvoice()
    elif menuNW in ["B", "b"]:
        clear()
        prt()
        lnpayPayInvoice()
    elif menuNW in ["C", "c"]:
        clear()
        prt()
        lnpayGetBalance()
    elif menuNW in ["D", "d"]:
        clear()
        prt()
        lnpayGetTransactions()
    elif menuNW in ["E", "e"]:
        clear()
        prt()
        lnpayTransBWallets()
    elif menuNW in ["R", "r"]:
        APIMenu()

def menuLNBPI(menuLNQ):
    if menuLNQ in ["A", "a"]:
        clear()
        prt()
        lnbitCreateNewInvoice()
    elif menuLNQ in ["B", "b"]:
        clear()
        prt()
        lnbitPayInvoice()
    elif menuLNQ in ["C", "c"]:
        clear()
        prt()
        lnbitCreatePayWall()
    elif menuLNQ in ["D", "d"]:
        clear()
        prt()
        lnbitDeletePayWall()
    elif menuLNQ in ["E", "e"]:
        clear()
        prt()
        lnbitListPawWall()
    elif menuLNQ in ["R", "r"]:
        APIMenu()

def menuA(menuS): #Execution of the Main Menu options
    if menuS in ["A", "a"]:
        artist()
    elif menuS in ["B", "b"]:
        while True:
            try:
                clear()
                close()
                getblock()
                tmp()
            except:
                break
                menu()
    elif menuS in ["C", "c"]:
        clear()
        prt()
        getgenesis()
        a = input("Do you want to return to the Main Menu? Y/n: ")
        if a in ["Y", "y"]:
            menuSelection()
        else:
            b = input("Do you want to exit? Y/n: ")
            if b in ["Y", "y"]:
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
    elif menuS in ["D", "d"]:
        clear()
        prt()
        readHexBlock()
        while True:
            r = input("Do you want to continue decoding? Y/n: ")
            if r in ["Y", "y"]:
                clear()
                prt()
                readHexBlock()
            else:
                break
    elif menuS in ["E", "e"]:
        clear()
        prt()
        readHexTx()
        while True:
            r = input("Do you want to continue decoding? Y/n: ")
            if r in ["Y", "y"]:
                clear()
                prt()
                sysinfo()
                readHexTx()
            else:
                break
    elif menuS in ["F", "f"]:
        getrawtx()
    elif menuS in ["G", "g"]:
        clear()
        prt()
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
    elif menuS in ["H", "h"]:
        advanceMenu()
    elif menuS in ["L", "l"]:
        clear()
        prt()
        menuSelectionLN()
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
    elif menuS in ["S", "s"]:
        clear()
        prt()
        satnodeMenu()
    elif menuS in ["P", "p"]:
        APIMenu()
    elif menuS in ["X", "x"]:
        dnt()
    elif menuS in ["U", "u"]:
        upgrade()
    elif menuS in ["N", "n"]:
        settings4()
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

def menuRemote(menuS): #Execution of the Main Menu options
    if menuS in ["A", "a"]:
        while True:
            try:
                clear()
                close()
                remotegetblock()
                tmp()
            except:
                break
                menuUserConn()
    elif menuS in ["B", "b"]:
        while True:
            try:
                clear()
                close()
                remotegetblockcount()
                tmp()
            except:
                break

    elif menuS in ["C", "c"]:
        clear()
        prt()
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
    elif menuS in ["H", "h"]:
        remoteadvanceMenu()
    elif menuS in ["L", "l"]:
        clear()
        prt()
        menuSelectionLN()
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
    elif menuS in ["S", "s"]:
        clear()
        prt()
        satnodeMenu()
    elif menuS in ["P", "p"]:
        APIMenu()
    elif menuS in ["X", "x"]:
        dnt()
    elif menuS in ["U", "u"]:
        upgrade()
    elif menuS in ["G", "g"]:
        settings4()
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
#------------------------------------------REMOTE
def menuLN(menuLL):
    if menuLL in ["I", "i"]:
        clear()
        prt()
        getnewinvoice()
    elif menuLL in ["P", "p"]:
        clear()
        prt()
        payinvoice()
    elif menuLL in ["Q", "q"]:
        clear()
        prt()
        channelbalance()
    elif menuLL in ["L", "l"]:
        clear()
        prt()
        listinvoice()
    elif menuLL in ["X", "x"]:
        clear()
        prt()
        listonchaintxs()
    elif menuLL in ["C", "c"]:
        clear()
        prt()
        channels()
    elif menuLL in ["B", "b"]:
        clear()
        prt()
        getnewaddress()
    elif menuLL in ["N", "n"]:
        clear()
        prt()
        getinfo()
    elif menuLL in ["O", "o"]:
        clear()
        prt()
        balanceOC()
    elif menuLL in ["R", "r"]:
        menuUserConn()

#------------------------------------------END REMOTE

#------------------------------------------LOCAL
def menuLNlocal(menuLL):
    if menuLL in ["I", "i"]:
        clear()
        prt()
        localaddinvoice()
    elif menuLL in ["P", "p"]:
        clear()
        prt()
        localpayinvoice()
    elif menuLL in ["Q", "q"]:
        clear()
        prt()
        localchannelbalance()
    elif menuLL in ["L", "l"]:
        clear()
        prt()
        locallistinvoices()
    elif menuLL in ["X", "x"]:
        clear()
        prt()
        locallistchaintxns()
    elif menuLL in ["C", "c"]:
        clear()
        prt()
        locallistchannels()
    elif menuLL in ["B", "b"]:
        clear()
        prt()
        localnewaddress()
    elif menuLL in ["N", "n"]:
        clear()
        prt()
        localgetinfo()
    elif menuLL in ["O", "o"]:
        clear()
        prt()
        localbalanceOC()
    elif menuLL in ["W", "w"]:
        clear()
        prt()
        localgetnetworkinfo()
    elif menuLL in ["J", "j"]:
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
    elif menuLL in ["K", "k"]:
        clear()
        prt()
        localkeysend()
    elif menuLL in ["R", "r"]:
        menuSelection()

#------------------------------------------END LOCAL

def menuB(menuR): # Advanced access Menu
    if menuR in ["A", "a"]:
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
    elif menuR in ["B", "b"]:
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
    elif menuR in ["C", "c"]:
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
    elif menuR in ["S", "s"]:
        while True:
            try:
                clear()
                prt()
                close()
                sysinfoDetail()
                t.sleep(1)
            except:
                break
    elif menuR in ["R", "r"]:
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
    if menuR in ["A", "a"]:
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
    elif menuR in ["B", "b"]:
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
    elif menuR in ["C", "c"]:
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
    elif menuR in ["S", "s"]:
        while True:
            try:
                clear()
                prt()
                close()
                sysinfoDetail()
                t.sleep(1)
            except:
                break
    elif menuR in ["R", "r"]:
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
    if menuO in ["A", "a"]:
        dntDev()
    elif menuO in ["B", "b"]:
        dntTst()
    elif menuO in ["R", "r"]:
        menuSelection()

def menuD(menuN): # Satnode access Menu
    if menuN in ["A", "a"]:
        satnode()
    elif menuN in ["B", "b"]:
        readFile()
    elif menuN in ["S", "s"]:
        try:
            close()
            message = input("\n\033[0;37;40mYour message it's a \033[1;34;40mF\033[0;37;40mile or a plain \033[1;32;40mT\033[0;37;40mext? \033[1;34;40mF\033[0;37;40m/\033[1;32;40mT\033[0;37;40m: ")
            if message in ["F", "f"]:
                try:
                    clear()
                    prt()
                    close()
                    apisenderFile()
                    t.sleep(30)
                    menuSelection()
                except:
                    menuSelection()
            elif message in ["T", "t"]:
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
    elif menuN in ["C", "c"]:
        print("\n\t This only will work on Linux or Unix systems.\n")
        a = input("Do we continue? Y/n: ")
        if a in ["Y", "y"]:
            gitclone()
        else:
            menuSelection()
    elif menuN in ["D", "d"]:
        menuSelection()

def menuE(menuQ): # Dev Donation access Menu
    if menuQ in ["A", "a"]:
        try:
            clear()
            prt()
            close()
            donationPN()
            t.sleep(50)
            menuSelection()
        except:
            menuSelection()
    elif menuQ in ["B", "b"]:
        try:
            clear()
            prt()
            close()
            donationAddr()
            t.sleep(50)
            menuSelection()
        except:
            menuSelection()
    elif menuQ in ["C", "c"]:
        try:
            clear()
            prt()
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
            prt()
            close()
            donationAddrTst()
            t.sleep(50)
            menuSelection()
        except:
            menuSelection()
    elif menuV in ["B", "b"]:
        try:
            clear()
            prt()
            close()
            donationLNTst()
            t.sleep(50)
            menuSelection()
        except:
            menuSelection()
    elif menuV in ["R", "r"]:
        menuSelection()

#--------------------------------- End Main Menu execution --------------------------------

settings = {"gradient":"", "design":"block", "colorA":"green", "colorB":"yellow"}
while True: # Loop
    clear()
    path = {"ip_port":"", "rpcuser":"", "rpcpass":"", "bitcoincli":""}

    if os.path.isfile('bclock.conf') or os.path.isfile('blnclock.conf'): # Check if the file 'bclock.conf' is in the same folder
        pathv = pickle.load(open("bclock.conf", "rb")) # Load the file 'bclock.conf'
        path = pathv # Copy the variable pathv to 'path'
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
