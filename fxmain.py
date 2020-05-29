import os
import time as t
import psutil
from pblogo import *

 
def sysinfo():  #Cpu and memory usage
    print("   \033[0;37;40m----------------------")
    print("   |\033[3;33;40mCPU Usage: \033[1;32;40m" + str(psutil.cpu_percent()) + "%\033[0;37;40m    |")
    print("   |\033[3;33;40mMemory Usage: \033[1;32;40m" "{}% \033[0;37;40m  |".format(int(psutil.virtual_memory().percent)))
    print("   \033[0;37;40m----------------------")

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
       
def close():
    print("<<< Back to the Main Menu Press Control + C.\n\n")
    
def readHexBlock(): # Hex Decoder using Hexyl on local node
    hexa = input("Add the Block Hash you want to decode: ")
    blocknumber = input("Add the Block number: ")
    decodeBlock = path + " getblock {} {}".format(hexa, blocknumber) + " | xxd -r -p | hexyl -n 256"
    os.system(decodeBlock)
    
def readHexTx(): # Hex Decoder using Hexyl on an external node
    hexa = input("Add the Transaction ID. you want to decode: ")
    decodeTX = path + " getrawtransaction {}".format(hexa) + " | xxd -r -p | hexyl -n 256"
    os.system(decodeTX)
    
def prt():
    print("\033[1;32;40m")
    blogo()
    #tprint("PyBLOCK", font="rnd-large") # random title design
    print("\033[0;37;40m")

def tmp():
    t.sleep(15)