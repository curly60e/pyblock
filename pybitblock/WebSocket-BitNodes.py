##SN PyBlock BitNodes WebSocket##

import websocket

def on_message(ws, message):
    print(message)

ws = websocket.WebSocketApp("wss://bitnodes.io/ws-bitcoind/bitcoind",
                            on_message=on_message)
ws.run_forever()
