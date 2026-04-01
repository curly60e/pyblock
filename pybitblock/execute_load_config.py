import json
import os
import sys

def load_config():
    settings = {"gradient": "", "design": "block", "colorA": "green", "colorB": "yellow"}
    settingsClock = {"gradient": "", "colorA": "green", "colorB": "yellow"}
    path = {"ip_port": "", "rpcuser": "", "rpcpass": "", "bitcoincli": ""}

    try:
        if os.path.isfile('config/bclock.conf'):
            with open("config/bclock.conf", "r") as f:
                pathv = json.load(f)
            path = pathv
        if os.path.isfile('config/blndconnect.conf'):
            with open("config/blndconnect.conf", "r") as f:
                lndconnectData = json.load(f)
            lndconnectload = lndconnectData
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(101)

    return path, settings, settingsClock
