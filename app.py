from flask import Flask, render_template
import requests
import serial.tools.list_ports

app = Flask(__name__)


@app.route('/')
def root():
    return 'hello'


@app.route('/hello')
@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template('hello.html', name=name)


@app.route('/show_com')
def show_coms():
    plist = serial.tools.list_ports.comports()
    ans = ''
    for com in plist:
        ans += '{} - {}<br>'.format(com.device, com.description)
    return ans


def get_my_ip():
    import socket
    # 获取本机电脑名
    name = socket.getfqdn(socket.gethostname())
    # 获取本机ip
    addr = socket.gethostbyname(name)
    print(name)
    print(addr)


if __name__ == '__main__':
    app.run(port=12345)
