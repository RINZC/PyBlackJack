from bj import *

deck = Deck()
current_turns = ''
clients_Hand = []
start = False
def start(clients):
    start = True
    for x in clients:
        clients_Hand.append(Client(x))
def draw(client_index):
    clients_Hand[client_index]._draw(deck._draw())