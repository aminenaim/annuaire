import socket
import threading

HEADER = 64
FORMAT = 'utf-8'

PORT = 5050
HOST = socket.gethostbyname(socket.gethostname()) # gets the current hostname IP
ADDR = (HOST, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR) # binding socket to address

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    
    connected = True
    while connected:
        message_lenght = conn.recv(HEADER).decode(FORMAT)

        if message_lenght:
            message_lenght = int(message_lenght)
            message = conn.recv(message_lenght).decode(FORMAT)

            if message == "DISCONNECT":
                connected = False
            
            print(f"[{addr}] {message}")
            conn.send("message received".encode(FORMAT))

    conn.close()
        

def start():
    server.listen()
    while True:
        conn, addr = server.accept() # storing connection object and address of connection 
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print("[ACTIVE CONNECTIONS]", threading.active_count()-1)

print("[STARTING] server is starting...")
print(f"[LISTENING] server is listening on {HOST}")
start()