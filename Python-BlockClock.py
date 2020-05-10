import os
import time as t
from art import *


#/home/pi/Documents/bitcoin-0.19.1/bin/./bitcoin-cli -datadir=/mnt/royal/Bitcoin 

def getblock(): # get access to bitcoin-cli with the command getblockchaininfo
    bitcoincli = " getblockchaininfo"
    os.system(path + bitcoincli)


def getblockcount(): # get access to bitcoin-cli with the command getblockcount
    bitcoincli = " getblockcount"
    os.system(path + bitcoincli)

def clear(): # clear the screen
    os.system('cls' if os.name=='nt' else 'clear')
    

def connection(conn): # here we initiate the connection function 
    if conn == "Y" or conn == "y":
        nodeinfo() # call 'nodeinfo' function that makes the connection to an external node
    else:
        a = input("Do you want to see just Block height? 'Yes', for just Block Height. 'No', for full blockchain data. Y/n: ")
        if a == "y" or a == "Y":
            while True:
                clear()
                artist()
                getblockcount()
                tmp()
        else:
            while True:
                clear()
                getblock()
                tmp()

def connected(info): # here we complete the connection to the external node
    if info == "Y" or info == "y":
        user = input("USER@NODE: ")        
        s = input("Do you want to see the blockheight? Y/n: ")
        if s == "Y" or s == "y":
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
            while True: # connection via ssh
                clear()
                sshb = "ssh " + user + " '" + "{}".format(path) + "'" + " getblockchaininfo"
                os.system(sshb)
                sshc = os.popen(str(sshb)).read()
                sshd = sshc
                tmp()
    else:
        connection(input("Are you going to connect to an external node? Y/n: "))

    
def nodeinfo(): 
    print("\nAdd your node information\n")
    connected(input("Are you sure you want to connect to a node? Y/n: ")) # call 'connected' function to make the connection with the node information
    

def artist(): # here we convert the result of the command 'getblockcount' on a random art design
    custom = input("Do you want random designs? Y/n: ")
    if custom == "Y" or custom == "y":
        while True:
            clear()
            bitcoinclient = path + " getblockcount"
            block = os.popen(str(bitcoinclient)).read() # 'getblockcount' convert to string
            b = block
            tprint(b, font="rnd-large")
            tmp()
    else:
        while True:
            clear()
            getblockcount()
            tmp()
            

def tmp():
    t.sleep(15)


while True: # Loop
    clear() # call clear function that clears the screen
    tprint("BlockClock", font="rnd-large") # random title design
    print("Welcome to Python BlockClock\n\n")
    path = input("Insert the Path to Bitcoin-Cli: ") # path to the bitcoin-cli
    connection(input("Are you going to connect to an external node? Y/n: ")) # access to 'connection' function
