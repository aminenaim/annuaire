import socket
from request import *

# HEADER = 64
# FORMAT = 'utf-8'

# PORT = 5050
# HOST = socket.gethostbyname(socket.gethostname()) # gets the current hostname IP
# ADDR = (HOST, PORT)

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(ADDR)

def send(request: request):
    formatted_request = request.dump()
    encoded_request = formatted_request.encode(FORMAT)

    request_len = len(encoded_request)
    
    request_len = str(request_len).encode(FORMAT)
    
    request_len += b' '* (HEADER - len(request_len))
    client.send(request_len)
    client.send(encoded_request)
    print(client.recv(2048).decode(FORMAT))


request = request(requestType.AUTH,['admin','admin'])

req = request.dump()
re = request(0, [""])
re.load()
print(req)


send(request)
