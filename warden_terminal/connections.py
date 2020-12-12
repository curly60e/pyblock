from time import time

import requests


def test_tor():
    response = {}
    session = requests.session()
    try:
        time_before = time()  # Save Ping time to compare
        r = session.get("http://httpbin.org/ip")
        time_after = time()
        pre_proxy_ping = time_after - time_before
        pre_proxy = r.json()
    except Exception as e:
        pre_proxy = pre_proxy_ping = "Connection Error: " + str(e)

    PORTS = ['9050', '9150']

    # Activate TOR proxies
    for PORT in PORTS:
        session.proxies = {
            "http": "socks5h://localhost:" + PORT,
            "https": "socks5h://localhost:" + PORT,
        }
        try:
            failed = False
            time_before = time()  # Save Ping time to compare
            r = session.get("http://httpbin.org/ip")
            time_after = time()
            post_proxy_ping = time_after - time_before
            post_proxy_difference = post_proxy_ping / pre_proxy_ping
            post_proxy = r.json()

            if pre_proxy["origin"] != post_proxy["origin"]:
                response = {
                    "pre_proxy": pre_proxy,
                    "post_proxy": post_proxy,
                    "post_proxy_ping":
                    "{0:.2f} seconds".format(post_proxy_ping),
                    "pre_proxy_ping": "{0:.2f} seconds".format(pre_proxy_ping),
                    "difference": "{0:.2f}".format(post_proxy_difference),
                    "status": True,
                    "port": PORT
                }
                return response
        except Exception as e:
            failed = True
            post_proxy_ping = post_proxy = "Failed checking TOR status. Error: " + str(
                e)

        if not failed:
            break

    response = {
        "pre_proxy": pre_proxy,
        "post_proxy": post_proxy,
        "post_proxy_ping": post_proxy_ping,
        "pre_proxy_ping": pre_proxy_ping,
        "difference": "-",
        "status": False,
        "port": "failed"
    }
    return response


def tor_request(url, tor_only=True, method="get"):
    # Tor requests takes arguments:
    # url:       url to get or post
    # tor_only:  request will only be executed if tor is available
    # method:    'get or' 'post'
    # Store TOR Status here to avoid having to check on all http requests
    TOR = test_tor()
    if TOR["status"] is True:
        try:
            # Activate TOR proxies
            session = requests.session()
            session.proxies = {
                "http": "socks5h://localhost:" + TOR['port'],
                "https": "socks5h://localhost:" + TOR['port'],
            }
            if method == "get":
                request = session.get(url, timeout=15)
            if method == "post":
                request = session.post(url, timeout=15)

        except (
                requests.exceptions.ConnectionError,
                requests.exceptions.ReadTimeout,
        ) as e:
            return "ConnectionError"
    else:
        if tor_only:
            return "Tor not available"
        try:
            if method == "get":
                request = requests.get(url, timeout=10)
            if method == "post":
                request = requests.post(url, timeout=10)

        except requests.exceptions.ConnectionError:
            return "ConnectionError"

    return request
