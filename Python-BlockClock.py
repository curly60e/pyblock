#Developer: Curly60e
#Python BlockClock its a clock of the Bitcoin blockchain.
#Version: 0.0.8.1

import os
import os.path
import time as t
import pickle
from donation import *
from art import *
from logos import *


def getblock(): # get access to bitcoin-cli with the command getblockchaininfo
    bitcoincli = " getblockchaininfo"
    os.system(path + bitcoincli)

def getblockcount(): # get access to bitcoin-cli with the command getblockcount
    bitcoincli = " getblockcount"
    os.system(path + bitcoincli)

def clear(): # clear the screen
    os.system('cls' if os.name=='nt' else 'clear')

def getgenesis(): # get and decode Genesis block 
    bitcoincli = " getblock 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f 0 | xxd -r -p | hexyl -n 256"
    os.system(path + bitcoincli)

def console(): # get into the console from bitcoin-cli
    print("\tThis is Bitcoin-cli's console. Type your respective commands you want to display.\n\n")
    while True:
        cle = input("console $>: ")
        lsd = os.popen(str(path + " " + cle)).read()
        print(lsd)

#-------------------From this line the program starts----------------------

def connected(info): # here we complete the connection to the external node
    if info == "Y" or info == "y":
        clear()
        prt()
        print("\nAdd your node information\n")
        menuUserConn()
    else:
        menu()
        
    
def nodeinfo():
    print("\nWARNING! This is not a safe method of connection. The best method is doing this locally.\n")
    connected(input("WARNING! Are you sure you want to connect to a node? Y/n: ")) # call 'connected' function to make the connection with the node information
    
    
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

def close():
    print("<<< Back to the Main Menu Press Control + C.\n\n")

def design():
    bitcoinclient = path + " getblockcount"
    block = os.popen(str(bitcoinclient)).read() # 'getblockcount' convert to string
    b = block 
    tprint(b, font="rnd-large")

#------------------------------------------- SSH connection external node --------------------------------------------

def userconn(): # All the connection to a remote node
    option = input("Select option: ")
    if option == "A" or option == "a": # Execution of the secondary Menu menuUserConn
        user = input("USER@NODE: ")
        s = input("Do you want to continue Y/n: ")
        if s == "Y" or s == "y":
            clear()
            c = input("Do you want to see custom design? Y/n: ")
            if c == "Y" or c == "y": 
                while True: # connection via ssh
                    try:
                        clear()
                        close()
                        sshb = "ssh " + user + " '" + "{}".format(path) + "'" + " getblockcount"
                        sshc = os.popen(str(sshb)).read()
                        sshd = sshc
                        tprint(sshd, font="rnd-large")
                        tmp()
                    except (KeyboardInterrupt, SystemExit):
                        menuUserConn()
                        raise
                else:
                    menu()        
            else:
                while True: # connection via ssh
                    try:
                        clear()
                        close()
                        sshb = "ssh " + user + " '" + "{}".format(path) + "'" + " getblockchaininfo"
                        os.system(sshb)
                        tmp()
                    except (KeyboardInterrupt, SystemExit):
                        menuUserConn()
                        raise
        else:
            menu()      
    elif option == "B" or option == "b": # Decode Block 0 on HEX for external node
        user = input("USER@NODE: ")
        while True:
            clear()
            prt()
            sshb = "ssh " + user + " '" + "{}".format(path) + "'" + " getblock 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f 0 | xxd -r -p | hexyl -n 256"
            os.system(sshb)
            a = input("Do you want to return to the Node Connection Menu? Y/n: ")
            if a == "Y" or a == "y":
                menuUserConn()
            else:
                b = input("Do you want to exit? Y/n: ")
                if b == "Y" or b == "y":
                    exit()
                else:
                    menuUserConn()  
            tmp()
    elif option == "C" or option == "c": # Block decoder to HEX for external node
        readHexBlockSsh()
        while True:
            m = input("Do you want to continue decoding? Y/n: ")
            if m == "Y" or m == "y":
                readHexBlockSsh()
            else:
                menuUserConn()  
    elif option == "D" or option == "d":
        readHexTXSsh()
        while True:
            m = input("Do you want to continue decoding? Y/n: ")
            if m == "Y" or m == "y":
                readHexTXSsh()
            else:
                menuUserConn()
    elif option == "R" or option == "r":
        menu()
        
#------------------------------------------- End SSH connection external node --------------------------------------------


#--------------------------------- Hex Block Decoder Functions -------------------------------------

def readHexBlock(): # Hex Decoder using Hexyl on local node
    hexa = input("Add the Block Hash you want to decode: ")
    blocknumber = input("Add the Block number: ")
    decodeBlock = path + " getblock {} {}".format(hexa, blocknumber) + " | xxd -r -p | hexyl -n 256"
    os.system(decodeBlock)
 
def readHexBlockSsh(): # Hex Decoder using Hexyl on an external node
    user = input("USER@NODE: ")
    clear()
    prt()
    hexa = input("Add the Block Hash you want to decode: ")
    blocknumber = input("Add the Block number: ")
    decodeBlock = "ssh " + user + " '" + "{}".format(path) + "'" +  " getblock {} {}".format(hexa, blocknumber) + " | xxd -r -p | hexyl -n 256"
    clear()
    prt()
    os.system(decodeBlock)
    
def readHexTx(): # Hex Decoder using Hexyl on an external node
    hexa = input("Add the Transaction ID. you want to decode: ")
    decodeTX = path + " getrawtransaction {}".format(hexa) + " | xxd -r -p | hexyl -n 256"
    os.system(decodeTX)
    
