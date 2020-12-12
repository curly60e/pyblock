import json
import os
import csv

import requests

from connections import tor_request


# Returns the current application path
def current_path():
    application_path = os.path.dirname(os.path.abspath(__file__))
    return (application_path)


# Returns the home path
def home_path():
    from pathlib import Path
    home = str(Path.home())
    return (home)


def GBTC_premium(price, btc, shares):
    if btc == 0:
        return 0, 0
    fairvalue = btc * shares
    premium = (price / fairvalue) - 1
    return fairvalue, premium


def fxsymbol(fx, output='symbol'):
    # Gets an FX 3 letter symbol and returns the HTML symbol
    # Sample outputs are:
    # "EUR": {
    # "symbol": "",
    # "name": "Euro",
    # "symbol_native": "",
    # "decimal_digits": 2,
    # "rounding": 0,
    # "code": "EUR",
    # "name_plural": "euros"
    filename = os.path.join(current_path(), 'static/json_files/currency.json')
    with open(filename) as fx_json:
        fx_list = json.load(fx_json)
    try:
        out = fx_list[fx][output]
    except Exception:
        if output == 'all':
            return (fx_list[fx])
        out = fx
    return (out)


def multiple_price_grab(tickers, fx):
    # tickers should be in comma sep string format like "BTC,ETH,LTC" and "USD,EUR"
    baseURL = \
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms="\
        + tickers + "&tsyms=" + fx + "&&api_key=9863dbe4217d98738f4ab58137007d24d70da92031584ba31de78137e0576225"
    try:
        request = tor_request(baseURL)
    except requests.exceptions.ConnectionError:
        return ("ConnectionError")
    try:
        data = request.json()
    except AttributeError:
        data = "ConnectionError"
    return (data)


def fx_list():
    filename = os.path.join(current_path(),
                            'static/csv_files/physical_currency_list.csv')
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        fiat_dict = {rows[0]: (rows[1]) for rows in reader}
    # Convert dict to list
    fx_list = [(k, k + ' | ' + v) for k, v in fiat_dict.items()]
    fx_list.sort()
    return (fx_list)


def is_currency(id):
    # Return true if id is in list of currencies
    found = ([item for item in fx_list() if item[0] == id])
    if found != []:
        return True
    return False
