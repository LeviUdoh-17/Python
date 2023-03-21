import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess =int( input(f'Enter a number 1 and {x}: '))
        if guess < random_number:
            print('The number guessed is too low, try again.')
        elif guess > random_number: 
            print('The number is greater, please try again.')
        else:    
            print('Congrats!!! You got the number right.')

guess(10)


