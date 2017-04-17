from websocket import create_connection
import json
import serial.tools.list_ports
import serial
import time
import threading

ws = create_connection("ws://zannb.site:9999/chat")
serial1 = serial.Serial(
    port='com3',
    baudrate=9600
)


def serial_send(s):
    s += '\r\n'
    s = s.encode()
    s = list(s)
    s = [len(s)] + s
    data = bytes(s)
    # print(data)
    print(serial1.write(data))


def rev():
    while 1:
        time.sleep(0.1)
        r = ws.recv()
        print(r)
        message = json.loads(r)['message']
        if 'led' in message.lower():
            serial_send(message)


def serial_rx():
    while 1:
        time.sleep(0.1)
        n = serial1.inWaiting()
        if n > 0:
            print(n)
            data = serial1.read(n)
            try:
                print('[{}] -> [{}]'.format(data, data.decode('utf-8')))
            except:
                print('[EXCEPTION], can\'t decode as utf-8')
                print(data)


t1 = threading.Thread(name='web_rx', target=rev)
t1.start()
t2=threading.Thread(name='uart_rx',target=serial_rx)
t2.start()

while 1:
    s = input()
    ws.send(s)
