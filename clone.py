import os
import os.path
import time as t


def gitclone():
    if os.path.isdir('$HOME/python-blockclock/satellite'):
        print("OK Pass")
        
    else:
        url = "https://github.com/curly60e/satellite"
        os.system("git clone " + url)
        os.system("mkdir $HOME/python-blockclock/satellite/api/examples/.gnupg")
        os.system("cp -r $HOME/python-blockclock/satellite/api/examples $HOME/python-blockclock/")
        os.system("gpg --full-generate-key --homedir $HOME/python-blockclock/examples/.gnupg")
        
def satnode():
    os.system("python3 $HOME/python-blockclock/examples/demo-rx.py &")
    t.sleep(5)
    os.system("python3 $HOME/python-blockclock/examples/api_data_reader.py --demo  --plaintext ")
    

