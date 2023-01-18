import socket, threading, sys, game
import os
def ClearScreen():
    try:
        os.system("cls")
    except:
        os.system("clear")
ClearScreen()
print("Server is running")

server_name = b"pikpok"

clients = []
ready = []


def AddClient(cs, addr):
    while True:
        recv = cs.recv(1024).decode('utf-8')
        if recv == "load":
            cs.send(server_name)
        if recv[0:4] == "name": 
            cname = recv[5:]
            if cname not in clients:
                clients.append(cname)
        if recv[0:5] == "ready":
            cname = recv[6:]
            if cname not in ready:
                ready.append(cname)
            onReady()
        if recv[0:4] == "exit":
            cname = recv[5:]
            if cname in clients:
                clients.remove(cname)
            if cname in ready:
                ready.remove(cname)
        if recv[0:4] == "draw":
            cname = recv[5:]
            if cname in clients:
                game.draw(clients.index(cname))

def onReady():
    if len(ready) == len(clients):
        game.start(clients)
def updatep():
    print(f"server_name: {server_name.decode('utf-8')}") 
    print("clients")
    while True:
        print(f"\r{clients}\r", end='')
        if len(ready) == len(clients) and len(clients) != 0: 
            ClearScreen()
            break
threading.Thread(target=updatep).start()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(
        ('', 6577)
    )
    s.listen(5)
    
    while True:
        conn, addr = s.accept()
        threading.Thread(target= AddClient , args =(conn, addr)).start()