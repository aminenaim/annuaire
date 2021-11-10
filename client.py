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
    message_len = len(message)
    send_len = str(message_len).encode(FORMAT)
    send_len += b' '* (HEADER - len(send_len))
    client.send(send_len)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("Hello World ")
send("DISCONNECT")