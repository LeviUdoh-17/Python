import random
Gen = random.randint(1, 15)
while Gen <= 10 :
    Gen = random.randint(1, 15)
    if Gen % 2 == 0:
        print(Gen, 'is an even number')
    elif Gen % 3 == 0:
        print(Gen, 'is an odd number')
    

