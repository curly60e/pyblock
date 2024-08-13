##SN PyBlock Txs WebSocket##

import websocket

def on_message(ws, message):
    print(message)

ws = websocket.WebSocketApp("wss://bits.monospace.live/ws/txs",
                            on_message=on_message)
ws.run_forever()
