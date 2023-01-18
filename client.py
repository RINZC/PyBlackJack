import sys
import socket
import os

address = socket.gethostbyname(socket.gethostname())

def ClearScreen():
    try:
        os.system("cls")
    except:
        os.system("clear")
        
def LoadData():
    s.send("load".encode("utf-8"))
    return s.recv(4096).decode("utf-8")

def Connect():
    s.send(f"name {name}".encode("utf-8"))

def main():
    Connect()
    ClearScreen()
    Data = LoadData()
    print("- Wellcome to The . BlackJack -\n")
    print(f"server    : {serv} {Data}")
    print(f"username  : {name}")
    print(f"address   : {address} \n")
    while True:
        red = input(" - enter - ")
        if red == "ready":
            s.send(f"ready {name}".encode("utf-8"))
        if red == "draw":
            s.send(f"draw {name}".encode("utf-8"))
        if red == "exit":
            s.send(f"exit {name}".encode("utf-8"))
            exit()
            
    
def buildAddr(s):
    return (s.split(':')[0], int(s.split(':')[1]))
try:
    ClearScreen()
    serv = buildAddr(sys.argv[1])
    name = sys.argv[2]
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(serv)
            main()
except:
    p = 0
    try:
        serv = buildAddr(str(input("server_address : ")))
        name = str(input("user_name      : "))
        p=1
    except:
        print("server_address -> ipv4:port ")
    if p!= 0: 
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(serv)
            main()