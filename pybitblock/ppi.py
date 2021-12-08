#Developer: Curly60e
#Tester: __B__T__C__
#ℙ𝕪𝔹𝕃𝕆ℂ𝕂 𝕚𝕥𝕤 𝕒 𝔹𝕚𝕥𝕔𝕠𝕚𝕟 𝔻𝕒𝕤𝕙𝕓𝕠𝕒𝕣𝕕 𝕨𝕚𝕥𝕙 ℂ𝕪𝕡𝕙𝕖𝕣𝕡𝕦𝕟𝕜 𝕒𝕖𝕤𝕥𝕙𝕖𝕥𝕚𝕔.


import base64, codecs, json, requests
import pickle
import os
import os.path
import qrcode
import lnpay_py
import requests
import xmltodict
import time as t
import simplejson as json
from art import *
from cfonts import render, say
from nodeconnection import *
from pblogo import *
from logos import *
from lnpay_py.wallet import LNPayWallet
from pycoingecko import CoinGeckoAPI

def clear(): # clear the screen
    os.system('cls' if os.name=='nt' else 'clear')

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
        output = render(str("OP_RETURN Message"), colors=['yellow'], align='left', font='tiny')
        print(output)
        message = input("Message: ")
        curl = "curl --header " + """"Content-Type: application/json" """ + "--request POST  --data " + """'{"message":""" + '"{}...PyBLOCK"'.format(message) + "}'"  + " https://opreturnbot.com/api/create"
        while True:
            if len(message) <= 70:
                break
            clear()
            blogo()
            print("Error! Only 80 characters allowed!")
            message = input("\nMessage: ")
        a = os.popen(curl).read()
        b = str(a)
        clear()
        blogo()
        print("\033[1;30;47m")
        qr.add_data(b)
        qr.print_ascii()
        print("\033[0;37;40m")
        print("LND Invoice: " + b)
        qr.clear()
        input("\nContinue...")
        if lndconnectload['ln']:
            invoiceN = b
            invoice = invoiceN.lower()
            lncli = " payinvoice "
            lsd = os.popen(lndconnectload['ln'] + " decodepayreq " + invoice).read()
            lsd0 = str(lsd)
            d = json.loads(lsd0)
            url = 'http://opreturnbot.com/api/status/{}'.format(d['payment_hash'])
        else:
            cert_path = lndconnectload["tls"]
            macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
            headers = {'Grpc-Metadata-macaroon': macaroon}
            bolt11N = b
            url = 'https://{}/v1/payreq/{}'.format(lndconnectload["ip_port"],bolt11N)
            r = requests.get(url, headers=headers, verify=cert_path)
            s = r.json()
            url = 'http://opreturnbot.com/api/status/{}'.format(s['payment_hash'])
        response = requests.get(url)
        responseB = str(response.text)
        responseC = responseB
        clear()
        blogo()
        print("\nTransaction ID: " + responseC)
        input("\nContinue...")
    except:
        pass

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
            lndconnectData= pickle.load(open("blndconnect.conf", "rb")) # Load the file 'bclock.conf'
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
            pickle.dump(lndconnectload, open("blndconnect.conf", "wb")) # Save the file 'bclock.conf'

        path = {"ip_port":"", "rpcuser":"", "rpcpass":"", "bitcoincli":""}
        if os.path.isfile('bclock.conf') or os.path.isfile('blnclock.conf'): # Check if the file 'bclock.conf' is in the same folder
            pathv = pickle.load(open("bclock.conf", "rb")) # Load the file 'bclock.conf'
            path = pathv # Copy the variable pathv to 'path'
        else:
            blogo()
            print("Welcome to \033[1;31;40mPyBLOCK\033[0;37;40m\n\n")
            print("\n\tIf you are going to use your local node leave IP:PORT/USER/PASSWORD in blank.\n")
            path['ip_port'] = "http://{}".format(input("Insert IP:PORT to access your remote Bitcoin-Cli node: "))
            path['rpcuser'] = input("RPC User: ")
            path['rpcpass'] = input("RPC Password: ")
            print("\n\tLocal Bitcoin Core Node connection.\n")
            path['bitcoincli']= input("Insert the Path to Bitcoin-Cli: ")
            pickle.dump(path, open("bclock.conf", "wb"))
        clear()
        blogo()
        output = render(str("OP_RETURN Message"), colors=['yellow'], align='left', font='tiny')
        print(output)
        message = input("Message: ")
        curl = "curl --header " + """"Content-Type: application/json" """ + "--request POST  --data " + """'{"message":""" + '"{}...PyBLOCK"'.format(message) + "}'"  + " https://opreturnbot.com/api/create"
        while True:
            if len(message) <= 70:
                break
            clear()
            blogo()
            print("Error! Only 80 characters allowed!")
            message = input("\nMessage: ")
        a = os.popen(curl).read()
        b = str(a)
        node_not = input("\nDo you want to pay this invoice with your node? Y/n: ")
        if node_not in ["Y", "y"]:
            lndconnectload = {"ip_port":"", "tls":"", "macaroon":"", "ln":""}
            lndconnectData = pickle.load(open("blndconnect.conf", "rb")) # Load the file 'bclock.conf'
            lndconnectload = lndconnectData # Copy the variable pathv to 'path'
            if lndconnectload['ip_port']:
                print("\nInvoice: " + b + "\n")
                payinvoice()
                cert_path = lndconnectload["tls"]
                macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
                headers = {'Grpc-Metadata-macaroon': macaroon}
                bolt11N = b
                url = 'https://{}/v1/payreq/{}'.format(lndconnectload["ip_port"],bolt11N)
                r = requests.get(url, headers=headers, verify=cert_path)
                s = r.json()
                url = 'http://opreturnbot.com/api/status/{}'.format(s['payment_hash'])
                response = requests.get(url)
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
                lncli = " payinvoice "
                lsd = os.popen(lndconnectload['ln'] + " decodepayreq " + invoice).read()
                lsd0 = str(lsd)
                d = json.loads(lsd0)
                url = 'http://opreturnbot.com/api/status/{}'.format(d['payment_hash'])
                response = requests.get(url)
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
            print("LND Invoice: " + b)
            qr.clear()
            input("\nContinue...")
            if lndconnectload['ln']:
                invoiceN = b
                invoice = invoiceN.lower()
                lncli = " payinvoice "
                lsd = os.popen(lndconnectload['ln'] + " decodepayreq " + invoice).read()
                lsd0 = str(lsd)
                d = json.loads(lsd0)
                url = 'http://opreturnbot.com/api/status/{}'.format(d['payment_hash'])
            else:
                cert_path = lndconnectload["tls"]
                macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
                headers = {'Grpc-Metadata-macaroon': macaroon}
                bolt11N = b
                url = 'https://{}/v1/payreq/{}'.format(lndconnectload["ip_port"],bolt11N)
                r = requests.get(url, headers=headers, verify=cert_path)
                s = r.json()
                url = 'http://opreturnbot.com/api/status/{}'.format(s['payment_hash'])
            response = requests.get(url)
            responseB = str(response.text)
            responseC = responseB
            clear()
            blogo()
            print("\nTransaction ID: " + responseC)
            input("\nContinue...")
    except:
        pass

