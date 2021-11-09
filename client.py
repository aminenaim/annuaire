import socket

HEADER = 64
FORMAT = 'utf-8'

PORT = 5050
HOST = socket.gethostbyname(socket.gethostname()) # gets the current hostname IP
ADDR = (HOST, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(string):
    message = string.encode(FORMAT)
    message_length = len(message)
    send_length = str(message_length).encode(FORMAT)
    send_length += b' '* (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("Hello World ")
send("DISCONNECT")