def readHexTXSsh(): # Hex Decoder using Hexyl on an external node
    user = input("USER@NODE: ")
    clear()
    prt()
    hexa = input("Add the Transaction ID. you want to decode: ")
    decodeTX = "ssh " + user + " '" + "{}".format(path) + "'" +  " getrawtransaction {}".format(hexa) + " | xxd -r -p | hexyl -n 256"
    clear()
    prt()
    os.system(decodeTX)
  
#--------------------------------- End Hex Block Decoder Functions -------------------------------------
 
#--------------------------------- Menu section -----------------------------------

def menu(): #Main Menu
    clear()
    prt()
    print("""\t\t
    Python BlockClock Menu
    Version 0.0.8.1
    
    A. Run BlockClock in your own node
    B. Show Blockchain information in your own node
    C. Show the Genesis Block
    D. Decode in HEX any block
    E. Decode in HEX any transaction
    F. Connect to an external node through SSH
    G. Advanced
    X. Donate
    Q. Exit
    \n\n""")
    menuA(input("Select option: "))
    
def menuUserConn(): #Menu before connection over ssh
    clear()
    prt()
    print("""\t\t
    Python BlockClock External Node Menu
    Version 0.0.8.1
    
    A. Run BlockClock in this external node 
    B. Show the Genesis Block
    C. Decode in HEX any block
    D. Decode in HEX any transaction
    R. Return Main Menu
    \n\n""")
    userconn()
    
def advanceMenu():
    clear()
    prt()
    print("""\t\t
    Python BlockClock Advance Menu
    Version 0.0.8.1
    
    A. Bitconi-cli Console
    B. FunB
    C. Show QR from a Bitcoin Address
    R. Return Main Menu
    \n\n""")
    menuB(input("Select option: "))

def dnt():
    clear()
    prt()
    print("""\t\t
    Python BlockClock Advance Menu
    Version 0.0.8.1
    
    A. PayNym
    B. Bitcoin Address
    C. Lightning Network
    D. Return Main Menu
    \n\n""")
    menuC(input("Select option: "))

#--------------------------------- End Menu section -----------------------------------
 
#--------------------------------- Main Menu execution --------------------------------

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
            except (KeyboardInterrupt, SystemExit):
                menu()
                raise
    elif menuS == "C" or menuS == "c":
        clear()
        prt()
        getgenesis()
        a = input("Do you want to return to the Main Menu? Y/n: ")
        if a == "Y" or a == "y":
            menu()
        else:
            b = input("Do you want to exit? Y/n: ")
            if b == "Y" or b == "y":
                exit()
            else:
                menu()
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
                menu()   
    elif menuS == "E" or menuS == "e":
        clear()
        prt()
        readHexTx()
        while True:
            r = input("Do you want to continue decoding? Y/n: ")
            if r == "Y" or r == "y":
                clear()
                prt()
                readHexTx()
            else:
                menu()       
    elif menuS == "F" or menuS == "f":
        nodeinfo()
    elif menuS == "Q" or menuS == "q":
        exit()
    elif menuS == "G" or menuS == "g":
        advanceMenu()
    elif menuS == "X" or menuS == "x":
        dnt()
        
def menuB(menuR):
    if menuR == "A" or menuR == "a":
        while True:
            try:
                clear()
                prt()
                close()
                console()
                t.sleep(5)
            except (KeyboardInterrupt, SystemExit):
                advanceMenu()
                raise
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
            except (KeyboardInterrupt, SystemExit):
                advanceMenu()
                raise
    elif menuR == "C" or menuR == "c":
        while True:
            try:
                clear()
                prt()
                close()
                decodeQR()
                t.sleep(50)
            except (KeyboardInterrupt, SystemExit):
                advanceMenu()
                raise         
    elif menuR == "R" or menuR == "r":
        menu()
        
def menuC(menuO):
    if menuO == "A" or menuO == "a":                
        try:
            clear()
            prt()
            close()
            donationPN()
            t.sleep(50)
            menu()
        except (KeyboardInterrupt, SystemExit):
            menu()
            raise
    elif menuO == "B" or menuO == "b":
        try:
            clear()
            prt()
            close()
            donationAddr()
            t.sleep(50)
            menu()
        except (KeyboardInterrupt, SystemExit):
            menu()
            raise
    elif menuO == "C" or menuO == "c":
        try:
            clear()
            prt()
            close()
            donationLN()
            t.sleep(50)
            menu()
        except (KeyboardInterrupt, SystemExit):
            menu()
            raise
    elif menuO == "D" or menuO == "d":
        menu()
#--------------------------------- End Main Menu execution --------------------------------
    
def prt():
    tprint("BlockClock", font="rnd-large") # random title design
    
def tmp(): 
    t.sleep(15)
    
                
while True: # Loop
    clear() # call clear function that clears the screen
    path = ""
    if os.path.isfile('bclock.conf'): # Check if the file 'bclock.conf' is in the same folder
        pathv = pickle.load(open("bclock.conf", "rb")) # Load the file 'bclock.conf'
        path = pathv # Copy the variable pathv to 'path'
        clear()
        menu()
    else:
        prt()
        print("Welcome to Python BlockClock\n\n")
        path = input("Insert the Path to Bitcoin-Cli: ") # path to the bitcoin-cli
        pickle.dump(path, open("bclock.conf", "wb")) # Save the file 'bclock.conf'
        clear()
        menu()

        
