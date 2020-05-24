import os
import os.path
import time as t


def gitclone():
    if os.path.isdir('$HOME/pyblock/satellite'):
        print("OK Pass")
        
    else:
        url = "https://github.com/curly60e/satellite"
        os.system("git clone " + url)
        os.system("mkdir $HOME/pyblock/satellite/api/examples/.gnupg")
        os.system("cp -r $HOME/pyblock/satellite/api/examples $HOME/python-blockclock/")
        os.system("gpg --full-generate-key --homedir $HOME/pyblock/examples/.gnupg")
        
def satnode():
    os.system("python3 $HOME/pyblock/examples/demo-rx.py &")
    t.sleep(5)
    os.system("python3 $HOME/pyblock/examples/api_data_reader.py --demo  --plaintext ")
    

