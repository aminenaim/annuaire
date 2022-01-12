import socket
import threading
from request import *

HEADER = 64
FORMAT = 'utf-8'

PORT = 5050
HOST = socket.gethostbyname(socket.gethostname()) # gets the current hostname IP
ADDR = (HOST, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR) # binding socket to address

def handle_client(conn, addr):
    """
    Handles connection with a client. Serves only one client and then exits.
    """
    print(f"[NEW CONNECTION] {addr} connected.")
    
    connected = True
    while connected == True:
        request_len = conn.recv(HEADER).decode(FORMAT)

        if request_len:
            request_len = int(request_len)
            formatted_request = conn.recv(request_len).decode(FORMAT)
            
            # r = request.load(formatted_request)
    
            # if r.rtype == 7:
            #     connected = False
            
            
            print(f"[{addr}] {formatted_request}")
            conn.send("message received".encode(FORMAT))

            if formatted_request == "quit":
                print("quit request received")
                connected = False

    conn.close()
        

def start():
    """
    
    """
    server.listen()
    while True:
        conn, addr = server.accept() # storing connection object and address of connection 
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print("[ACTIVE CONNECTIONS]", threading.active_count()-1)
    


print("[STARTING] server is starting...")
print(f"[LISTENING] server is listening on {HOST}")
start()
