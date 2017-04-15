from websocket import create_connection
ws=create_connection("ws://localhost:12345")
print('sending hello')
ws.send('hello')
result = ws.recv()
print('[Receive]',result)
ws.close()