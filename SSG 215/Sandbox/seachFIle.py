userInput = input('What is it you are looking for : ')
limitFile = open('Sandbox/Limit.py')
frequency = 0
for string in limitFile :
    frequency = frequency + 1
    if string.startswith(f'{userInput}') :
        print(f'Found, line {frequency}')
        print (string)
    else :
        print('Not Found')