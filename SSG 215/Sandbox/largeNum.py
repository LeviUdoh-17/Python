import random

score = [1, 2, 3, 5, 6, 8]
trial = 0

while  trial <= 5 :
    randomNumber = random.randint(1, 8)
    randomNumber = int(randomNumber)
    if trial < 5 :
        if randomNumber < 7 and randomNumber != 8 and randomNumber in score :
            print(f'{randomNumber} is too low, try again later') 
        elif randomNumber > 8 and randomNumber in score and randomNumber != 8 :
            print(f'{randomNumber} is not the highest number. Try again, it is too high')
        elif randomNumber == 8 :
            print('Congratulations, 8 is the correct number')
            break
        elif trial > 5 :
            print('I lost!!')
        else :
            print('The chosen number not in score, please try again')
    trial = trial + 1
print('Done')
