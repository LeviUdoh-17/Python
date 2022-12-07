#Lambda can be used instead of functions it has it's up's and down's 
#I actually prefer the use of normal functions because it is more readable and beginner friendly
str1 = 'Ukaraobong1'
#lambda returns a function object
rev_upper = lambda string: string.upper()[::-1]
print(rev_upper(str1))