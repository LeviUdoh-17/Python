# Script loops through numbers 1 through 60 and states if a loop variable is a multiple of 3 or 4 or both, given it is. 
for num in range(1, 61):
    if num % 3 == 0 and num % 4 == 0:
        print(f"{num}, a multiple of 3 and 4.")
    elif num % 3 == 0:
        print(f"{num}, a multiple of 3 only.")
    elif num % 4 == 0:
        print(f"{num}, a multiple of 4 only.")
    else:
        continue