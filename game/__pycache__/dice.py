import matplotlib.pyplot as plt
import random
import statistics as sts

dice = [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1],
    [1, 1],
    [1,],
]



def get_loop(r1=100, r2=2**(10)):
    ymode = []
    xmode = []
    for u in range(r1):
        
        xmode.append(u+1)
        xresult = []
        yresult = []
        plt.title("dicier")

        for x in range(r2):
            yresult.append(x+1)
            x = random.randrange(5)
            xresult.append(sum(dice[x]))
        _xmode = sts.mode(xresult)
        ymode.append(_xmode)
        # print( xmode, '\r') 
    return (xmode, ymode)
        
        

for o in range(100):
    x, y = get_loop()
    plt.plot(
        x,
        y,
        '-',
        label = f"L{o+1}"
    )

plt.legend()
plt.show()