#Developer: Curly60e
#Tester: __B__T__C__
#ℙ𝕪𝔹𝕃𝕆ℂ𝕂 𝕚𝕥𝕤 𝕒 𝔹𝕚𝕥𝕔𝕠𝕚𝕟 𝔻𝕒𝕤𝕙𝕓𝕠𝕒𝕣𝕕 𝕨𝕚𝕥𝕙 ℂ𝕪𝕡𝕙𝕖𝕣𝕡𝕦𝕟𝕜 𝕒𝕖𝕤𝕥𝕙𝕖𝕥𝕚𝕔.


import base64, codecs, requests
import logging
import subprocess
import os
import os.path
import qrcode
import xmltodict
import time as t
try:
    import simplejson as json
except ImportError:
    import json
from cfonts import render, say
from pblogo import blogo
from logos import logoB
#from lnpay_py.wallet import LNPayWallet
from pycoingecko import CoinGeckoAPI

logger = logging.getLogger(__name__)

# Allowed fiat currency codes for rate.sx
_VALID_FIAT_CODES = {
    'AUD', 'BRL', 'CAD', 'CHF', 'CLP', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP',
    'HKD', 'HUF', 'IDR', 'ILS', 'INR', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK',
    'NZD', 'PHP', 'PKR', 'PLN', 'RUB', 'SEK', 'SGD', 'THB', 'TRY', 'TWD',
    'USD',
}

def clear(): # clear the screen
    subprocess.run(['clear'] if os.name != 'nt' else ['cls'], shell=(os.name == 'nt'))  # noqa: S603 - hardcoded safe commands only

def closed():
    print("<<< Back Control + C.\n\n")

def opreturnOnchainONLY():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    try:
        clear()
        blogo()
        output = render(
            "OP_RETURN Message", colors=['yellow'], align='left', font='tiny'
        )

        print(output)
        message = input("Message: ")

        while len(message) > 70:
            clear()
            blogo()
            print("Error! Only 80 characters allowed!")
            message = input("\nMessage: ")
        resp = requests.post('https://opreturnbot.com/api/create', json={'message': message + '...PyBLOCK'}, timeout=10)
        b = resp.text
        clear()
        blogo()
        print("\033[1;30;47m")
        qr.add_data(b)
        qr.print_ascii()
        print("\033[0;37;40m")
        print(f'LND Invoice: {b}')
        qr.clear()
        input("\nContinue...")
        if lndconnectload['ln']:
            invoiceN = b
            invoice = invoiceN.lower()
            lsd = subprocess.run([lndconnectload["ln"], "decodepayreq", invoice], capture_output=True, text=True).stdout
            lsd0 = str(lsd)
            d = json.loads(lsd0)
            url = f"https://opreturnbot.com/api/status/{d['payment_hash']}"
        else:
            cert_path = lndconnectload["tls"]
            with open(lndconnectload["macaroon"], 'rb') as f:
                macaroon = codecs.encode(f.read(), 'hex')
            headers = {'Grpc-Metadata-macaroon': macaroon}
            url = f'https://{lndconnectload["ip_port"]}/v1/payreq/{b}'
            r = requests.get(url, headers=headers, verify=cert_path, timeout=10)
            s = r.json()
            url = f"https://opreturnbot.com/api/status/{s['payment_hash']}"
        response = requests.get(url, timeout=10)
        responseB = str(response.text)
        responseC = responseB
        clear()
        blogo()
        print("\nTransaction ID: " + responseC)
        input("\nContinue...")
    except (requests.RequestException, json.JSONDecodeError, KeyError, subprocess.SubprocessError, OSError) as e:
        logger.debug("opreturnOnchainONLY error: %s", e)

def opreturn():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    try:
        lndconnectload = {"ip_port":"", "tls":"", "macaroon":"", "ln":""}
        if os.path.isfile('blndconnect.conf'): # Check if the file 'bclock.conf' is in the same folder
            with open("blndconnect.conf", "r") as f:
                lndconnectData = json.load(f) # Load the file 'bclock.conf'
                lndconnectload = lndconnectData # Copy the variable pathv to 'path'
        else:
            clear()
            blogo()
            print("\n\tIf you are going to use your local node leave IP:PORT/CERT/MACAROONS in blank.\n")
            lndconnectload["ip_port"] = input("Insert IP:PORT to your node: ") # path to the bitcoin-cli
            lndconnectload["tls"] = input("Insert the path to tls.cert file: ")
            lndconnectload["macaroon"] = input("Insert the path to admin.macaroon: ")
            print("\n\tLocal Lightning Node connection.\n")
            lndconnectload["ln"] = input("Insert the path to lncli: ")
            with open("blndconnect.conf", "w") as f:
                json.dump(lndconnectload, f) # Save the file 'bclock.conf'

        path = {"ip_port":"", "rpcuser":"", "rpcpass":"", "bitcoincli":""}
        if os.path.isfile('bclock.conf') or os.path.isfile('blnclock.conf'): # Check if the file 'bclock.conf' is in the same folder
            with open("bclock.conf", "r") as f:
                pathv = json.load(f) # Load the file 'bclock.conf'
                path = pathv # Copy the variable pathv to 'path'
        else:
            blogo()
            print("Welcome to \033[1;31;40mPyBLOCK\033[0;37;40m\n\n")
            print("\n\tIf you are going to use your local node leave IP:PORT/USER/PASSWORD in blank.\n")
            path[
                'ip_port'
            ] = f'http://{input("Insert IP:PORT to access your remote Bitcoin-Cli node: ")}'

            path['rpcuser'] = input("RPC User: ")
            path['rpcpass'] = input("RPC Password: ")
            print("\n\tLocal Bitcoin Core Node connection.\n")
            path['bitcoincli']= input("Insert the Path to Bitcoin-Cli: ")
            with open("bclock.conf", "w") as f:
                json.dump(path, f)
        clear()
        blogo()
        output = render(
            "OP_RETURN Message", colors=['yellow'], align='left', font='tiny'
        )

        print(output)
        message = input("Message: ")

        while len(message) > 70:
            clear()
            blogo()
            print("Error! Only 80 characters allowed!")
            message = input("\nMessage: ")
        resp = requests.post('https://opreturnbot.com/api/create', json={'message': message + '...PyBLOCK'}, timeout=10)
        b = resp.text
        node_not = input("\nDo you want to pay this invoice with your node? Y/n: ")
        if node_not in ["Y", "y"]:
            lndconnectload = {"ip_port":"", "tls":"", "macaroon":"", "ln":""}
            with open("blndconnect.conf", "r") as f:
                lndconnectData = json.load(f) # Load the file 'bclock.conf'
                lndconnectload = lndconnectData # Copy the variable pathv to 'path'
            if lndconnectload['ip_port']:
                print("\nInvoice: " + b + "\n")
                payinvoice()
                cert_path = lndconnectload["tls"]
                with open(lndconnectload["macaroon"], 'rb') as f:
                    macaroon = codecs.encode(f.read(), 'hex')
                headers = {'Grpc-Metadata-macaroon': macaroon}
                url = f'https://{lndconnectload["ip_port"]}/v1/payreq/{b}'
                r = requests.get(url, headers=headers, verify=cert_path, timeout=10)
                s = r.json()
                url = f"https://opreturnbot.com/api/status/{s['payment_hash']}"
                response = requests.get(url, timeout=10)
                responseB = str(response.text)
                responseC = responseB
                clear()
                blogo()
                print("\nTransaction ID: " + responseC)
                input("\nContinue...")
            elif lndconnectload['ln']:
                print("\nInvoice: " + b + "\n")
                localpayinvoice()
                invoiceN = b
                invoice = invoiceN.lower()
                lsd = subprocess.run([lndconnectload["ln"], "decodepayreq", invoice], capture_output=True, text=True).stdout
                lsd0 = str(lsd)
                d = json.loads(lsd0)
                url = f"https://opreturnbot.com/api/status/{d['payment_hash']}"
                response = requests.get(url, timeout=10)
                responseB = str(response.text)
                responseC = responseB
                clear()
                blogo()
                print("\nTransaction ID: " + responseC)
                input("\nContinue...")
        else:
            clear()
            blogo()
            print("\033[1;30;47m")
            qr.add_data(b)
            qr.print_ascii()
            print("\033[0;37;40m")
            print(f'LND Invoice: {b}')
            qr.clear()
            input("\nContinue...")
            if lndconnectload['ln']:
                invoiceN = b
                invoice = invoiceN.lower()
                lsd = subprocess.run([lndconnectload["ln"], "decodepayreq", invoice], capture_output=True, text=True).stdout
                lsd0 = str(lsd)
                d = json.loads(lsd0)
                url = f"https://opreturnbot.com/api/status/{d['payment_hash']}"
            else:
                cert_path = lndconnectload["tls"]
                with open(lndconnectload["macaroon"], 'rb') as f:
                    macaroon = codecs.encode(f.read(), 'hex')
                headers = {'Grpc-Metadata-macaroon': macaroon}
                url = f'https://{lndconnectload["ip_port"]}/v1/payreq/{b}'
                r = requests.get(url, headers=headers, verify=cert_path, timeout=10)
                s = r.json()
                url = f"https://opreturnbot.com/api/status/{s['payment_hash']}"
            response = requests.get(url, timeout=10)
            responseB = str(response.text)
            responseC = responseB
            clear()
            blogo()
            print("\nTransaction ID: " + responseC)
            input("\nContinue...")
    except (requests.RequestException, json.JSONDecodeError, KeyError, subprocess.SubprocessError, OSError) as e:
        logger.debug("opreturn error: %s", e)

def opreturn_view():
    try:
        clear()
        blogo()
        output = render(
            "OP_RETURN Message", colors=['yellow'], align='left', font='tiny'
        )

        print(output)
        responseC = input("TX ID: ")
        url2 = f'https://opreturnbot.com/api/view/{responseC}'
        r = requests.get(url2, timeout=10)
        r2 = str(r.text)
        r3 = r2
        clear()
        blogo()
        print("\nTransaction ID: " + responseC)
        print(f'OP_RETURN Message: {r3}')
        input("\nContinue...")
    except (requests.RequestException, KeyError) as e:
        logger.debug("opreturn_view error: %s", e)

