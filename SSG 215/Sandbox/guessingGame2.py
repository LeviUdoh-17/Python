import random
# Create a function guess
def guess(x):
    # Ask the user to pick a number.
    random_number = int(input (f'Enter a number from 1 to {x}: '))
    # Create a loop in which the computer guesses the number, and also sending the feedback of whether the computer guessed it right or not.
    guess = 0
    while guess != random_number:
        guess = random.randint(1, x)
        if guess < random_number:
            print(f'O boy, I guessed it wrong, {guess} is too low')
        elif guess > random_number:
            print(f'O boy, I guessed it wrong, {guess} is too high')
        else:
            print('Yes!! I got it right.')

# Call the function Guess()
guess(10)