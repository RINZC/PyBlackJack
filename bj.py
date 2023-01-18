from bjc import *
import numpy as np

class Deck:
    def __init__(self):
        self.cards = []
        for card in card_count_dicts:
            count = card_count_dicts[card]
            # for c in range(count-1):
            self.cards.append(card)
        np.random.shuffle(self.cards)
        # print(self.cards)
    def _draw(self):
        ncard = self.cards[-1]
        self.cards.remove(self.cards[-1])
        return ncard
    def pcards(self):
        print("\n- Deck -")
        print(self.cards)
        print("\n")

class Client:
    def __init__(self, pname):
        self.pname = pname
        self.onHand = []
        self.onHandValues = []
        self.lp = 1
    
    def pHand(self):
        print(f"{self.pname}")
        print(f"card   :{self.onHand}")
        print(f"values :{self.__OnHandValues()}")
        print(f"sum    :{sum(self.__OnHandValues())}\n")
    
    def _draw(self, name):
        if name in card_count_dicts:
            if self.lp != 0:
                self.onHand.append(name)
                self.pHand()
                if sum(self.__OnHandValues()) == 21:
                    print(f"{self.pname} win !!!")
                    print("- scores -")
                    exit()
                if sum(self.__OnHandValues()) > 21:
                    print(f"{self.pname} lose !!!")
                    print("- scores -")
                    exit()
            else:
                print(f"{self.pname} dead!!")
        else:
            print(f"this card [ {name} ] does not exist")
        
    def __GetCardValue(self, name):
        Fn = name.replace("c", ' ').replace("h", ' ').replace("b", ' ').replace("d", ' ')
        Fn.split(' ')
        f = Fn[0] if len(Fn) == 2 else "10"
        return card_values_dicts[f]
    def __OnHandValues(self):
        vR = []
        for name in self.onHand:
            vR.append(self.__GetCardValue(name))
        return vR
         


