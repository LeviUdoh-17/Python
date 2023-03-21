def multiples() :
    begin = 1500
    end = 2700
    while begin <= end:
        if begin % 7 == 0 and begin % 5 == 0:
            print(begin)
        begin = begin + 1
    print(f'Done at {end}')

def list() :
    start = 0
    while start <= 6  :
        if  start != 6 and start !=  3 :
            print(start)
        start = start + 1

# The function accepts an arguement
# The function counts the number of charateers in the string 

def char_counter(string) :
    string = input('Enter a string: ')
    