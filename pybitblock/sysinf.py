#Developer: Curly60e
#PyBLOCK its a clock of the Bitcoin blockchain.


import psutil


def sysinfoDetail(): #Cpu and memory usage
# gives a single float value
    print("   \033[0;37;40m----------------------------")
    print("   \033[3;33;40mCPU Usage: \033[1;32;40m" + str(psutil.cpu_percent()) + "\033[0;37;40m%")
    print("   \033[3;33;40mMemory Usage: \033[1;32;40m" "{}\033[0;37;40m%".format(int(psutil.virtual_memory().percent)))
    print("   \033[3;33;40mMemory Available: \033[1;32;40m" "{} \033[0;37;40mMB".format(int(psutil.virtual_memory().available / 1024 / 1024)))
    print("   \033[3;33;40mDisk Usage: \033[1;32;40m" "{}%\033[0;37;40m%".format(psutil.disk_usage('/').percent))
    print("   \033[0;37;40m----------------------------")
