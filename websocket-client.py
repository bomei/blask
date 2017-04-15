from websocket import create_connection
ws=create_connection("ws://localhost:12345/chat")
print('sending hello')
ws.send('hello')
result = ws.recv()
print('[Receive]',result)
result = ws.recv()
print('[Receive]',result)
ws.close()
#
# from socketIO_client import SocketIO, LoggingNamespace, BaseNamespace
#
#
# def on_response(*args):
#     print('on_response',args)
#
#
# # socketIO.emit('my_event', {'data': 'bobo'})
# # socketIO.on('my_response', on_response)
# socketIO = SocketIO('localhost')
# socketIO.on('my_response', on_response)
# socketIO.emit('my_event',{'data':'hello'}, path='/test')
# socketIO.wait(seconds=10)
