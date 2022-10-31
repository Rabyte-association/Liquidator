import simple_websocket
#import encode

#bardzo bardzo nie działa

def send():
    ws = simple_websocket.Client('ws://192.168.0.69:8765')
    try:
        while True:
            data = input('> ')
            ws.send(data)
            data = ws.receive() 
            print(f'< {data}')
    except (KeyboardInterrupt, EOFError, simple_websocket.ConnectionClosed):
        ws.close()

send()