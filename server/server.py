# echo-server.py

import socket
import datetime 
import time
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Turned on socket")
    s.bind((HOST, PORT))
    print("Binded adress and port")
    s.listen()
    print("Started to search for a client")
    conn, addr = s.accept()
    print(f"Connected to {conn}, {addr}")
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if data:
                print(f"{data} , sent at {datetime.datetime.now()}")
            
            conn.sendall(data)
            time.sleep(0.1)