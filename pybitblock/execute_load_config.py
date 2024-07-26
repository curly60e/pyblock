import os
import pickle
import sys

def load_config():
    settings = {"gradient": "", "design": "block", "colorA": "green", "colorB": "yellow"}
    settingsClock = {"gradient": "", "colorA": "green", "colorB": "yellow"}
    path = {"ip_port": "", "rpcuser": "", "rpcpass": "", "bitcoincli": ""}

    try:
        if os.path.isfile('config/bclock.conf'):
            pathv = pickle.load(open("config/bclock.conf", "rb"))
            path = pathv
        if os.path.isfile('config/blndconnect.conf'):
            lndconnectData = pickle.load(open("config/blndconnect.conf", "rb"))
            lndconnectload = lndconnectData
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(101)

    return path, settings, settingsClock
