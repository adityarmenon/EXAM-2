seed = 94687

a = 8375
c= 928475
m =2**32

def rng():
    global seed
    seed = (a*seed +c)%m
    return seed

for i in range(10):
    print(rng())
    