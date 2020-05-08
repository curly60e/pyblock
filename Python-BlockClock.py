
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

clear()

tprint("BlockClock", font="rnd-large")

print("Welcome to Python BlockClock\n\n")
path = input("Insert the Path to Bitcoin-Cli: ") # path to the bitcoin-cli

a = input("Do you want to see just Block height? 'Yes', for just Block Height. 'No', for full blockchain data. Y/n: ") # select if block height or just ful\
lblockchain information
custom = input("Do you want random designs? Y/n: ")


while True: # Loop
    clear() # call clear function that clears the screen
    bitcoinclient = path + " getblockcount"
    block = os.popen(str(bitcoinclient)).read() # 'getblockcount' convert to string
    b = block # copy the result in the variable 'b'
    if a == "y" or a == "Y":
        if custom == "y" or custom == "Y":
            tprint(b, font="rnd-large") # use the art collection and print the result in a nice ASCII result
        else:
            getblockcount()
    else:
        getblock()

    t.sleep(3) # pause the loop for 3 seconds


