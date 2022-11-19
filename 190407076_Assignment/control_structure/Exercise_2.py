# Script continuously generates a random integer between 1 and 15 inclusively as long as the value generated is less than or equal to 10. 
# Script also states if the number generated is an even or odd number i.e., if 1 is generated, it prints 1 is an odd number, if 6 is generated, it prints 6 is an even number
from random import randint
for num in randint(1, 15):
    if num <= 10:
        if num % 2 == 0:
            print(f"{num} is an odd number")
        else:
            print(f"{num} is an even number")