def opretminer():
    try:
        resp = requests.get('https://bitcointicker.co/latestblocks/', timeout=15)
        raw_html = resp.text
        # Use html2text subprocess (safe: no user input)
        proc = subprocess.run(
            ["html2text"],
            input=raw_html, capture_output=True, text=True
        )
        lines = proc.stdout.splitlines()
        filtered = []
        capture = False
        capture_count = 0
        for line in lines:
            stripped = line.replace('|', '')
            if "Coinbase" in line:
                capture = True
                capture_count = 0
                continue
            if capture:
                capture_count += 1
                if capture_count > 70:
                    capture = False
                elif '6.25' in stripped:
                    filtered.append(stripped)
        a = '\n'.join(filtered)
        clear()
        blogo()
        closed()
        output = render(
            "decoded coinbase", colors=['yellow'], align='left', font='tiny'
        )

        print(output)
        print(a)
        input("")
    except (requests.RequestException, subprocess.SubprocessError, OSError) as e:
        logger.debug("opretminer error: %s", e)

#-----------------------------GAMES--------------------------------
#------------------------------------------------------------------

def gameroom():
    try:
        clear()
        blogo()
        print("""
        --------------------------------------

                  INITIATE ARCADE?

        --------------------------------------
        """.format(closed()))
        input("\a\nContinue...")
        subprocess.run(["ssh", "gameroom@bitreich.org"])
    except (subprocess.SubprocessError, OSError) as e:
        logger.debug("gameroom error: %s", e)
#----------------------------------------------------------------------

#-----------------------------Stats--------------------------------

