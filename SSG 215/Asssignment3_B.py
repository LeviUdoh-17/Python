import random

times_generated = 0

while times_generated <= 10 :
    generated_number = random.randint(1, 16)
    if generated_number % 2 == 0:
        print(f'{generated_number} is an even number.') 
    else :
        print(f'{generated_number} is a odd number.')
    times_generated = times_generated + 1