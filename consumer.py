import websocket

def on_open(ws):
    print("Connection opened")
    # Send a message to the WebSocket
    ws.send("Hello, Integration!")

def on_message(ws, message):
    print("Received message:", message)

def on_error(ws, error):
    print("Error:", error)

def on_close(ws):
    print("Connection closed")

# Create a WebSocket connection
ws = websocket.WebSocketApp("wss://ws.postman-echo.com/raw/",
                            on_open=on_open,
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)

# Start the WebSocket connection
ws.run_forever()
