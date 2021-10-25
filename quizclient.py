import socket
from threading import Thread

nickname = input('Please enter your nickname ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ipAdress = '127.0.0.1'
port = 5080

client.connect((ipAdress, port))

print("Connected with server")

def receive():
    while True:
        try:
            message = client.recv(2048).decode('utf-8')

            if message == 'NICKNAME':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occured")
            client.close()
            break

def write():
    while True:
        message = '{} : {}'.format(nickname, input(''))
        client.send(message.encode('utf-8'))

receive_thread = Thread(target = receive)
receive_thread.start()
write_thread = Thread(target = write)
write_thread.start()