def opreturn_view():
    try:
        clear()
        blogo()
        output = render(str("OP_RETURN Message"), colors=['yellow'], align='left', font='tiny')
        print(output)
        responseC = input("TX ID: ")
        url2 = 'http://opreturnbot.com/api/view/{}'.format(responseC)
        r = requests.get(url2)
        r2 = str(r.text)
        r3 = r2
        clear()
        blogo()
        print("\nTransaction ID: " + responseC)
        print("OP_RETURN Message: " + r3)
        input("\nContinue...")
    except:
        pass

def opretminer():
    try:
        conn = """curl -s 'https://bitcointicker.co/latestblocks/' | xargs --null | html2text | grep "Coinbase" -A 70 | tr -d '|' | grep -v "Coinbase" | grep '6.25'"""
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render(str("decoded coinbase"), colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("")
    except:
        pass

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
        conn = "ssh gameroom@bitreich.org"
        os.system(conn).read()
    except:
        pass
#----------------------------------------------------------------------

#-----------------------------Stats--------------------------------

def statsConn():
    try:
        conn = """curl -s https://www.bitcoinblockhalf.com/ | html2text | grep -E "Total" -A 10  | grep -v -E "\--" | tr -d '*' | jq -R | tr -d '"' """
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render(str("stats"), colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\nContinue...")
    except:
        pass

#-----------------------------END Stats--------------------------------
#-----------------------------Whale Alert--------------------------------

def whalalConn():
    try:
        conn = """curl -s 'https://api.whale-alert.io/v1/transactions?api_key=3LYGErNwoCSj6QUsWOWdpEuGTuYxakMZ&limit=7&currency=btc' | jq  -C '.transactions[]' | tr -d '{|}|,|"|:|' | grep -E "blockchain|amount" -A 8 | grep -v -E "\--|from|symbol|to|id" | xargs -L 1 | sed 's/blockchain/PyBLØCK/g' | sed 's/amount/₿/g' | sed 's/_usd/=$/g' | sed 's/bitcoin/WHALE ALERT/g' | grep -E ' '"""
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render(str("whale alert"), colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\nContinue...")
    except:
        pass

#-----------------------------END Whale Alert--------------------------------
#-----------------------------bwt.dev--------------------------------

def bwtConn():
    try:
        conn = "curl -s https://bwt.dev/banner.txt"
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        print(a)
        input("\a\nContinue...")
    except:
        pass

#-----------------------------END bwt.dev--------------------------------
#-----------------------------Dates--------------------------------

def datesConn():
    try:
        conn = """curl -s "https://bitcoinexplorer.org/fun" | html2text | grep "20" | grep -v -E "https" | grep -E " " | head -n 46 | tr -d '[' | tr -d ',' | jq -R"""
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render(str("dates"), colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\nContinue...")
    except:
        pass

#-----------------------------END Dates--------------------------------
#-----------------------------Quotes--------------------------------

def quotesConn():
    try:
        conn = """curl -s "https://bitcoinexplorer.org/api/quotes/all" | jq -C '.[]' | tr -d '{|}|]|,' | sed 's/text/Quote/g' | sed 's/speaker/By/g' | sed 's/url/Link/g' | sed 's/date/Date/g' | grep -v -E 'conQuote'"""
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render(str("quotes"), colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\nContinue...")
    except:
        pass
#-----------------------------END Quotes--------------------------------
#-----------------------------Hashrate--------------------------------

def miningConn():
    try:
        conn = """curl -s "https://bitcoinexplorer.org/api/mining/hashrate" | jq -C '.[]' | tr -d '{|}|]|,'"""
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render(str("hashrate"), colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\nContinue...")
    except:
        pass

#-----------------------------END Hashrate--------------------------------
#-----------------------------StatsLN--------------------------------

def stalnConn():
    try:
        conn = """curl -s 'https://1ml.com' | html2text | xargs -L 1 | grep -E "Number" -A 8 | jq -R"""
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render(str("lightning stats"), colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\nContinue...")
    except:
        pass

#-----------------------------END StatsLN--------------------------------
#-----------------------------StatRanking--------------------------------
def ranConn():
    try:
        conn = """curl -s 'https://1ml.com/node?order=capacity&json=true' | jq -C '.[]' | xargs -L 1  | tr -d '{|}|]|,' | grep -v -E "last_update|color|noderank" | sed 's/alias/Node/g' | grep -v -E "addresses" | grep -E " " | sed 's/capacity/RANK/g'
"""
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render(str("ranking"), colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\nContinue...")
    except:
        pass
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
        conn = "telnet cut45oarvxfvfydrjery6slyeca4zpal7tljygdt5bji7l3jsrrgwkad.onion 6023"
        os.system(conn)
    except:
        pass
#-----------------------------END GAMES--------------------------------

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
            list = "curl '" + lang + ".wttr.in/" + selectData2 + "?F&" + unit + "'"
        else:
            list = "curl wttr.in/" + selectData + "?F"
        a = os.popen(list).read()
        clear()
        blogo()
        print(a)
        input("Continue...")
    except:
        pass

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
            list = "curl 'v2.wttr.in/" + selectData2 + "?" + unit + "&F&lang=" + lang + "'"

        else:
            list = "curl v2.wttr.in/" + selectData + "?F"
        a = os.popen(list).read()
        clear()
        blogo()
        print(a)
        input("Continue...")
    except:
        pass


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
        selectFiat = input("Insert a Fiat currency: ")
    except:
        pass
    while True:
        try:
            list = "curl -s '" + selectFiat + ".rate.sx/?F&n=1'"
            a = os.popen(list).read()
            clear()
            blogo()
            closed()
            print(a)
            t.sleep(20)
        except:
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
        selectFiat = input("Insert a Fiat currency: ")
    except:
        pass
    while True:
        try:
            list = "curl -s '" + selectFiat + """.rate.sx/btc' | grep -v -E 'Use'"""
            a = os.popen(list).read()
            clear()
            blogo()
            closed()
            print(a)
            t.sleep(20)
        except:
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
    except:
        pass

#-----------------------------END COINGECKO--------------------------------


#-----------------------------LNBITS--------------------------------

def loadFileConnLNBits(lnbitLoad):
    lnbitLoad = {"wallet_name":"", "wallet_id":"", "admin_key":"", "invoice_read_key":""}

    if os.path.isfile('lnbit.conf'): # Check if the file 'bclock.conf' is in the same folder
        lnbitData= pickle.load(open("lnbit.conf", "rb")) # Load the file 'bclock.conf'
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
        pickle.dump(lnbitLoad, open("lnbit.conf", "wb"))
    return lnbitLoad

def createFileConnLNBits():
    lnbitLoad = {"wallet_name":"", "wallet_id":"", "admin_key":"", "invoice_read_key":""}

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

    pickle.dump(lnbitLoad, open("lnbit.conf", "wb"))

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
        curl = 'curl -X POST https://lnbits.com/api/v1/payments -d ' + "'{" + """"out": false, "amount": {}, "memo": "{} -PyBLOCK" """.format(amt,memo) + "}'" + """ -H "X-Api-Key: {} " -H "Content-type: application/json" """.format(b)
        sh = os.popen(curl).read()
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
                lndconnectData = pickle.load(open("blndconnect.conf", "rb")) # Load the file 'bclock.conf'
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
                print("Lightning Invoice: " + c)
                t.sleep(10)
                dn = str(d['checking_id'])
                checkcurl = 'curl -X GET https://lnbits.com/api/v1/payments/' + dn + """ -H "X-Api-Key: {}" -H "Content-type: application/json" """.format(b)
                rsh = os.popen(checkcurl).read()
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
    except:
        pass

def lnbitPayInvoice():
    bolt = input("Invoice: ")
    a = loadFileConnLNBits(['admin_key'])
    b = str(a['admin_key'])
    curl = 'curl -X POST https://lnbits.com/api/v1/payments -d ' + "'{" + """"out": true, "bolt11": "{}" """.format(bolt) + "}'" + """ -H "X-Api-Key: {}" -H "Content-type: application/json" """.format(b)
    try:
        sh = os.popen(curl).read()
        n = str(sh)
        d = json.loads(n)
        dn = str(d['checking_id'])
        a = loadFileConnLNBits(['invoice_read_key'])
        b = str(a['invoice_read_key'])
        while True:
            checkcurl = 'curl -X GET https://lnbits.com/api/v1/payments/' + dn + """ -H "X-Api-Key: {}" -H "Content-type: application/json" """.format(b)
            rsh = os.popen(checkcurl).read()
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
    except:
        pass

def lnbitCreatePayWall():
    while True:
        try:
            url = input("Url: ")
            memo = input("Memo: ")
            desc = input("Description: ")
            amt = input("Amount in sats: ")
            remb = input("Remembers Y/n: ")
            a = loadFileConnLNBits(['admin_key'])
            b = str(a['admin_key'])
            if remb in ["Y", "y"]:
                remember = "true"
            elif remb in ["N", "n"]:
                remember = "false"
            curl = 'curl -X POST https://lnbits.com/paywall/api/v1/paywalls -d ' + "'{" + """"url": "{}", "memo": "{}", "description": "{}", "amount": {}, "remembers": {} """.format(url,memo,desc,amt,remember) + "}'" + """ -H  "Content-type: application/json" -H "X-Api-Key: {}" """.format(b)
            sh = os.popen(curl).read()
            clear()
            blogo()
            n = str(sh)
            d = json.loads(n)
            print("\n\tPAYWALL CREATED SUCCESSFULLY\n")
            t.sleep(2)
            clear()
            aa = loadFileConnLNBits(['invoice_read_key'])
            bb = str(a['invoice_read_key'])
            checkcurl = 'curl -X GET https://lnbits.com/paywall/api/v1/paywalls -H' + """ "X-Api-Key: {}" """.format(bb)
            sh = os.popen(checkcurl).read()
            clear()
            blogo()
            n = str(sh)
            d = json.loads(n)
            while True:
                print("\n\tLNBITS PAYWALL LIST\n")
                for item_ in d:
                    s = item_
                    print("ID: " + s['id'])
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
                input("Continue...")
            clear()
            blogo()
        except:
            break

def lnbitListPawWall():
    a = loadFileConnLNBits(['invoice_read_key'])
    b = str(a['invoice_read_key'])
    checkcurl = 'curl -X GET https://lnbits.com/paywall/api/v1/paywalls -H' + """ "X-Api-Key: {}" """.format(b)
    sh = os.popen(checkcurl).read()
    clear()
    blogo()
    n = str(sh)
    d = json.loads(n)
    while True:
        print("\n\tLNBITS PAYWALL LIST\n")
        try:
            for item_ in d:
                s = item_
                print("ID: " + s['id'])
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
        except:
            break
        input("Continue...")
        clear()
        blogo()

def lnbitDeletePayWall():
    while True:
        try:
            a = loadFileConnLNBits(['invoice_read_key'])
            b = str(a['invoice_read_key'])
            checkcurl = 'curl -X GET https://lnbits.com/paywall/api/v1/paywalls -H' + """ "X-Api-Key: {}" """.format(b)
            sh = os.popen(checkcurl).read()
            clear()
            blogo()
            n = str(sh)
            d = json.loads(n)
            while True:
                print("\n\tLNBITS PAYWALL LIST\n")
                try:
                    for item_ in d:
                        s = item_
                        print("ID: " + s['id'])
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
                except:
                    break
                input("Continue...")
                break
            print("\n\tDELETE PAYWALL\n")
            a = loadFileConnLNBits(['admin_key'])
            b = str(a['admin_key'])
            id = input("Insert PayWall ID: ")
            curl = "curl -X DELETE https://lnbits.com/paywall/api/v1/paywalls/{}".format(id) + """ -H "X-Api-Key: {}" """.format(b)
            sh = os.popen(curl).read()
            clear()
            blogo()
            print("\n\tPAYWALL DELETED SUCCESSFULLY\n")
            t.sleep(2)
            clear()
        except:
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
            curl = 'curl -X POST https://lnbits.com/withdraw/api/v1/links -d ' + """'{"title":""" + f'"{title}", "min_withdrawable": {minwith}, "max_withdrawable": {maxwith}, "uses": {usesw}, "wait_time": {waittime}, "is_unique": {isunique}' + "}'"  + ' -H "Content-type: application/json" -H "X-Api-Key: {}"'.format(b)
            sh = os.popen(curl).read()
            clear()
            blogo()
            n = str(sh)
            d = json.loads(n)
            print("\n\tLNURLW CREATED SUCCESSFULLY\n")
            t.sleep(2)
            clear()
            while True:
                checkcurl = 'curl -X GET https://lnbits.com/withdraw/api/v1/links -H ' '"X-Api-Key: {}"'.format(b)
                sh = os.popen(checkcurl).read()
                clear()
                blogo()
                n = str(sh)
                d = json.loads(n)
                print("\n\tLNBITS LNURLW LIST\n")
                for item_ in d:
                    s = item_
                    print("ID: " + s['id'] + " Uses: " + str(s['uses']) + " Used: " + str(s['used']))
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
        except:
            break

def lnbitsLNURLwList():
    try:
        while True:
            a = loadFileConnLNBits(['admin_key'])
            b = str(a['admin_key'])
            checkcurl = 'curl -X GET https://lnbits.com/withdraw/api/v1/links -H ' '"X-Api-Key: {}"'.format(b)
            sh = os.popen(checkcurl).read()
            clear()
            blogo()
            n = str(sh)
            d = json.loads(n)
            print("\n\tLNBITS LNURLW LIST\n")
            for item_ in d:
                s = item_
                print("ID: " + s['id'] + " Uses: " + str(s['uses']) + " Used: " + str(s['used']))
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
    except:
        print("\n")

#-------------------------1d646820055e4e2da218e801eaacfc94----END LNBITS--------------------------------
#-----------------------------LNPAY--------------------------------

def loadFileConnLNPay(lnpayLoad):
    lnpayLoad = {"key":""}

    if os.path.isfile('lnpay.conf'): # Check if the file 'bclock.conf' is in the same folder
        lnpayData= pickle.load(open("lnpay.conf", "rb")) # Load the file 'bclock.conf'
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
        pickle.dump(lnpayLoad, open("lnpay.conf", "wb"))
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
    pickle.dump(lnpayLoad, open("lnpay.conf", "wb"))

def lnpayGetBalance():
    a = loadFileConnLNPay(['key'])
    b = str(a['key'])
    n = loadFileConnLNPay(['wallet_key_id'])
    q = str(n['wallet_key_id'])
    lnpay_py.initialize(b)
    clear()
    blogo()
    my_wallet = LNPayWallet(q)
    info = my_wallet.get_info()
    print("\n---------------------------------------------------------------------------------------------------")
    print("""
    \tLNPAY WALLET BALANCE

    Wallet ID: {}
    Wallet Name: {}
    Balance: {} sats
    """.format(info['id'], info['user_label'], info['balance']))
    print("---------------------------------------------------------------------------------------------------\n")
    input("\nContinue... ")

def lnpayCreateInvoice():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    a = loadFileConnLNPay(['key'])
    b = str(a['key'])
    n = loadFileConnLNPay(['wallet_key_id'])
    q = str(n['wallet_key_id'])
    lnpay_py.initialize(b)
    clear()
    blogo()
    my_wallet = LNPayWallet(q)
    amt = input("\nAmount in Sats: ")
    memo = input("Memo: ")
    invoice_params = {
        'num_satoshis': amt,
        'memo': memo + ' -PyBLOCK'
    }
    try:
        invoice = my_wallet.create_invoice(invoice_params)
        clear()
        blogo()
        node_not = input("Do you want to pay this invoice with your node? Y/n: ")
        while True:
            if node_not in ["Y", "y"]:
                lndconnectload = {"ip_port":"", "tls":"", "macaroon":"", "ln":""}
                lndconnectData = pickle.load(open("blndconnect.conf", "rb")) # Load the file 'bclock.conf'
                lndconnectload = lndconnectData # Copy the variable pathv to 'path'
                if lndconnectload['ip_port']:
                    print("\nInvoice: " + invoice['payment_request'] + "\n")
                    payinvoice()
                elif lndconnectload['ln']:
                    print("\nInvoice: " + invoice['payment_request'] + "\n")
                    localpayinvoice()
            elif node_not in ["N", "n"]:
                print("\033[1;30;47m")
                qr.add_data(invoice['payment_request'])
                qr.print_ascii()
                print("\033[0;37;40m")
                qr.clear()
                print("Lightning Invoice: " + invoice['payment_request'])
                t.sleep(10)
                curl = 'curl -u ' + b + ': https://api.lnpay.co/v1/lntx/' + invoice['id'] + '?fields=settled,num_satoshis'
                rsh = os.popen(curl).read()
                clear()
                blogo()
                nn = str(rsh)
                dd = json.loads(nn)
                db = dd['settled']
                if db != 1:
                    continue
                clear()
                blogo()
                tick()
                t.sleep(2)
                break
    except:
        pass

def lnpayGetTransactions():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    a = loadFileConnLNPay(['key'])
    b = str(a['key'])
    n = loadFileConnLNPay(['wallet_key_id'])
    q = str(n['wallet_key_id'])
    lnpay_py.initialize(b)
    clear()
    blogo()
    my_wallet = LNPayWallet(q)

    transactions = my_wallet.get_transactions()
    while True:
        try:
            print("\n\tLNPAY LIST PAYMENTS\n")
            for transaction_ in transactions:
                s = transaction_
                q = s['lnTx']

                print("ID: " + s['id'])
            nd = input("\nSelect ID: ")
            for transaction in transactions:
                s = transaction
                nn = s['id']
                nnn = s['lnTx']
                if nd == nn:
                    print("\n----------------------------------------------------------------------------------------------------")
                    print("""
                    \tLNPAY LIST PAYMENT DECODED

                    ID: {}
                    Amount: {} sats
                    Memo: {}
                    Invoice: {}
                    RHash: {}
                    """.format(nnn['id'], nnn['num_satoshis'], nnn['memo'], nnn['payment_request'], nnn['r_hash_decoded']))
                    print("----------------------------------------------------------------------------------------------------\n")
                    print("\033[1;30;47m")
                    qr.add_data(nnn['payment_request'])
                    qr.print_ascii()
                    print("\033[0;37;40m")
                    qr.clear()
            input("Continue...")
            clear()
            blogo()
        except:
            break
    clear()
    blogo()

def lnpayPayInvoice():
    a = loadFileConnLNPay(['key'])
    b = str(a['key'])
    n = loadFileConnLNPay(['wallet_key_id'])
    q = str(n['wallet_key_id'])
    lnpay_py.initialize(b)
    clear()
    blogo()
    my_wallet = LNPayWallet(q)
    try:
        print("\n\tLNPAY PAY INVOICE\n")
        inv = input("\nInvoice: ")
        curl = 'curl -u' + b +': https://api.lnpay.co/v1/node/default/payments/decodeinvoice?payment_request=' + inv
        clear()
        rsh = os.popen(curl).read()
        nn = str(rsh)
        dd = json.loads(nn)
        clear()
        blogo()
        print("\n----------------------------------------------------------------------------------------------------")
        print("""
        \tLNPAY INVOICE DECODED

        Destination: {}
        Amount: {} sats
        Memo: {}
        Invoice: {}
        """.format(dd['destination'], dd['num_satoshis'], dd['description'], inv))
        print("----------------------------------------------------------------------------------------------------\n")
        print("<<< Cancel Control + C")
        input("\nEnter to Continue... ")
        invoice_params = {
            'payment_request': inv
        }
        pay_result = my_wallet.pay_invoice(invoice_params)
    except:
        pass

def lnpayTransBWallets():
    a = loadFileConnLNPay(['key'])
    b = str(a['key'])
    n = loadFileConnLNPay(['wallet_key_id'])
    q = str(n['wallet_key_id'])
    lnpay_py.initialize(b)
    clear()
    blogo()
    print("""\n\tLNPAY TRANSFER BETWEEN WALLETS
    \nCaution: If you Transfer to another of your LNPay wallets
    you will only access to your funds via Web.\n""")
    try:
        wall = input("Wallet destination ID: ")
        amt = input("Amount in Sats: ")
        memo = input("Memo: ")
        my_wallet = LNPayWallet(q)
        transfer_params = {
            'dest_wallet_id': wall,
            'num_satoshis': amt,
            'memo': memo
        }
        transfer_result = my_wallet.internal_transfer(transfer_params)
        p = transfer_result['wtx_transfer_in']
        e = transfer_result['wtx_transfer_out']
        f = e['wal']
        v = p['wal']
        print("\n----------------------------------------------------------------------------------------------------")
        print("""
        \tLNPAY TRANSFER BETEWWN WALLETS INFORMATION

        ID: {}
        Amount: {} sats
        Memo: {}
        To Wallet: {}
        From Wallet: {}
        """.format(p['id'], p['num_satoshis'], p['user_label'], v['user_label'], f['user_label']))
        print("----------------------------------------------------------------------------------------------------\n")
        input("Continue...")
    except:
        pass

#-----------------------------END LNPAY--------------------------------
#-----------------------------OPENNODE--------------------------------

def loadFileConnOpenNode(opennodeLoad):
    opennodeLoad = {"key":"","wdr":"","inv":""}

    if os.path.isfile('opennode.conf'): # Check if the file 'bclock.conf' is in the same folder
        opennodeData= pickle.load(open("opennode.conf", "rb")) # Load the file 'bclock.conf'
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
        pickle.dump(opennodeLoad, open("opennode.conf", "wb"))
    clear()
    blogo()
    return opennodeLoad

def createFileConnOpenNode():
    opennodeLoad = {"key":"","wdr":"","inv":""}

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
    pickle.dump(opennodeLoad, open("opennode.conf", "wb"))

def OpenNodelistfunds():
    a = loadFileConnOpenNode(['wdr'])
    b = str(a['wdr'])
    curl = "curl https://api.opennode.co/v1/account/balance -H "+ '"Content-Type: application/json" -H "Authorization: {}"'.format(b)
    sh = os.popen(curl).read()
    clear()
    blogo()
    n = str(sh)
    d = json.loads(n)
    r = d['data']
    p = r['balance']
    print("\n----------------------------------------------------------------------------------------------------")
    print("""
    OPENNODE BALANCE

    Amount: {} sats
    """.format(p['BTC']))
    print("----------------------------------------------------------------------------------------------------\n")
    input("Continue...")

def OpenNodeCheckStatus():
    curl = "curl -X GET https://status.opennode.com/history.rss"
    sh = os.popen(curl).read()
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
        amt = input("Amount in {}: ".format(selection))
        curl = 'curl https://api.opennode.co/v1/charges -X POST -H ' + '"Authorization: {}"'.format(b) + ' -H "Content-Type: application/json" -d ' + "'{" + '"amount": "{}", "currency": "{}"'.format(amt,selection.upper()) +  "}'"
        sh = os.popen(curl).read()
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
                        lndconnectData = pickle.load(open("blndconnect.conf", "rb")) # Load the file 'bclock.conf'
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
            except:
                break
    elif fiat in ["N", "n"]:
        amt = input("Amount in sats: ")
        curl = 'curl https://api.opennode.co/v1/charges -X POST -H' + '"Authorization: {}"'.format(b) + ' -H "Content-Type: application/json" -d ' + "'{" + '"amount": "{}", "currency": "BTC"'.format(amt) +  "}'"
        sh = os.popen(curl).read()
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
                        lndconnectload = {"ip_port":"", "tls":"", "macaroon":"", "ln":""}
                        lndconnectData = pickle.load(open("blndconnect.conf", "rb")) # Load the file 'bclock.conf'
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
            except:
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
                checkcurl = 'curl https://api.opennode.co/v1/charge/decode -X POST -H "Authorization: {}" -H "Content-Type: application/json" -d '.format(b) + "'{" + '"pay_req": "{}"'.format(invoice) + "}'"
                ssh = os.popen(checkcurl).read()
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

            curl = 'curl https://api.opennode.co/v2/withdrawals -X POST -H "Content-Type: application/json" -H "Authorization: {}"'.format(b) + " -d '{" + '"type": "ln", "address": "{}", "callback_url": ""'.format(invoice) + "}'"
            sh = os.popen(curl).read()
            n = str(sh)
            d = json.loads(n)
            clear()
            blogo()
            tick()
            t.sleep(2)
        except:
            pass

    elif lnchain in ["O", "o"]:
        try:
            while True:
                print("\n\tOPENNODE TRANSFER REQUEST\n")
                print("\n\tMinimum amount 200000 sats\n")
                address = input("\nBitcoin Address: ")
                amt = int(input("Amount in sats: "))
                curl = 'curl https://api.opennode.co/v2/withdrawals -X POST -H "Content-Type: application/json" -H "Authorization: {}"'.format(b) + " -d '{" + '"type": "chain", "amount": {}, "address": "{}", "callback_url": ""'.format(amt,address) + "}'"
                if amt < 199999:
                    sh = os.popen(curl).read()
                    n = str(sh)
                    d = json.loads(n)
                    print("\n----------------------------------------------------------------------------------------------------")
                    print("""
                    \tOPENNODE TRANSFER REQUEST

                    Message: {}
                    """.format(d['message']))
                    print("----------------------------------------------------------------------------------------------------\n")
                elif amt > 200000:
                    sh = os.popen(curl).read()
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
        except:
            pass

def OpenNodeListPayments():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    a = loadFileConnOpenNode(['wdr'])
    b = str(a['wdr'])
    curl = 'curl https://api.opennode.co/v1/withdrawals -H "Content-Type: application/json" -H "Authorization: {}"'.format(b)
    sh = os.popen(curl).read()
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
                print("ID: " + s['id'] + " " + q)
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
        except:
            break

#-----------------------------END OPENNODE--------------------------------
#-----------------------------TIPPINME--------------------------------

def loadFileTippinMe(tippinmeLoad):
    tippinmeLoad = {"key":""}

    if os.path.isfile('tippinme.conf'): # Check if the file 'bclock.conf' is in the same folder
        tippinmeData= pickle.load(open("tippinme.conf", "rb")) # Load the file 'bclock.conf'
        tippinmeLoad = tippinmeData # Copy the variable pathv to 'path'
    else:
        clear()
        blogo()
        print("""\n\t   \033[1;33;40mATENTION\033[0;37;40m: YOUR CONFIGURATION INFORMATION WILL BE SAVE IN '\033[1;33;40mtippinme.conf\033[0;37;40m'
                                                                IF YOU NEED TO START AGAIN, DELETE IT.\n
        """)
        tippinmeLoad["key"] = input("Twitter @user: ")
        pickle.dump(tippinmeLoad, open("tippinme.conf", "wb"))
    clear()
    blogo()
    return tippinmeLoad

def createFileTippinMe():
    tippinmeLoad = {"key":""}
    clear()
    blogo()
    print("""\n\t   \033[1;33;40mATENTION\033[0;37;40m: YOUR CONFIGURATION INFORMATION WILL BE SAVE IN '\033[1;33;40mtippinme.conf\033[0;37;40m'
                                                                IF YOU NEED TO START AGAIN, DELETE IT.\n
    """)
    tippinmeLoad["key"] = input("Twitter @user: ")
    pickle.dump(tippinmeLoad, open("tippinme.conf", "wb"))

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
        url = 'https://api.tippin.me/v1/public/addinvoice/{}/{}'.format(b,q)
        response = requests.get(url)
        responseB = str(response.text)
        responseC = responseB
        lnreq = responseC.split(',')
        lnbc1 = lnreq[1]
        lnbc1S = str(lnbc1)
        lnbc1R = lnbc1S.split(':')
        lnbc1W = lnbc1R[1]
        ln = str(lnbc1W)
        ln1 = ln.strip('"')
        node_not = input("Do you want to pay this invoice with your node? Y/n: ")
        if node_not in ["Y", "y"]:
            lndconnectload = {"ip_port":"", "tls":"", "macaroon":"", "ln":""}
            lndconnectData = pickle.load(open("blndconnect.conf", "rb")) # Load the file 'bclock.conf'
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
            print("LND Invoice: " + ln1)
            response.close()
            input("Continue...")
    except:
        pass

#-----------------------------END TIPPINME--------------------------------
#-----------------------------TALLYCOIN------------------------------
def loadFileConnTallyCo(tallycoLoad):
    tallycoLoad = {"tallyco.conf":"","id":""}

    if os.path.isfile('tallyco.conf'): # Check if the file 'bclock.conf' is in the same folder
        tallyData= pickle.load(open("tallyco.conf", "rb")) # Load the file 'bclock.conf'
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
        pickle.dump(tallycoLoad, open("tallyco.conf", "wb"))
    clear()
    blogo()
    return tallycoLoad

def createFileConnTallyCo():
    tallycoLoad = {"fundraiser_id":"","id":""}

    clear()
    blogo()
    print("""\n\t   \033[1;33;40mATENTION\033[0;37;40m: YOU ARE GOING TO CREATE A FILE WITH YOUR INFORMATION OF CONNECTION TO TALLYCO.IN.
               WE WILL NEED SOME INFORMATION FROM YOUR ACCOUNT THAT THE ONLY ONE THAT WILL HAVE ACCESS IS YOU.
                      IF YOU DELETE THIS FILE YOU WILL NEED TO PAY AGAIN TO GET ACCESS FROM PyBLOCK.
                                       SAVE THE FILE '\033[1;33;40mtallycoSN.conf\033[0;37;40m' IN A SAFE PLACE.\n
    """)
    print("\nEXAMPLE: https://tallyco.in/s/{fundraiser_id}/\n")
    tallycoLoad["id"] = input("User ID or Twitter @USER: ")
    pickle.dump(tallycoLoad, open("tallyco.conf", "wb"))

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
        curl = "curl -d " + '"type=profile&id={}&satoshi_amount={}&payment_method={}"'.format(d, amount, lnd_onchain) + " -X POST https://api.tallyco.in/v1/payment/request/"
        tallycomethod = os.popen(curl).read()
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
            print("LND Invoice: " + f)
            qr.clear()
            input("\nContinue...")
        elif lnd_onchain == "btc":
            e = d['btc_address']
            print("\033[1;30;47m")
            qr.add_data(e)
            qr.print_ascii()
            print("\033[0;37;40m")
            print("Amount: " + d['cost'])
            print("Bitcoin Address: " + e)
            qr.clear()
            input("\nContinue...")
    except:
        pass


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
        curl = "curl -d " + '"type=profile&id={}&satoshi_amount={}&payment_method={}"'.format(donate, amount, lnd_onchain) + " -X POST https://api.tallyco.in/v1/payment/request/"
        tallycomethod = os.popen(curl).read()
        n = str(tallycomethod)
        d = json.loads(n)
        clear()
        blogo()
        if lnd_onchain in ["ln", "lN", "Ln", "LN"]:
            node_not = input("Do you want to pay this tip with your node? Y/n: ")
            if node_not in ["Y", "y"]:
                lndconnectload = {"ip_port":"", "tls":"", "macaroon":"", "ln":""}
                lndconnectData = pickle.load(open("blndconnect.conf", "rb")) # Load the file 'bclock.conf'
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
                print("LND Invoice: " + f)
                qr.clear()
                input("\nContinue...")
        elif lnd_onchain in ["btc", "bTC", "BtC", "BTC", "BTc", "btC"]:
            e = d['btc_address']
            print("\033[1;30;47m")
            qr.add_data(e)
            qr.print_ascii()
            print("\033[0;37;40m")
            print("Amount: " + d['cost'])
            print("Bitcoin Address: " + e)
            qr.clear()
            input("\nContinue...")
    except:
        pass


#-----------------------------END TALLYCOIN------------------------------
#-----------------------------MEMPOOL.SPACE------------------------------

def fee():
    try:
        while True:
            r = requests.get('https://mempool.space/api/v1/fees/recommended')
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
    except:
        pass

def blocks():
    try:
        while True:
            clear()
            blogo()
            print("\n\t             Getting New Information")
            r = requests.get('https://mempool.space/api/v1/fees/mempool-blocks')
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
    except:
        pass


#-----------------------------END MEMPOOL.SPACE------------------------------
