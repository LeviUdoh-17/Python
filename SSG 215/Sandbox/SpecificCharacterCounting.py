word = input('Input the word: ')
letter = input('input the letter: ')
count = 0
for this in word :
    index = 0
    if index < len(word) :
        if this is 'a' :
            count = count + 1
            print('I got one!')
        else :
            print('Nah, I am on to the next one')
print(f'Done/, i got {count}')