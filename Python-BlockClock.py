import os
import time as t


def getblock(): #get access to bitcoin-cli with the command getblockchaininfo
    bitcoincli = " getblockchaininfo" #get blockchain information
    os.system(path + bitcoincli)

def clear(): #clear the screen
    os.system('cls' if os.name=='nt' else 'clear')

clear()
path = input("Path to your Bitcoin-cli: ")


while True: #Loop
    clear() #call clear function that clears the screen
    getblock() #call getblock function
    t.sleep(3) #pause the loop for 3 seconds
