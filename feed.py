import os
import os.path
import time as t


def readFile():
    try:
        while True:
            downloadsFolder = 'downloads/'
            if not os.listdir(downloadsFolder):
                print ("\nWaiting for new data...\n")
                t.sleep(50)
            else:
                print("\t\t\nNew message from Space just arrived...\n")
                os.system("cat downloads/*")
                os.system("rm downloads/*")
                
    except (KeyboardInterrupt, SystemExit):
        exit()

        
