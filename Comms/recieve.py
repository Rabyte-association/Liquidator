import simple_websocket

#baardzo nie działa

def echo():
    ws = simple_websocket.Server("ws://192.168.0.69:8765")
    try:
        while True:
            data = ws.receive()
            ws.send(data)
    except simple_websocket.ConnectionClosed:
        pass
    return ''

if __name__ == '__main__':
    echo()