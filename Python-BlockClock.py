import os
import time as t

def getblock(): #get access to bitcoin-cli with the command getblockchaininfo
    bitcoincli = "/home/pi/Documents/bitcoin-0.19.1/bin/./bitcoin-cli -datadir=/mnt/royal/Bitcoin getblockchaininfo"
    os.system(bitcoincli)
    
def clear(): #clear the screen
    os.system('cls' if os.name=='nt' else 'clear')
    
    
while True: #Loop
    clear() #call clear function that clears the screen
    getblock() #call getblock function
    t.sleep(3) #pause the loop for 3 seconds