def statsConn():
    try:
        resp = requests.get('https://www.bitcoinblockhalf.com/', timeout=15)
        proc = subprocess.run(
            ["html2text"],
            input=resp.text, capture_output=True, text=True
        )
        lines = proc.stdout.splitlines()
        filtered = []
        capture = False
        capture_count = 0
        for line in lines:
            cleaned = line.replace('*', '').replace('"', '')
            if "Total" in line:
                capture = True
                capture_count = 0
            if capture:
                capture_count += 1
                if capture_count > 11:
                    capture = False
                elif '--' not in cleaned:
                    filtered.append(cleaned)
        a = '\n'.join(filtered)
        clear()
        blogo()
        closed()
        output = render("stats", colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\nContinue...")
    except (requests.RequestException, subprocess.SubprocessError, OSError) as e:
        logger.debug("statsConn error: %s", e)

#-----------------------------END Stats--------------------------------

#-----------------------------PGP--------------------------------

def pgpConn():
    try:
        resp = requests.get('https://web.archive.org/web/20110228054007/http://www.bitcoin.org/Satoshi_Nakamoto.asc', timeout=15)
        a = resp.text
        clear()
        blogo()
        closed()
        output = render(
            "pgp", colors=['yellow'], align='left', font='tiny'
        )

        print(output)
        print(a)
        input("\a\nContinue...")
    except requests.RequestException as e:
        logger.debug("pgpConn error: %s", e)

#-----------------------------END PGP--------------------------------

#-----------------------------MoscowT--------------------------------
def mtConn():  # here we convert the result of the command 'getblockcount' on a random art design
    while True:
        try:
            resp = requests.get('https://blockchain.info/tobtc', params={'currency': 'USD', 'value': '1'}, timeout=10)
            a = resp.text.strip()
            sats = a.lstrip('0.')
            clear()
            blogo()
            closed()
            output = render("Moscow Time", colors=['yellow'], align='left', font='tiny')
            outputT = render(f"{sats[:4]} sats", colors=['green'], align='left', font='tiny')
            print(output)
            print(outputT)
            input("\a\nContinue...")
        except (requests.RequestException, ValueError, KeyboardInterrupt):
            break

def mtclock():
    try:
        resp = requests.get('https://blockchain.info/tobtc', params={'currency': 'USD', 'value': '1'}, timeout=10)
        a = resp.text.strip()
        clear()
        blogo()
        closed()
        output = render("Moscow Time", colors=['yellow'], align='left', font='tiny')
        outputT = render(f"{a} sats", colors=['green'], align='left', font='tiny')
        print(output)
        print(outputT)
        input("\a\nContinue...")
    except requests.RequestException as e:
        logger.debug("mtclock error: %s", e)

#-----------------------------END MT--------------------------------

#-----------------------------Satoshi--------------------------------

def satoshiConn():
    try:
        resp = requests.get('https://www.metzdowd.com/pipermail/cryptography/2009-January/014994.html', timeout=15)
        proc = subprocess.run(
            ["html2text"],
            input=resp.text, capture_output=True, text=True
        )
        lines = proc.stdout.splitlines()
        # Take last 82 lines, filter out navigation text
        tail_lines = lines[-82:] if len(lines) >= 82 else lines
        exclude = ["Unsubscribe", "Next message", "Previous message", "Messages sorted", "More information", "list]"]
        filtered = [l for l in tail_lines if not any(ex in l for ex in exclude)]
        a = '\n'.join(filtered)
        clear()
        blogo()
        closed()
        output = render(
            "𝐒𝐚𝐭𝐨𝐬𝐡𝐢 𝐍𝐚𝐤𝐚𝐦𝐨𝐭𝐨. 𝟎𝐱𝟏𝟖𝐂𝟎𝟗𝐄𝟖𝟔𝟓𝐄𝐂𝟗𝟒𝟖𝐀𝟏. 𝐃𝐄𝟒𝐄 𝐅𝐂𝐀𝟑 𝐄𝟏𝐀𝐁 𝟗𝐄𝟒𝟏 𝐂𝐄𝟗𝟔 𝐂𝐄𝐂𝐁 𝟏𝟖𝐂𝟎 𝟗𝐄𝟖𝟔 𝟓𝐄𝐂𝟗 𝟒𝟖𝐀𝟏.", colors=['green'], align='left', font='console'
        )

        print(output)
        print(a)
        input("\a\nContinue...")
    except (requests.RequestException, subprocess.SubprocessError, OSError) as e:
        logger.debug("satoshiConn error: %s", e)

#-----------------------------END Satoshi--------------------------------

#-----------------------------Whale Alert--------------------------------

def whalalConn():
    try:
        api_key = os.environ.get("WHALE_ALERT_API_KEY", "")
        if not api_key:
            print("\n\033[1;31;40mSet WHALE_ALERT_API_KEY environment variable to use Whale Alert.\033[0;37;40m")
            input("\nContinue...")
            return
        url = "https://api.whale-alert.io/v1/transactions"
        params = {"api_key": api_key, "limit": 7, "min_value": 5000000, "currency": "btc"}
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        clear()
        blogo()
        closed()
        output = render("whale alert", colors=['yellow'], align='left', font='tiny')
        print(output)
        for tx in data.get("transactions", []):
            blockchain = tx.get("blockchain", "unknown")
            amount = tx.get("amount", 0)
            amount_usd = tx.get("amount_usd", 0)
            print(f" WHALE ALERT ₿ {amount} =${amount_usd:.0f}")
        input("\a\nContinue...")
    except (requests.RequestException, json.JSONDecodeError, KeyError) as e:
        logger.debug("whalalConn error: %s", e)

#-----------------------------END Whale Alert--------------------------------
#-----------------------------bwt.dev--------------------------------

def bwtConn():
    try:
        resp = requests.get('https://bwt.dev/banner.txt', timeout=10)
        a = resp.text
        clear()
        blogo()
        closed()
        print(a)
        input("\a\nContinue...")
    except requests.RequestException as e:
        logger.debug("bwtConn error: %s", e)

#-----------------------------END bwt.dev--------------------------------
#-----------------------------Dates--------------------------------

def datesConn():
    try:
        resp = requests.get('https://bitcoinexplorer.org/fun', timeout=15)
        proc = subprocess.run(
            ["html2text"],
            input=resp.text, capture_output=True, text=True
        )
        lines = proc.stdout.splitlines()
        filtered = []
        for line in lines:
            if '20' in line and 'https' not in line and ' ' in line:
                cleaned = line.replace('[', '').replace(',', '')
                filtered.append(cleaned)
                if len(filtered) >= 46:
                    break
        a = '\n'.join(filtered)
        clear()
        blogo()
        closed()
        output = render("dates", colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\nContinue...")
    except (requests.RequestException, subprocess.SubprocessError, OSError) as e:
        logger.debug("datesConn error: %s", e)

#-----------------------------END Dates--------------------------------
#-----------------------------Quotes--------------------------------

def quotesConn():
    try:
        resp = requests.get('https://bitcoinexplorer.org/api/quotes/all', timeout=10)
        data = resp.json()
        clear()
        blogo()
        closed()
        output = render("quotes", colors=['yellow'], align='left', font='tiny')
        print(output)
        for quote in data:
            text = quote.get('text', '')
            speaker = quote.get('speaker', '')
            url = quote.get('url', '')
            date = quote.get('date', '')
            if 'conQuote' not in text:
                print(f'  Quote: {text}')
                print(f'  By: {speaker}')
                if url:
                    print(f'  Link: {url}')
                if date:
                    print(f'  Date: {date}')
                print()
        input("\a\nContinue...")
    except (requests.RequestException, json.JSONDecodeError, KeyError) as e:
        logger.debug("quotesConn error: %s", e)

#-----------------------------END Quotes--------------------------------
#-----------------------------Hashrate--------------------------------

def miningConn():
    try:
        resp = requests.get('https://bitcoinexplorer.org/api/mining/hashrate', timeout=10)
        data = resp.json()
        clear()
        blogo()
        closed()
        output = render("hashrate", colors=['yellow'], align='left', font='tiny')
        print(output)
        for key, value in data.items():
            if isinstance(value, dict):
                for k, v in value.items():
                    print(f'  {k}: {v}')
            else:
                print(f'  {key}: {value}')
        input("\a\nContinue...")
    except (requests.RequestException, json.JSONDecodeError, KeyError) as e:
        logger.debug("miningConn error: %s", e)

#-----------------------------END Hashrate--------------------------------
#-----------------------------StatsLN--------------------------------

def stalnConn():
    try:
        resp = requests.get('https://1ml.com', timeout=15)
        proc = subprocess.run(
            ["html2text"],
            input=resp.text, capture_output=True, text=True
        )
        lines = proc.stdout.splitlines()
        filtered = []
        capture = False
        capture_count = 0
        for line in lines:
            stripped = ' '.join(line.split())
            if "Number" in line:
                capture = True
                capture_count = 0
            if capture:
                filtered.append(stripped)
                capture_count += 1
                if capture_count > 8:
                    capture = False
        a = '\n'.join(filtered)
        clear()
        blogo()
        closed()
        output = render(
            "lightning stats", colors=['yellow'], align='left', font='tiny'
        )

        print(output)
        print(a)
        input("\a\nContinue...")
    except (requests.RequestException, subprocess.SubprocessError, OSError) as e:
        logger.debug("stalnConn error: %s", e)

#-----------------------------END StatsLN--------------------------------
#-----------------------------StatRanking--------------------------------
def ranConn():
    try:
        resp = requests.get('https://1ml.com/node?order=capacity&json=true', timeout=15)
        data = resp.json()
        clear()
        blogo()
        closed()
        output = render("ranking", colors=['yellow'], align='left', font='tiny')
        print(output)
        exclude_keys = {'last_update', 'color', 'noderank', 'addresses'}
        for node in data:
            if isinstance(node, dict):
                for k, v in node.items():
                    if k not in exclude_keys:
                        label = 'Node' if k == 'alias' else ('RANK' if k == 'capacity' else k)
                        print(f'  {label}: {v}')
                print()
        input("\a\nContinue...")
    except (requests.RequestException, json.JSONDecodeError, KeyError, ValueError) as e:
        logger.debug("ranConn error: %s", e)
#-----------------------------END Ranking--------------------------------

def trustednode():
    try:
        clear()
        blogo()
        closed()
        addv = """
        ---------------------------------------------------------------

                    REMEMBER TO INITIALIZE \033[1;35;40mTOR\033[0;37;40m ON THE SHELL

                            $ source torsocks on

        ---------------------------------------------------------------

        """
        print(addv)
        input("\a\nContinue...")
        conn = ["telnet", "cut45oarvxfvfydrjery6slyeca4zpal7tljygdt5bji7l3jsrrgwkad.onion", "6023"]
        subprocess.run(conn)
    except (subprocess.SubprocessError, OSError) as e:
        logger.debug("trustednode error: %s", e)
#-----------------------------END GAMES--------------------------------

#-----------------------------Node Miner--------------------------------

def CoreMiner(): 
    try:
        clear()
        blogo()
        output = render("Core Miner", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\n...Mining...")
        subprocess.run([path['bitcoincli'], "-generate", "1", "2147483647"])
        input("\a\nContinue...")
    except (subprocess.SubprocessError, OSError, KeyError) as e:
        logger.debug("CoreMiner error: %s", e)

def OwnNodeMinerComputer():
    try:
        clear()
        blogo()
        output = render(
        "Own Node Miner", colors=['yellow'], align='left', font='tiny'
        )
        if os.path.isdir ('OwnNodeMiner'):
            print("...Follow the steps...")
        else: # Check if the file 'bclock.conf' is in the same folder
            os.makedirs("OwnNodeMiner", exist_ok=True)
            subprocess.run(["wget", "https://github.com/pooler/cpuminer/releases/download/v2.5.1/pooler-cpuminer-2.5.1-linux-x86_64.tar.gz"], cwd="OwnNodeMiner")
            subprocess.run(["tar", "-xf", "pooler-cpuminer-2.5.1-linux-x86_64.tar.gz"], cwd="OwnNodeMiner")
            clear()
            blogo()
            print(output)
        responseC = input("Your RPC User: ")
        responseD = input("Your RPC Pass: ")
        responseE = input("Your Bitcoin Address: ")
        responseF = input("Select Your Threads, 2, 4, 6, 8, 10, ..: ")
        subprocess.run(["./minerd", "-a", "sha256d", "-O", f"{responseC}:{responseD}", "-o", "http://127.0.0.1:8332", f"--coinbase-addr={responseE}", "-t", responseF], cwd="OwnNodeMiner")
        input("\a\nContinue...")
    except (subprocess.SubprocessError, OSError) as e:
        logger.debug("OwnNodeMinerComputer error: %s", e)

def OwnNodeMinerRaspberry():
    try:
        clear()
        blogo()
        output = render(
        "Own Node Miner", colors=['yellow'], align='left', font='tiny'
        )
        if os.path.isdir ('OwnNodeMiner'):
            print("...Follow the steps...")
        else: # Check if the file 'bclock.conf' is in the same folder
            os.makedirs("OwnNodeMiner", exist_ok=True)
            subprocess.run(["git", "clone", "https://github.com/jojapoppa/cpuminer-multi-arm.git"], cwd="OwnNodeMiner")
            clear()
            blogo()
            print(output)
        responseC = input("Your RPC User: ")
        responseD = input("Your RPC Pass: ")
        responseE = input("Your Bitcoin Address: ")
        responseF = input("Select Your Threads, 2, 4, 6, 8, 10, ..: ")
        subprocess.run(["./cpuminer", "-a", "sha256d", "-O", f"{responseC}:{responseD}", "-o", "http://127.0.0.1:8332", f"--coinbase-addr={responseE}", "-t", responseF], cwd="OwnNodeMiner/cpuminer-multi-arm")
        input("\a\nContinue...")
    except (subprocess.SubprocessError, OSError) as e:
        logger.debug("OwnNodeMinerRaspberry error: %s", e)
#-----------------------------Node Miner--------------------------------

#-----------------------------wttr.in--------------------------------
def wttrDataV1():
    try:
        clear()
        blogo()
        weatherList = """
        ------------------------------------------------------------------------------------



            \033[1;31;40m*\033[0;37;40m uruguay                # city name
            \033[1;31;40m*\033[0;37;40m ~Giza+pyramid          # any location (+ for spaces)
            \033[1;31;40m*\033[0;37;40m Москва                 # Unicode name of any location in any language
            \033[1;31;40m*\033[0;37;40m muc                    # airport code (3 letters)
            \033[1;31;40m*\033[0;37;40m @lightninghood.com     # domain name
            \033[1;31;40m*\033[0;37;40m 94107                  # area codes
            \033[1;31;40m*\033[0;37;40m -78.46,106.79          # GPS coordinates
            \033[1;31;40m*\033[0;37;40m moon                   # Moon phase (add ,+US or ,+France for these cities)
            \033[1;31;40m*\033[0;37;40m moon@2009-01-03        # Moon phase for the date (@2016-10-25)

            PRESS \033[1;32;40mM\033[0;37;40m TO INSERT MORE DATA

        ------------------------------------------------------------------------------------

        """
        print(weatherList)
        selectData = input("Insert your data \033[1;31;40m*\033[0;37;40m : ")
        if selectData in ['M', 'm']:
            moreData = """

        ------------------------------------------------------------------------------------
                                        Supported languages

                        ar af be ca da de el es et fr fa hi hu ia id it nb nl
                        oc pl pt-br ro ru tr th uk vi zh-cn zh-tw (supported)

        ------------------------------------------------------------------------------------
        ------------------------------------------------------------------------------------
                                             Units

                    m        # metric (SI) (used by default everywhere except US)
                    u        # USCS (used by default in US)
                    M        # show wind speed in m/s

        ------------------------------------------------------------------------------------
            """
            print(moreData)
            selectData2 = input("Insert your data \033[1;31;40m*\033[0;37;40m : ")
            lang = input("Insert your language: ")
            unit = input("Insert your metric units: ")
            url = f"https://{lang}.wttr.in/{selectData2}?F&{unit}"
        else:
            url = f"https://wttr.in/{selectData}?F"
        a = requests.get(url, headers={"User-Agent": "curl"}, timeout=15).text
        clear()
        blogo()
        print(a)
        input("Continue...")
    except requests.RequestException as e:
        logger.debug("wttrDataV1 error: %s", e)

def wttrDataV2():
    try:
        clear()
        blogo()
        weatherList = """
        ------------------------------------------------------------------------------------



            \033[1;31;40m*\033[0;37;40m uruguay                # city name
            \033[1;31;40m*\033[0;37;40m ~Giza+pyramid          # any location (+ for spaces)
            \033[1;31;40m*\033[0;37;40m Москва                 # Unicode name of any location in any language
            \033[1;31;40m*\033[0;37;40m muc                    # airport code (3 letters)
            \033[1;31;40m*\033[0;37;40m @lightninghood.com     # domain name
            \033[1;31;40m*\033[0;37;40m 94107                  # area codes
            \033[1;31;40m*\033[0;37;40m -78.46,106.79          # GPS coordinates

            PRESS \033[1;32;40mM\033[0;37;40m TO INSERT MORE DATA

        ------------------------------------------------------------------------------------

        """
        print(weatherList)
        selectData = input("Insert your data \033[1;31;40m*\033[0;37;40m : ")
        if selectData in ['M', 'm']:
            moreData = """

        ------------------------------------------------------------------------------------
                                        Supported languages

                        ar af be ca da de el es et fr fa hi hu ia id it nb nl
                        oc pl pt-br ro ru tr th uk vi zh-cn zh-tw (supported)

        ------------------------------------------------------------------------------------
        ------------------------------------------------------------------------------------
                                             Units

                    m        # metric (SI) (used by default everywhere except US)
                    u        # USCS (used by default in US)
                    M        # show wind speed in m/s

        ------------------------------------------------------------------------------------
            """
            print(moreData)
            selectData2 = input("Insert your data \033[1;31;40m*\033[0;37;40m : ")
            lang = input("Insert your language: ")
            unit = input("Insert your metric units: ")
            url = f"https://v2.wttr.in/{selectData2}?{unit}&F&lang={lang}"
        else:
            url = f"https://v2.wttr.in/{selectData}?F"
        a = requests.get(url, headers={"User-Agent": "curl"}, timeout=15).text
        clear()
        blogo()
        print(a)
        input("Continue...")
    except requests.RequestException as e:
        logger.debug("wttrDataV2 error: %s", e)


#-----------------------------END wttr.in--------------------------------

#-----------------------------RATE.SX--------------------------------

def rateSXList():
    try:
        clear()
        blogo()
        fiat = """
                -------------------------------------------
                        AUD    Australian dollar
                        BRL    Brazilian real
                        CAD    Canadian dollar
                        CHF    Swiss franc
                        CLP    Chilean peso
                        CNY    Chinese yuan
                        CZK    Czech koruna
                        DKK    Danish krone
                        EUR    Euro
                        GBP    Pound sterling
                        HKD    Hong Kong dollar
                        HUF    Hungarian forint
                        IDR    Indonesian rupiah
                        ILS    Israeli shekel
                        INR    Indian rupee
                        JPY    Japanese yen
                        KRW    South Korean won
                        MXN    Mexican peso
                        MYR    Malaysian ringgit
                        NOK    Norwegian krone
                        NZD    New Zealand dollar
                        PHP    Philippine peso
                        PKR    Pakistani rupee
                        PLN    Polish zloty
                        RUB    Russian ruble
                        SEK    Swedish krona
                        SGD    Singapore dollar
                        THB    Thai baht
                        TRY    Turkish lira
                        TWD    New Taiwan dollar
                        USD    Dollars
                -------------------------------------------
        """
        print(fiat)
        selectFiat = input("Insert a Fiat currency: ").strip().upper()
        if selectFiat not in _VALID_FIAT_CODES:
            print(f"Invalid currency code: {selectFiat}")
            return
    except (KeyboardInterrupt, EOFError):
        return
    while True:
        try:
            url = f"https://{selectFiat}.rate.sx/?F&n=1"
            resp = requests.get(url, headers={"User-Agent": "curl"}, timeout=15)
            a = resp.text
            clear()
            blogo()
            closed()
            print(a)
            t.sleep(20)
        except (requests.RequestException, KeyboardInterrupt):
            break

def rateSXGraph():
    try:
        clear()
        blogo()
        fiat = """
                -------------------------------------------
                        AUD    Australian dollar
                        BRL    Brazilian real
                        CAD    Canadian dollar
                        CHF    Swiss franc
                        CLP    Chilean peso
                        CNY    Chinese yuan
                        CZK    Czech koruna
                        DKK    Danish krone
                        EUR    Euro
                        GBP    Pound sterling
                        HKD    Hong Kong dollar
                        HUF    Hungarian forint
                        IDR    Indonesian rupiah
                        ILS    Israeli shekel
                        INR    Indian rupee
                        JPY    Japanese yen
                        KRW    South Korean won
                        MXN    Mexican peso
                        MYR    Malaysian ringgit
                        NOK    Norwegian krone
                        NZD    New Zealand dollar
                        PHP    Philippine peso
                        PKR    Pakistani rupee
                        PLN    Polish zloty
                        RUB    Russian ruble
                        SEK    Swedish krona
                        SGD    Singapore dollar
                        THB    Thai baht
                        TRY    Turkish lira
                        TWD    New Taiwan dollar
                        USD    Dollars
                -------------------------------------------
        """
        print(fiat)
        selectFiat = input("Insert a Fiat currency: ").strip().upper()
        if selectFiat not in _VALID_FIAT_CODES:
            print(f"Invalid currency code: {selectFiat}")
            return
    except (KeyboardInterrupt, EOFError):
        return
    while True:
        try:
            url = f"https://{selectFiat}.rate.sx/btc"
            resp = requests.get(url, headers={"User-Agent": "curl"}, timeout=15)
            lines = resp.text.splitlines()
            filtered = [l for l in lines if 'Use' not in l]
            a = '\n'.join(filtered)
            clear()
            blogo()
            closed()
            print(a)
            t.sleep(20)
        except (requests.RequestException, KeyboardInterrupt):
            break

#-----------------------------END RATE.SX--------------------------------



#-----------------------------COINGECKO--------------------------------

def CoingeckoPP():
    try:
        btcInfo = CoinGeckoAPI()
        n = btcInfo.get_price(ids='bitcoin', vs_currencies='usd,eur,gbp,jpy,aud')
        q = n['bitcoin']
        usd = q['usd']
        eur = q['eur']
        gbp = q['gbp']
        jpy = q['jpy']
        aud = q['aud']


        print("""
        --------------------COINGECKO BITCOIN PRICE-----------------------

                              1 BTC = {} USD
                              1 BTC = {} EUR
                              1 BTC = {} GBP
                              1 BTC = {} JPY
                              1 BTC = {} AUD

        ------------------------------------------------------------------

                                  ...BUT...

                                1 BTC = 1 BTC

        ------------------------------------------------------------------
        """.format(usd,eur,gbp,jpy,aud))
        input("Continue...")
    except (requests.RequestException, KeyError, ValueError) as e:
        logger.debug("CoingeckoPP error: %s", e)

#-----------------------------END COINGECKO--------------------------------


#-----------------------------LNBITS--------------------------------

def loadFileConnLNBits(lnbitLoad):
    lnbitLoad = {"wallet_name":"", "wallet_id":"", "admin_key":"", "invoice_read_key":""}

    if os.path.isfile('lnbit.conf'): # Check if the file 'bclock.conf' is in the same folder
        with open("lnbit.conf", "r") as f:
            lnbitData = json.load(f) # Load the file 'bclock.conf'
            lnbitLoad = lnbitData # Copy the variable pathv to 'path'
    else:
        clear()
        blogo()
        print("""\n\t   \033[1;33;40mATENTION\033[0;37;40m: YOU ARE GOING TO CREATE A FILE WITH YOUR INFORMATION OF CONNECTION TO LNBITS.COM.
                   WE WILL NEED SOME INFORMATION FROM YOUR ACCOUNT THAT THE ONLY ONE THAT WILL HAVE ACCESS IS YOU.
                          IF YOU DELETE THIS FILE YOU WILL NEED TO PAY AGAIN TO GET ACCESS FROM PyBLOCK.
                                           SAVE THE FILE '\033[1;33;40mlnbitSN.conf\033[0;37;40m' IN A SAFE PLACE.\n
        """)
        lnbitLoad["wallet_name"] = input("Wallet name: ") # path to the bitcoin-cli
        lnbitLoad["wallet_id"] = input("Wallet ID: ")
        lnbitLoad["admin_key"] = input("Admin key: ")
        lnbitLoad["invoice_read_key"] = input("Invoice/read key: ")
        with open("lnbit.conf", "w") as f:
            json.dump(lnbitLoad, f)
    return lnbitLoad

def createFileConnLNBits():
    clear()
    blogo()
    print("""\n\t   \033[1;33;40mATENTION\033[0;37;40m: YOU ARE GOING TO CREATE A FILE WITH YOUR INFORMATION OF CONNECTION TO LNBITS.COM.
               WE WILL NEED SOME INFORMATION FROM YOUR ACCOUNT THAT THE ONLY ONE THAT WILL HAVE ACCESS IS YOU.
                      IF YOU DELETE THIS FILE YOU WILL NEED TO PAY AGAIN TO GET ACCESS FROM PyBLOCK.
                                       SAVE THE FILE '\033[1;33;40mlnbitSN.conf\033[0;37;40m' IN A SAFE PLACE.\n
    """)
    lnbitLoad = {
        'wallet_id': '',
        'admin_key': '',
        'invoice_read_key': '',
        'wallet_name': input("Wallet name: "),
    }

    lnbitLoad["wallet_id"] = input("Wallet ID: ")
    lnbitLoad["admin_key"] = input("Admin key: ")
    lnbitLoad["invoice_read_key"] = input("Invoice/read key: ")

    with open("lnbit.conf", "w") as f:
        json.dump(lnbitLoad, f)

def lnbitCreateNewInvoice():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    try:
        print("\n\tLNBITS CREATE INVOICE\n")
        amt = input("Amount: ")
        memo = input("Memo: ")
        a = loadFileConnLNBits(['invoice_read_key'])
        b = str(a['invoice_read_key'])
        headers = {"X-Api-Key": b, "Content-type": "application/json"}
        payload = {"out": False, "amount": int(amt), "memo": f"{memo} -PyBLOCK"}
        sh = requests.post("https://legend.lnbits.com/api/v1/payments", json=payload, headers=headers, timeout=10).text
        clear()
        blogo()
        n = str(sh)
        d = json.loads(n)
        q = d['payment_request']
        c = q.lower()
        node_not = input("Do you want to pay this invoice with your node? Y/n: ")

        while True:
            if node_not in ["Y", "y"]:
                lndconnectload = {"ip_port":"", "tls":"", "macaroon":"", "ln":""}
                with open("blndconnect.conf", "r") as f:
                    lndconnectData = json.load(f) # Load the file 'bclock.conf'
                    lndconnectload = lndconnectData # Copy the variable pathv to 'path'
                if lndconnectload['ip_port']:
                    print("\nInvoice: " + c + "\n")
                    payinvoice()
                elif lndconnectload['ln']:
                    print("\nInvoice: " + c + "\n")
                    localpayinvoice()
            elif node_not in ["N", "n"]:
                print("\033[1;30;47m")
                qr.add_data(c)
                qr.print_ascii()
                print("\033[0;37;40m")
                qr.clear()
                print(f'Lightning Invoice: {c}')
                t.sleep(10)
                dn = str(d['checking_id'])
                headers = {"X-Api-Key": b, "Content-type": "application/json"}
                rsh = requests.get(f"https://legend.lnbits.com/api/v1/payments/{dn}", headers=headers, timeout=10).text
                clear()
                blogo()
                nn = str(rsh)
                dd = json.loads(nn)
                db = dd['paid']
                if db != True:
                    continue
                clear()
                blogo()
                tick()
                t.sleep(2)
                break
    except (requests.RequestException, json.JSONDecodeError, KeyError, OSError) as e:
        logger.debug("lnbitCreateNewInvoice error: %s", e)

def lnbitPayInvoice():
    bolt = input("Invoice: ")
    a = loadFileConnLNBits(['admin_key'])
    b = str(a['admin_key'])
    headers = {"X-Api-Key": b, "Content-type": "application/json"}
    payload = {"out": True, "bolt11": bolt}

    try:
        sh = requests.post("https://legend.lnbits.com/api/v1/payments", json=payload, headers=headers, timeout=10).text
        n = str(sh)
        d = json.loads(n)
        dn = str(d['checking_id'])
        a = loadFileConnLNBits(['invoice_read_key'])
        b = str(a['invoice_read_key'])
        while True:
            headers = {"X-Api-Key": b, "Content-type": "application/json"}
            rsh = requests.get(f"https://legend.lnbits.com/api/v1/payments/{dn}", headers=headers, timeout=10).text
            clear()
            blogo()
            nn = str(rsh)
            dd = json.loads(nn)
            db = dd['paid']
            if db != True:
                continue
            tick()
            t.sleep(2)
            break
    except (requests.RequestException, json.JSONDecodeError, KeyError) as e:
        logger.debug("lnbitPayInvoice error: %s", e)

def lnbitCreatePayWall():
    while True:
        try:
            url = input("Url: ")
            memo = input("Memo: ")
            desc = input("Description: ")
            amt = input("Amount in sats: ")
            remb = input("Remembers Y/n: ")
            a = loadFileConnLNBits(['admin_key'])
            if remb in ["Y", "y"]:
                remember = "true"
            elif remb in ["N", "n"]:
                remember = "false"
            b = str(a['admin_key'])
            headers = {"X-Api-Key": b, "Content-type": "application/json"}
            payload = {"url": url, "memo": memo, "description": desc, "amount": int(amt), "remembers": remember == "true"}
            sh = requests.post("https://legend.lnbits.com/paywall/api/v1/paywalls", json=payload, headers=headers, timeout=10).text
            clear()
            blogo()
            n = str(sh)
            d = json.loads(n)
            print("\n\tPAYWALL CREATED SUCCESSFULLY\n")
            t.sleep(2)
            clear()
            aa = loadFileConnLNBits(['invoice_read_key'])
            bb = str(a['invoice_read_key'])
            headers = {"X-Api-Key": bb}
            sh = requests.get("https://legend.lnbits.com/paywall/api/v1/paywalls", headers=headers, timeout=10).text
            clear()
            blogo()
            n = str(sh)
            d = json.loads(n)
            while True:
                print("\n\tLNBITS PAYWALL LIST\n")
                for item_ in d:
                    s = item_
                    print(f'ID: {s["id"]}')
                nd = input("\nSelect ID: ")
                for item in d:
                    s = item
                    nn = s['id']
                    if nd == nn:
                        print("\n----------------------------------------------------------------------------------------------------------------")
                        print(
                            """
                        \tLNBITS PAYWALL DECODED

                        ID: {}
                        Amount: {} sats
                        Description: {}
                        Memo: {}
                        Extras: {}
                        Remembers: {}
                        URL: {}
                        Wallet: {}
                        """.format(
                                nn,
                                s['amount'],
                                s['description'],
                                s['memo'],
                                s['extras'],
                                s['remembers'],
                                s['url'],
                                s['wallet'],
                            )
                        )

                        print("----------------------------------------------------------------------------------------------------------------\n")
                input("Continue...")
            clear()
            blogo()
        except (requests.RequestException, json.JSONDecodeError, KeyError, KeyboardInterrupt):
            break

def lnbitListPawWall():
    a = loadFileConnLNBits(['invoice_read_key'])
    b = str(a['invoice_read_key'])
    headers = {"X-Api-Key": b}
    sh = requests.get("https://legend.lnbits.com/paywall/api/v1/paywalls", headers=headers, timeout=10).text
    clear()
    blogo()
    n = str(sh)
    d = json.loads(n)
    while True:
        print("\n\tLNBITS PAYWALL LIST\n")
        try:
            for item_ in d:
                s = item_
                print(f'ID: {s["id"]}')
            nd = input("\nSelect ID: ")
            for item in d:
                s = item
                nn = s['id']
                if nd == nn:
                    print("\n----------------------------------------------------------------------------------------------------------------")
                    print("""
                    \tLNBITS PAYWALL DECODED

                    ID: {}
                    Amount: {} sats
                    Description: {}
                    Memo: {}
                    Extras: {}
                    Remembers: {}
                    URL: {}
                    Wallet: {}
                    """.format(s['id'], s['amount'], s['description'], s['memo'], s['extras'], s['remembers'], s['url'], s['wallet']))
                    print("----------------------------------------------------------------------------------------------------------------\n")
        except (json.JSONDecodeError, KeyError, KeyboardInterrupt):
            break
        input("Continue...")
        clear()
        blogo()

def lnbitDeletePayWall():
    while True:
        try:
            a = loadFileConnLNBits(['invoice_read_key'])
            b = str(a['invoice_read_key'])
            headers = {"X-Api-Key": b}
            sh = requests.get("https://legend.lnbits.com/paywall/api/v1/paywalls", headers=headers, timeout=10).text
            clear()
            blogo()
            n = str(sh)
            d = json.loads(n)
            while True:
                print("\n\tLNBITS PAYWALL LIST\n")
                try:
                    for item_ in d:
                        s = item_
                        print(f'ID: {s["id"]}')
                    nd = input("\nSelect ID: ")
                    for item in d:
                        s = item
                        nn = s['id']
                        if nd == nn:
                            print("\n----------------------------------------------------------------------------------------------------------------")
                            print("""
                            \tLNBITS PAYWALL DECODED

                            ID: {}
                            Amount: {} sats
                            Description: {}
                            Memo: {}
                            Extras: {}
                            Remembers: {}
                            URL: {}
                            Wallet: {}
                            """.format(s['id'], s['amount'], s['description'], s['memo'], s['extras'], s['remembers'], s['url'], s['wallet']))
                            print("----------------------------------------------------------------------------------------------------------------\n")
                except (json.JSONDecodeError, KeyError, KeyboardInterrupt):
                    break
                input("Continue...")
                break
            print("\n\tDELETE PAYWALL\n")
            a = loadFileConnLNBits(['admin_key'])
            b = str(a['admin_key'])
            id = input("Insert PayWall ID: ")
            headers = {"X-Api-Key": b}
            sh = requests.delete(f"https://legend.lnbits.com/paywall/api/v1/paywalls/{id}", headers=headers, timeout=10).text
            clear()
            blogo()
            print("\n\tPAYWALL DELETED SUCCESSFULLY\n")
            t.sleep(2)
            clear()
        except (requests.RequestException, json.JSONDecodeError, KeyError, KeyboardInterrupt):
            break

def lnbitsLNURLw():
    while True:
        try:
            clear()
            blogo()
            print("""
            ----------------------
                 CREATE LNURL
            ----------------------\n""")
            title = input("Title: ")
            minwith = input("Minimum Withdraw: ")
            maxwith = input("Maximum Withdraw: ")
            usesw = input("Uses: ")
            waittime = input("Wait Time: ")
            isunique = input("Is unique? true/false: ")
            a = loadFileConnLNBits(['admin_key'])
            b = str(a['admin_key'])
            headers = {"X-Api-Key": b, "Content-type": "application/json"}
            payload = {"title": title, "min_withdrawable": int(minwith), "max_withdrawable": int(maxwith), "uses": int(usesw), "wait_time": int(waittime), "is_unique": isunique == "true"}
            sh = requests.post("https://legend.lnbits.com/withdraw/api/v1/links", json=payload, headers=headers, timeout=10).text
            clear()
            blogo()
            n = str(sh)
            d = json.loads(n)
            print("\n\tLNURLW CREATED SUCCESSFULLY\n")
            t.sleep(2)
            clear()
            while True:
                headers = {"X-Api-Key": b}
                sh = requests.get("https://legend.lnbits.com/withdraw/api/v1/links", headers=headers, timeout=10).text
                clear()
                blogo()
                n = str(sh)
                d = json.loads(n)
                print("\n\tLNBITS LNURLW LIST\n")
                for item_ in d:
                    s = item_
                    print(f'ID: {s["id"]} Uses: ' + str(s['uses']) + " Used: " + str(s['used']))
                nd = input("\nSelect ID: ")
                for item in d:
                    s = item
                    nn = s['id']
                    if nd == nn:
                        print("\n----------------------------------------------------------------------------------------------------------------")
                        print("""
                        \tLNBITS LNURLW DECODED

                        ID: {}
                        LNURL: {}
                        Wait Time: {}
                        Uses: {}
                        Used: {}
                        Minimum Withdraw: {}
                        Maximum Withdraw: {}
                        """.format(s['id'], s['lnurl'], s['wait_time'], s['uses'], s['used'], s['min_withdrawable'], s['max_withdrawable']))
                        print("----------------------------------------------------------------------------------------------------------------\n")
                input("Continue...")
                clear()
                blogo()
        except (requests.RequestException, json.JSONDecodeError, KeyError, KeyboardInterrupt):
            break

def lnbitsLNURLwList():
    try:
        while True:
            a = loadFileConnLNBits(['admin_key'])
            b = str(a['admin_key'])
            headers = {"X-Api-Key": b}
            sh = requests.get("https://legend.lnbits.com/withdraw/api/v1/links", headers=headers, timeout=10).text
            clear()
            blogo()
            n = str(sh)
            d = json.loads(n)
            print("\n\tLNBITS LNURLW LIST\n")
            for item_ in d:
                s = item_
                print(f'ID: {s["id"]} Uses: ' + str(s['uses']) + " Used: " + str(s['used']))
            nd = input("\nSelect ID: ")
            for item in d:
                s = item
                nn = s['id']
                if nd == nn:
                    print("\n----------------------------------------------------------------------------------------------------------------")
                    print("""
                    \tLNBITS LNURLW DECODED

                    ID: {}
                    LNURL: {}
                    Wait Time: {}
                    Uses: {}
                    Used: {}
                    Minimum Withdraw: {}
                    Maximum Withdraw: {}
                    """.format(s['id'], s['lnurl'], s['wait_time'], s['uses'], s['used'], s['min_withdrawable'], s['max_withdrawable']))
                    print("----------------------------------------------------------------------------------------------------------------\n")
            input("Continue...")
    except (requests.RequestException, json.JSONDecodeError, KeyError, KeyboardInterrupt):
        print("\n")

#-------------------------1d646820055e4e2da218e801eaacfc94----END LNBITS--------------------------------
#-----------------------------LNPAY--------------------------------

def loadFileConnLNPay(lnpayLoad):
    lnpayLoad = {"key":""}

    if os.path.isfile('lnpay.conf'): # Check if the file 'bclock.conf' is in the same folder
        with open("lnpay.conf", "r") as f:
            lnpayData = json.load(f) # Load the file 'bclock.conf'
            lnpayLoad = lnpayData # Copy the variable pathv to 'path'
    else:
        clear()
        blogo()
        print("""\n\t   \033[1;33;40mATENTION\033[0;37;40m: YOU ARE GOING TO CREATE A FILE WITH YOUR INFORMATION OF CONNECTION TO LNPAY.CO.
                   WE WILL NEED SOME INFORMATION FROM YOUR ACCOUNT THAT THE ONLY ONE THAT WILL HAVE ACCESS IS YOU.
                          IF YOU DELETE THIS FILE YOU WILL NEED TO PAY AGAIN TO GET ACCESS FROM PyBLOCK.
                                           SAVE THE FILE '\033[1;33;40mlnpaySN.conf\033[0;37;40m' IN A SAFE PLACE.\n
        """)
        lnpayLoad["key"] = input("API Key: ")
        print("\n\tWALLET ACCESS KEYS\n")
        lnpayLoad["wallet_key_id"] = input("Wallet Admin: ")
        with open("lnpay.conf", "w") as f:
            json.dump(lnpayLoad, f)
    clear()
    blogo()
    return lnpayLoad

def createFileConnLNPay():
    clear()
    blogo()
    print("""\n\t   \033[1;33;40mATENTION\033[0;37;40m: YOU ARE GOING TO CREATE A FILE WITH YOUR INFORMATION OF CONNECTION TO LNPAY.CO.
               WE WILL NEED SOME INFORMATION FROM YOUR ACCOUNT THAT THE ONLY ONE THAT WILL HAVE ACCESS IS YOU.
                      IF YOU DELETE THIS FILE YOU WILL NEED TO PAY AGAIN TO GET ACCESS FROM PyBLOCK.
                                       SAVE THE FILE '\033[1;33;40mlnpaySN.conf\033[0;37;40m' IN A SAFE PLACE.\n
    """)
    lnpayLoad["key"] = input("API Key: ")
    print("\n\tWALLET ACCESS KEYS\n")
    lnpayLoad["wallet_key_id"] = input("Wallet Admin: ")
    with open("lnpay.conf", "w") as f:
        json.dump(lnpayLoad, f)


#-----------------------------END LNPAY--------------------------------
#-----------------------------OPENNODE--------------------------------

def loadFileConnOpenNode(opennodeLoad):
    opennodeLoad = {"key":"","wdr":"","inv":""}

    if os.path.isfile('opennode.conf'): # Check if the file 'bclock.conf' is in the same folder
        with open("opennode.conf", "r") as f:
            opennodeData = json.load(f) # Load the file 'bclock.conf'
            opennodeLoad = opennodeData # Copy the variable pathv to 'path'
    else:
        clear()
        blogo()
        print("""\n\t   \033[1;33;40mATENTION\033[0;37;40m: YOU ARE GOING TO CREATE A FILE WITH YOUR INFORMATION OF CONNECTION TO OPENNODE.COM.
                   WE WILL NEED SOME INFORMATION FROM YOUR ACCOUNT THAT THE ONLY ONE THAT WILL HAVE ACCESS IS YOU.
                          IF YOU DELETE THIS FILE YOU WILL NEED TO PAY AGAIN TO GET ACCESS FROM PyBLOCK.
                                           SAVE THE FILE '\033[1;33;40mopennodeSN.conf\033[0;37;40m' IN A SAFE PLACE.\n
        """)
        opennodeLoad["key"] = input("API Read Only Key: ")
        opennodeLoad["wdr"] = input("API Withdrawall Key: ")
        opennodeLoad["inv"] = input("API Invoices Key: ")
        with open("opennode.conf", "w") as f:
            json.dump(opennodeLoad, f)
    clear()
    blogo()
    return opennodeLoad

def createFileConnOpenNode():
    clear()
    blogo()
    print("""\n\t   \033[1;33;40mATENTION\033[0;37;40m: YOU ARE GOING TO CREATE A FILE WITH YOUR INFORMATION OF CONNECTION TO OPENNODE.COM.
               WE WILL NEED SOME INFORMATION FROM YOUR ACCOUNT THAT THE ONLY ONE THAT WILL HAVE ACCESS IS YOU.
                      IF YOU DELETE THIS FILE YOU WILL NEED TO PAY AGAIN TO GET ACCESS FROM PyBLOCK.
                                       SAVE THE FILE '\033[1;33;40mopennodeSN.conf\033[0;37;40m' IN A SAFE PLACE.\n
    """)
    opennodeLoad = {'wdr': '', 'inv': '', 'key': input("API Read Only Key: ")}
    opennodeLoad["wdr"] = input("API Withdrawall Key: ")
    opennodeLoad["inv"] = input("API Invoices Key: ")
    with open("opennode.conf", "w") as f:
        json.dump(opennodeLoad, f)

def OpenNodelistfunds():
    a = loadFileConnOpenNode(['wdr'])
    b = str(a['wdr'])
    headers = {"Content-Type": "application/json", "Authorization": b}
    sh = requests.get("https://api.opennode.co/v1/account/balance", headers=headers, timeout=10).text
    clear()
    blogo()
    n = str(sh)
    d = json.loads(n)
    r = d['data']
    print("\n----------------------------------------------------------------------------------------------------")
    p = r['balance']
    print("""
    OPENNODE BALANCE

    Amount: {} sats
    """.format(p['BTC']))
    print("----------------------------------------------------------------------------------------------------\n")
    input("Continue...")

def OpenNodeCheckStatus():
    sh = requests.get("https://status.opennode.com/history.rss", timeout=10).text
    clear()
    blogo()
    my_dict=xmltodict.parse(sh)
    n=json.dumps(my_dict)
    nn = str(n)
    qq = json.loads(n)
    a = qq['rss']
    b = a['channel']
    c = b['title']
    d = b['item']
    dd = d[0]
    e = dd['title']
    print("""
    \n----------------------------------------------------------------------------------------------------
    \n\t{}

    {}\n
    {}

    \n----------------------------------------------------------------------------------------------------
    """.format(c.upper(),e,b['pubDate']))
    input("Enter to Continue...")

def OpenNodecreatecharge():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    a = loadFileConnOpenNode(['key'])
    b = str(a['key'])
    fiat = input("Are you going to pay in FIAT? Y/n:")
    if fiat in ["Y", "y"]:
        print("\n----------------------------------------------------------------------------------------------------")
        print("""
        \tFIAT supported on OpenNode:

        AED,AFN,ALL,AMD,ANG,AOA,ARS,AUD,AWG,AZN,BAM,BBD,BDT,BGN,BHD,BIF,BMD,BND,BOB,BRL,BSD,BTN,BWP,
        BYN,BZD,CAD,CDF,CHF,CLF,CLP,CNH,CNY,COP,CRC,CUC,CUP,CVE,CZK,DJF,DKK,DOP,DZD,EGP,ERN,ETB,EUR,
        FJD,FKP,GBP,GEL,GGP,GHS,GIP,GMD,GNF,GTQ,GYD,HKD,HNL,HRK,HTG,HUF,IDR,ILS,IMP,INR,IQD,IRR,ISK,
        JEP,JMD,JOD,JPY,KES,KGS,KHR,KMF,KPW,KRW,KWD,KYD,KZT,LAK,LBP,LKR,LRD,LSL,LYD,MAD,MDL,MGA,MKD,
        MMK,MNT,MOP,MRO,MUR,MVR,MWK,MXN,MYR,MZN,NAD,NGN,NIO,NOK,NPR,NZD,OMR,PAB,PEN,PGK,PHP,PKR,PLN,
        PYG,QAR,RON,RSD,RUB,RWF,SAR,SBD,SCR,SDG,SEK,SGD,SHP,SLL,SOS,SRD,SSP,STD,SVC,SYP,SZL,THB,TJS,
        TMT,TND,TOP,TRY,TTD,TWD,TZS,UAH,UGX,USD,UYU,UZS,VES,VND,VUV,WST,XAF,XAG,XAU,XCD,XDR,XOF,XPD,
        XPF,XPT,YER,ZAR,ZMW,ZWL,USDC.
        """)
        print("\n----------------------------------------------------------------------------------------------------")
        selection = input("Select a FIAT currency: ")
        amt = input(f"Amount in {selection}: ")
        headers = {"Authorization": b, "Content-Type": "application/json"}
        payload = {"amount": amt, "currency": selection.upper()}
        sh = requests.post("https://api.opennode.co/v1/charges", json=payload, headers=headers, timeout=10).text
        clear()
        blogo()
        n = str(sh)
        d = json.loads(n)
        dd = d['data']
        qq = dd['lightning_invoice']
        pp = dd['address']
        nn = qq['payreq']
        mm = nn.lower()
        while True:
            try:
                print("\n----------------------------------------------------------------------------------------------------")
                print("""
                \tOPENNODE PAYMENT REQUEST

                Amount: {} {}
                ID: {}
                Status: {}
                Invoice: {}
                Onchain Address: {}
                Amount: {} sats
                """.format(amt, selection.upper(), dd['id'], dd['status'], mm, pp, dd['amount']))
                print("----------------------------------------------------------------------------------------------------\n")
                pay = input("Invoice or Onchain Address? I/O: ")
                if pay in ["I", "i"]:
                    node_not = input("Do you want to pay this invoice with your node? Y/n: ")
                    if node_not in ["Y", "y"]:
                        lndconnectload = {"ip_port":"", "tls":"", "macaroon":"", "ln":""}
                        with open("blndconnect.conf", "r") as f:
                            lndconnectData = json.load(f) # Load the file 'bclock.conf'
                            lndconnectload = lndconnectData # Copy the variable pathv to 'path'
                        if lndconnectload['ip_port']:
                            print("\nInvoice: " + mm + "\n")
                            payinvoice()
                        elif lndconnectload['ln']:
                            print("\nInvoice: " + mm + "\n")
                            localpayinvoice()
                    elif node_not in ["N", "n"]:
                        print("\033[1;30;47m")
                        qr.add_data(mm)
                        qr.print_ascii()
                        print("\033[0;37;40m")
                        qr.clear()
                        print("\nLightning Invoice: " + mm)
                elif pay in ["O", "o"]:
                    print("\033[1;30;47m")
                    qr.add_data(pp)
                    qr.print_ascii()
                    print("\033[0;37;40m")
                    qr.clear()
                    print("\nAmount in sats: {} sats".format(dd['amount']))
                    print("\nOnchain Address: " + pp)
                input("\nContinue...")
                clear()
                blogo()
            except (requests.RequestException, json.JSONDecodeError, KeyError, KeyboardInterrupt):
                break
    elif fiat in ["N", "n"]:
        amt = input("Amount in sats: ")
        headers = {"Authorization": b, "Content-Type": "application/json"}
        payload = {"amount": amt, "currency": "BTC"}
        sh = requests.post("https://api.opennode.co/v1/charges", json=payload, headers=headers, timeout=10).text
        clear()
        blogo()
        n = str(sh)
        d = json.loads(n)
        dd = d['data']
        qq = dd['lightning_invoice']
        nn = qq['payreq']
        pp = dd['address']
        mm = nn.lower()
        while True:
            try:
                print("\n----------------------------------------------------------------------------------------------------")
                print("""
                \tOPENNODE PAYMENT REQUEST

                Amount: {} sats
                ID: {}
                Status: {}
                Invoice: {}
                Onchain Address: {}
                Amount: {} sats
                """.format(amt, dd['id'], dd['status'], mm, pp, dd['amount']))
                print("----------------------------------------------------------------------------------------------------\n")
                pay = input("Invoice or Onchain Address? I/O: ")
                if pay in ["I", "i"]:
                    node_not = input("Do you want to pay this invoice with your node? Y/n: ")
                    if node_not in ["Y", "y"]:
                        with open("blndconnect.conf", "r") as f:
                            lndconnectData = json.load(f) # Load the file 'bclock.conf'
                        lndconnectload = {"ip_port":"", "tls":"", "macaroon":"", "ln":""}
                        lndconnectload = lndconnectData # Copy the variable pathv to 'path'
                        if lndconnectload['ip_port']:
                            print("\nInvoice: " + mm + "\n")
                            payinvoice()
                        elif lndconnectload['ln']:
                            print("\nInvoice: " + mm + "\n")
                            localpayinvoice()
                    elif node_not in ["N", "n"]:
                        print("\033[1;30;47m")
                        qr.add_data(mm)
                        qr.print_ascii()
                        print("\033[0;37;40m")
                        qr.clear()
                        print("\nLightning Invoice: " + mm)
                elif pay in ["O", "o"]:
                    print("\033[1;30;47m")
                    qr.add_data(pp)
                    qr.print_ascii()
                    print("\033[0;37;40m")
                    qr.clear()
                    print("\nAmount in sats: {} sats".format(dd['amount']))
                    print("\nOnchain Address: " + pp)
                input("\nContinue...")
                clear()
                blogo()
            except (requests.RequestException, json.JSONDecodeError, KeyError, KeyboardInterrupt):
                break

def OpenNodeiniciatewithdrawal():
    a = loadFileConnOpenNode(['wdr'])
    b = str(a['wdr'])
    c = loadFileConnOpenNode(['key'])
    d = str(a['key'])
    lnchain = input("Are you going to pay with Lightning or Onchain? L/O: ")
    clear()
    blogo()
    if lnchain in ["L", "l"]:
        try:
            while True:
                invoice = input("\nInvoice: ")
                headers = {"Authorization": b, "Content-Type": "application/json"}
                payload = {"pay_req": invoice}
                ssh = requests.post("https://api.opennode.co/v1/charge/decode", json=payload, headers=headers, timeout=10).text
                nn = str(ssh)
                dd = json.loads(nn)
                print(dd)
                if invoice != "":
                    break
                print("\n----------------------------------------------------------------------------------------------------")
                print("""
                    \tOPENNODE TRANSFER REQUEST

                    Message: {}
                    """.format(dd['message']))
                print("----------------------------------------------------------------------------------------------------\n")
            rr = dd['data']
            ss = rr['pay_req']

            print("\n----------------------------------------------------------------------------------------------------")
            print("""
            \tOPENNODE TRANSFER REQUEST

            Network: {}
            Amount: {} sats
            Destination: {}
            Hash: {}
            """.format(ss['network'],ss['amount'],ss['pub_key'],ss['hash']))
            print("----------------------------------------------------------------------------------------------------\n")
            print("<<< Cancel Control + C")
            input("\nEnter to Continue... ")

            headers = {"Authorization": b, "Content-Type": "application/json"}
            payload = {"type": "ln", "address": invoice, "callback_url": ""}
            sh = requests.post("https://api.opennode.co/v2/withdrawals", json=payload, headers=headers, timeout=10).text
            n = str(sh)
            d = json.loads(n)
            clear()
            blogo()
            tick()
            t.sleep(2)
        except (requests.RequestException, json.JSONDecodeError, KeyError) as e:
            logger.debug("OpenNodeiniciatewithdrawal LN error: %s", e)

    elif lnchain in ["O", "o"]:
        try:
            while True:
                print("\n\tOPENNODE TRANSFER REQUEST\n")
                print("\n\tMinimum amount 200000 sats\n")
                address = input("\nBitcoin Address: ")
                amt = int(input("Amount in sats: "))
                headers = {"Authorization": b, "Content-Type": "application/json"}
                payload = {"type": "chain", "amount": amt, "address": address, "callback_url": ""}

                if amt < 199999:
                    sh = requests.post("https://api.opennode.co/v2/withdrawals", json=payload, headers=headers, timeout=10).text
                    n = str(sh)
                    d = json.loads(n)
                    print("\n----------------------------------------------------------------------------------------------------")
                    print("""
                    \tOPENNODE TRANSFER REQUEST

                    Message: {}
                    """.format(d['message']))
                    print("----------------------------------------------------------------------------------------------------\n")
                elif amt > 200000:
                    sh = requests.post("https://api.opennode.co/v2/withdrawals", json=payload, headers=headers, timeout=10).text
                    n = str(sh)
                    d = json.loads(n)
                    dd = d['data']
                    print("\n----------------------------------------------------------------------------------------------------")
                    print("""
                    \tOPENNODE TRANSFER REQUEST

                    Amount: {} sats
                    Address Destination: {}
                    Fee: {}
                    Status: {}
                    """.format(dd['amount'],dd['address'],dd['fee'], dd['status']))
                    print("----------------------------------------------------------------------------------------------------\n")
                    input("\nContinue... ")
                    clear()
                    blogo()
                    logoB()
                    t.sleep(2)
                    break
        except (requests.RequestException, json.JSONDecodeError, KeyError, ValueError) as e:
            logger.debug("OpenNodeiniciatewithdrawal onchain error: %s", e)

def OpenNodeListPayments():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    a = loadFileConnOpenNode(['wdr'])
    b = str(a['wdr'])
    headers = {"Content-Type": "application/json", "Authorization": b}
    sh = requests.get("https://api.opennode.co/v1/withdrawals", headers=headers, timeout=10).text
    clear()
    blogo()
    print("\n\tOPENNODE TRANSACTIONS LIST\n")
    n = str(sh)
    d = json.loads(n)
    da = d['data']
    while True:
        try:
            for item_ in da:
                s = item_
                n = s['status']
                q = str(n)
                print(f'ID: {s["id"]} {q}')
            nd = input("\nSelect ID: ")
            for item in da:
                s = item
                nn = s['id']
                if nd == nn:
                    print("\n----------------------------------------------------------------------------------------------------")
                    print("""
                    \tOPENNODE TRANSACTION DECODED
                    ID: {}
                    Amount: {} sats
                    Type: {}
                    Invoice or Tx ID: {}
                    Status: {}
                    """.format(s['id'], s['amount'], s['type'], s['reference'], s['status']))
                    print("----------------------------------------------------------------------------------------------------\n")
                    print("\033[1;30;47m")
                    qr.add_data(s['reference'])
                    qr.print_ascii()
                    print("\033[0;37;40m")
                    qr.clear()
            input("Continue...")
            clear()
            blogo()
            print("\n\tOPENNODE TRANSACTIONS LIST\n")
        except (json.JSONDecodeError, KeyError, KeyboardInterrupt):
            break

#-----------------------------END OPENNODE--------------------------------
#-----------------------------TIPPINME--------------------------------

def loadFileTippinMe(tippinmeLoad):
    tippinmeLoad = {"key":""}

    if os.path.isfile('tippinme.conf'): # Check if the file 'bclock.conf' is in the same folder
        with open("tippinme.conf", "r") as f:
            tippinmeData = json.load(f) # Load the file 'bclock.conf'
            tippinmeLoad = tippinmeData # Copy the variable pathv to 'path'
    else:
        clear()
        blogo()
        print("""\n\t   \033[1;33;40mATENTION\033[0;37;40m: YOUR CONFIGURATION INFORMATION WILL BE SAVE IN '\033[1;33;40mtippinme.conf\033[0;37;40m'
                                                                IF YOU NEED TO START AGAIN, DELETE IT.\n
        """)
        tippinmeLoad["key"] = input("Twitter @user: ")
        with open("tippinme.conf", "w") as f:
            json.dump(tippinmeLoad, f)
    clear()
    blogo()
    return tippinmeLoad

def createFileTippinMe():
    clear()
    blogo()
    print("""\n\t   \033[1;33;40mATENTION\033[0;37;40m: YOUR CONFIGURATION INFORMATION WILL BE SAVE IN '\033[1;33;40mtippinme.conf\033[0;37;40m'
                                                                IF YOU NEED TO START AGAIN, DELETE IT.\n
    """)
    tippinmeLoad = {'key': input("Twitter @user: ")}
    with open("tippinme.conf", "w") as f:
        json.dump(tippinmeLoad, f)

def tippinmeGetInvoice():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    a = loadFileTippinMe(['key'])
    b = str(a['key'])
    try:
        print("\n\tTIPPINME GENERATE INVOICE\n")
        q = input("Amount in Sats: ")
        clear()
        blogo()
        url = f'https://api.tippin.me/v1/public/addinvoice/{b}/{q}'
        response = requests.get(url, timeout=10)
        responseB = str(response.text)
        responseC = responseB
        lnreq = responseC.split(',')
        lnurl = lnreq[1]
        lnurlS = str(lnurl)
        lnurlR = lnurlS.split(':')
        lnurlW = lnurlR[1]
        ln = str(lnurlW)
        ln1 = ln.strip('"')
        node_not = input("Do you want to pay this invoice with your node? Y/n: ")
        if node_not in ["Y", "y"]:
            lndconnectload = {"ip_port":"", "tls":"", "macaroon":"", "ln":""}
            with open("blndconnect.conf", "r") as f:
                lndconnectData = json.load(f) # Load the file 'bclock.conf'
                lndconnectload = lndconnectData # Copy the variable pathv to 'path'
            if lndconnectload['ip_port']:
                print("\nInvoice: " + ln1 + "\n")
                payinvoice()
            elif lndconnectload['ln']:
                print("\nInvoice: " + ln1 + "\n")
                localpayinvoice()
        elif node_not in ["N", "n"]:
            print("\033[1;30;47m")
            qr.add_data(ln1)
            qr.print_ascii()
            print("\033[0;37;40m")
            print(f'LND Invoice: {ln1}')
            response.close()
            input("Continue...")
    except (requests.RequestException, json.JSONDecodeError, KeyError, IndexError, OSError) as e:
        logger.debug("tippinmeGetInvoice error: %s", e)

#-----------------------------END TIPPINME--------------------------------
#-----------------------------TALLYCOIN------------------------------
def loadFileConnTallyCo(tallycoLoad):
    tallycoLoad = {"tallyco.conf":"","id":""}

    if os.path.isfile('tallyco.conf'): # Check if the file 'bclock.conf' is in the same folder
        with open("tallyco.conf", "r") as f:
            tallyData = json.load(f) # Load the file 'bclock.conf'
            tallycoLoad = tallyData # Copy the variable pathv to 'path'
    else:
        clear()
        blogo()
        print("""\n\t   \033[1;33;40mATENTION\033[0;37;40m: YOU ARE GOING TO CREATE A FILE WITH YOUR INFORMATION OF CONNECTION TO TALLYCO.IN.
                   WE WILL NEED SOME INFORMATION FROM YOUR ACCOUNT THAT THE ONLY ONE THAT WILL HAVE ACCESS IS YOU.
                          IF YOU DELETE THIS FILE YOU WILL NEED TO PAY AGAIN TO GET ACCESS FROM PyBLOCK.
                                           SAVE THE FILE '\033[1;33;40mtallycoSN.conf\033[0;37;40m' IN A SAFE PLACE.\n
        """)
        print("\nEXAMPLE: https://tallyco.in/s/{fundraiser_id}/\n")
        tallycoLoad["id"] = input("User ID or Twitter @USER: ")
        with open("tallyco.conf", "w") as f:
            json.dump(tallycoLoad, f)
    clear()
    blogo()
    return tallycoLoad

def createFileConnTallyCo():
    clear()
    blogo()
    print("""\n\t   \033[1;33;40mATENTION\033[0;37;40m: YOU ARE GOING TO CREATE A FILE WITH YOUR INFORMATION OF CONNECTION TO TALLYCO.IN.
               WE WILL NEED SOME INFORMATION FROM YOUR ACCOUNT THAT THE ONLY ONE THAT WILL HAVE ACCESS IS YOU.
                      IF YOU DELETE THIS FILE YOU WILL NEED TO PAY AGAIN TO GET ACCESS FROM PyBLOCK.
                                       SAVE THE FILE '\033[1;33;40mtallycoSN.conf\033[0;37;40m' IN A SAFE PLACE.\n
    """)
    print("\nEXAMPLE: https://tallyco.in/s/{fundraiser_id}/\n")
    tallycoLoad = {'fundraiser_id': '', 'id': input("User ID or Twitter @USER: ")}
    with open("tallyco.conf", "w") as f:
        json.dump(tallycoLoad, f)

def tallycoGetPayment():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    c = loadFileConnTallyCo(['id'])
    d = str(c['id'])
    try:
        amount = input("Amount in Sats: ")
        print("""\nPayment Method Example: 'ln' or 'btc'
                 'ln' = Lightnin Netowrk
                 'btc'= Bitcoin Onchain Payment
                    \n""")
        lnd_onchain = input("Payment Method: ")
        payload = {"type": "profile", "id": d, "satoshi_amount": amount, "payment_method": lnd_onchain}
        tallycomethod = requests.post("https://api.tallyco.in/v1/payment/request/", data=payload, timeout=10).text
        n = str(tallycomethod)
        d = json.loads(n)
        clear()
        blogo()
        if lnd_onchain == "ln":
            e = d['lightning_pay_request']
            f = e.lower()
            print("\033[1;30;47m")
            qr.add_data(f)
            qr.print_ascii()
            print("\033[0;37;40m")
            print(f'LND Invoice: {f}')
            qr.clear()
            input("\nContinue...")
        elif lnd_onchain == "btc":
            e = d['btc_address']
            print("\033[1;30;47m")
            qr.add_data(e)
            qr.print_ascii()
            print("\033[0;37;40m")
            print(f'Amount: {d["cost"]}')
            print(f'Bitcoin Address: {e}')
            qr.clear()
            input("\nContinue...")
    except (requests.RequestException, json.JSONDecodeError, KeyError) as e:
        logger.debug("tallycoGetPayment error: %s", e)


def tallycoDonateid():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    clear()
    blogo()
    try:
        donate = input("Donate to ID: ")
        amount = input("Amount in Sats: ")
        print("""\nPayment Method Example: 'ln' or 'btc'
                 'ln' = Lightnin Netowrk
                 'btc'= Bitcoin Onchain Payment
                    \n""")
        lnd_onchain = input("Payment Method: ")
        payload = {"type": "profile", "id": donate, "satoshi_amount": amount, "payment_method": lnd_onchain}
        tallycomethod = requests.post("https://api.tallyco.in/v1/payment/request/", data=payload, timeout=10).text
        n = str(tallycomethod)
        d = json.loads(n)
        clear()
        blogo()
        if lnd_onchain in ["ln", "lN", "Ln", "LN"]:
            node_not = input("Do you want to pay this tip with your node? Y/n: ")
            if node_not in ["Y", "y"]:
                lndconnectload = {"ip_port":"", "tls":"", "macaroon":"", "ln":""}
                with open("blndconnect.conf", "r") as f:
                    lndconnectData = json.load(f) # Load the file 'bclock.conf'
                    lndconnectload = lndconnectData # Copy the variable pathv to 'path'
                if lndconnectload['ip_port']:
                    e = d['lightning_pay_request']
                    f = e.lower()
                    print("\nInvoice: " + f + "\n")
                    payinvoice()
                elif lndconnectload['ln']:
                    e = d['lightning_pay_request']
                    f = e.lower()
                    print("\nInvoice: " + f + "\n")
                    localpayinvoice()
            elif node_not in ["N", "n"]:
                e = d['lightning_pay_request']
                f = e.lower()
                print("\033[1;30;47m")
                qr.add_data(f)
                qr.print_ascii()
                print("\033[0;37;40m")
                print(f'LND Invoice: {f}')
                qr.clear()
                input("\nContinue...")
        elif lnd_onchain in ["btc", "bTC", "BtC", "BTC", "BTc", "btC"]:
            e = d['btc_address']
            print("\033[1;30;47m")
            qr.add_data(e)
            qr.print_ascii()
            print("\033[0;37;40m")
            print(f'Amount: {d["cost"]}')
            print(f'Bitcoin Address: {e}')
            qr.clear()
            input("\nContinue...")
    except (requests.RequestException, json.JSONDecodeError, KeyError, OSError) as e:
        logger.debug("tallycoDonateid error: %s", e)


#-----------------------------END TALLYCOIN------------------------------
#-----------------------------MEMPOOL.SPACE------------------------------

def fee():
    try:
        while True:
            r = requests.get('https://mempool.space/api/v1/fees/recommended', timeout=10)
            r.headers['Content-Type']
            n = r.text
            di = json.loads(n)
            clear()
            blogo()
            print("""
            ------------------------
                Fastest Fee:   {}
                Half Hour Fee: {}
                Hour Fee:      {}
            ------------------------
            <<< Back Control + C
            """.format(di['fastestFee'], di['halfHourFee'], di['hourFee']))
            t.sleep(5)
            print("\n\t    Getting New Information")
    except (requests.RequestException, json.JSONDecodeError, KeyError, KeyboardInterrupt) as e:
        logger.debug("fee error: %s", e)

def blocks():
    try:
        while True:
            clear()
            blogo()
            print("\n\t             Getting New Information")
            r = requests.get('https://mempool.space/api/v1/fees/mempool-blocks', timeout=10)
            r.headers['Content-Type']
            n = r.text
            di = json.loads(n)
            for n in range(len(di)):
                q = di[n]
                clear()
                blogo()
                print("""
                -----------------------------------------
                                  BLOCK
                -----------------------------------------
                    Block Size:   {} bytes
                    Block VSize:  {} bytes
                    Transactions: {}
                    Total Fees:   {}
                    Median Fee:   {}
                -----------------------------------------
                <<< Back Control + C
                """.format(q['blockSize'], q['blockVSize'], q['nTx'], q['totalFees'], q['medianFee']))
                t.sleep(3)
    except (requests.RequestException, json.JSONDecodeError, KeyError, KeyboardInterrupt) as e:
        logger.debug("blocks error: %s", e)


#-----------------------------END MEMPOOL.SPACE------------------------------
