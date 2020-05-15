#Developer: Curly60e
#Python BlockClock its a clock of the Bitcoin blockchain.
#Version: 0.0.3

import os
import time as t
from art import *


def getblock(): # get access to bitcoin-cli with the command getblockchaininfo
    bitcoincli = " getblockchaininfo"
    os.system(path + bitcoincli)

def getblockcount(): # get access to bitcoin-cli with the command getblockcount
    bitcoincli = " getblockcount"
    os.system(path + bitcoincli)

def clear(): # clear the screen
    os.system('cls' if os.name=='nt' else 'clear')

def getgenesis():
    bitcoincli = " getblock 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f 0 | xxd -r -p | hexyl -n 256"
    os.system(path + bitcoincli)

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
    connected(input("Are you sure you want to connect to a node? Y/n: ")) # call 'connected' function to make the connection with the node information

    
def artist(): # here we convert the result of the command 'getblockcount' on a random art design
    custom = input("Do you want random designs? Y/n: ")
    if custom == "Y" or custom == "y":
        while True:
            clear()
            design()
            tmp()
    else:
        while True:
            clear()
            getblockcount()
            tmp()
            

def design():
    bitcoinclient = path + " getblockcount"
    block = os.popen(str(bitcoinclient)).read() # 'getblockcount' convert to string
    b = block 
    tprint(b, font="rnd-large")
    

def userconn():
    option = input("Select option: ")
    if option == "A" or option == "a":
        user = input("USER@NODE: ")
        s = input("Do you want to continue Y/n: ")
        if s == "Y" or s == "y":
            clear()
            c = input("Do you want to see custom design? Y/n: ")
            if c == "Y" or c == "y": 
                while True: # connection via ssh 
                    clear()
                    sshb = "ssh " + user + " '" + "{}".format(path) + "'" + " getblockcount"
                    sshc = os.popen(str(sshb)).read()
                    sshd = sshc
                    tprint(sshd, font="rnd-large")
                    tmp()
                else:
                    menu()
            
            else:
                while True: # connection via ssh
                    clear()
                    sshb = "ssh " + user + " '" + "{}".format(path) + "'" + " getblockchaininfo"
                    os.system(sshb)
                    tmp()
        else:
            menu()
            
    elif option == "B" or option == "b":
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
            
    elif option == "C" or option == "c":
        menu()
    
                  
def tmp():
    t.sleep(15)


def menu():
    clear()
    prt()
    print("""\t\t
    Python BlockClock Menu
    Version 0.0.4
    
    A. Connect to an external node through SSH
    B. Show Blockchain information in your own node
    C. Run BlockClock in your own node
    D. Show the Genesis Block
    E. Exit
    \n\n""")
    menuA(input("Select option: "))
    
def menuUserConn():
    clear()
    prt()
    print("""\t\t
    Python BlockClock Menu
    Version 0.0.4
    
    A. Run BlockClock in this external node 
    B. Show the Genesis Block
    C. Return Main Menu
    \n\n""")
    userconn()

    
def menuA(menuS):
    if menuS == "A" or menuS == "a":
        nodeinfo()
    elif menuS == "B" or menuS == "b":
        while True:
            clear()
            getblock()
            tmp()
    elif menuS == "C" or menuS == "c":
        artist()
    elif menuS == "D" or menuS == "d":
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
    elif menuS == "E" or menuS == "e":
        exit()
            
        
    
def prt():
    tprint("BlockClock", font="rnd-large") # random title design
    
    
while True: # Loop
    clear() # call clear function that clears the screen
    prt()
    print("Welcome to Python BlockClock\n\n")
    path = input("Insert the Path to Bitcoin-Cli: ") # path to the bitcoin-cli
    clear()
    menu()

