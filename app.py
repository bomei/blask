from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'


def get_my_ip():
    import socket
    #获取本机电脑名
    myname = socket.getfqdn(socket.gethostname(  ))
    #获取本机ip
    myaddr = socket.gethostbyname(myname)
    print(myname)
    print(myaddr)


if __name__ == '__main__':
    app.run(port=12345)
