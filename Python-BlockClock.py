import os
import time as t


def getblock(): #get access to bitcoin-cli with the command getblockchaininfo
    bitcoincli = " getblockchaininfo"
    os.system(path + bitcoincli)

def getblockcount(): #get access to bitcoin-cli with the command getblockcount
    bitcoincli = " getblockcount"
    os.system(path + bitcoincli)

def clear(): #clear the screen
    os.system('cls' if os.name=='nt' else 'clear')

clear()
print("Welcome to the Python Block Clock\n\n")
path = input("Insert the Path to Bitcoin-Cli: ") #path to the bitcoin-cli
a = input("Do you want to see just Block height? 'Yes', for just Block Height. 'No', for full blockchain data. Y/n: ") #select if block height or just fullblockchain information


while True: #Loop
    clear() #call clear function that clears the screen

    if a == "y" or a == "Y":
        getblockcount()
    else:
        getblock()


    t.sleep(3) #pause the loop for 3 seconds

