##SN PyBlock Bitaxe WebSocket##

import websocket

def on_message(ws, message):
    print(message)

ws = websocket.WebSocketApp("ws://YOUR-BITAXE-IP/api/ws",
                            on_message=on_message)
ws.run_forever()
