#the IF statement
print('the IF statement')
x = int(input("Please enter an integer: "))
if x < 0: 
    x=0
    print('Negative changed to zero')
elif x == 0: 
    print('Zero') 
elif x == 1: 
    print('Single') 
else: 
    print('More') 

#the WHILE statement
print('\nthe WHILE statement')
# Fibonacci series: 
	# the sum of two elements defines the next 
a, b = 0, 1 
while b < 20: 
    print(b) 
   # a = b
    # b = a + b
    a, b = b, a + b

#the FOR statement
print('\nthe FOR statement')
schools = ['unilag', 'funaab', 'convenant_university', 'uniport', 'eksu']
for school in schools:	   	
    print(school, len(school))

# The SLICE notation
print('\nthe SLICE notation')
for school in schools[0:1]:
    if len(school) > 6:
        schools.insert(0, school)
print(schools)

# The Range Function
# If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy. 
# It generates arithmetic progressions: 
# The given end point is never part of the generated sequence 

print('\nthe RANGE function')
for i in range(5):
    print(i)

for i in range(len(schools)):		
    print(i, schools[i])

# It is possible to let the range start at another number, or to specify a different increment (even negative; 
# sometimes this is called the ‘step’): 

# range(5, 10) 5 through 9 
# range(0, 10, 3) 0, 3, 6, 9 
# range(-10, -100, -30) -10, -40, -70 


# for i in range(-10, -100, -30):
#     print(i)

# Break and continue statements

# The BREAK statement breaks out of the innermost enclosing 'for' or 'while' loop. 
# Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the list (with for)
# or when the condition becomes false (with while), but not when the loop is terminated by a break statement. 

print('\nthe BREAK statement')
#Determining the prime numbers between 2 and 9
for n in range(2, 10): 
    for x in range(2, n):
        if n % x == 0: 
             print(n, 'equals', x, '*', n//x) #The “//” operator is used to return the closest integer value which is less than or equal to a specified expression or value.
             break
        else: 
            print(n, 'is a prime number')

# The CONTINUE statement continues with the next iteration of the loop: 
print('\nthe CONTINUE statement')
#Determining the even numbers between 2 and 9
for num in range(2, 10): 
    if num % 2 == 0:		
        print("Found an even number", num) 
        continue 
    print("Found a number", num) 

#ENUMERATE
# Another built-in Python function that takes input as iterator, list etc. and 
# returns a tuple containing index and data at that index in the iterator sequence. 

print('\nthe ENUMERATE function') 
for i, x in enumerate(schools):  print("%s  %s" %(i, x))  

#ZIP
# Another in-built python function which is helpful to combine similar types of iterators (list-list or dictionary- dictionary etc.) data items at ith position. 
# It uses the shortest length of these input iterators. 
# Other items of larger length iterators are skipped.
print('\nthe ZIP function')
states = ['Lagos', 'Ogun', 'Ogun', 'Rivers', 'Ekiti']  
for school,state in zip(schools, states):   
   print("%s is in %s state" %(school, state))

# PASS
# The pass statement is used as a placeholder for future code.
# When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.
# Empty code is not allowed in loops, function definitions, class definitions, or in if statements.

# try statement
# The try statement specifies exception handlers and/or cleanup code for a group of statements.
for x in [0, 1, 2]:
      pass

# EXCEPT clause or statement is a place that contains code to handle the exception or error raised in TRY block and multiple except clauses while a single try statement clause can be added into the code. 
# In the below example, print command will raise a ‘TypeError’ because %d is expecting integer value
print('\nthe TRY-EXCEPT block')
try:  
    for i in range(len(schools)):        
            print("%d" %schools[i])   
except TypeError:   
    print('oops! Type error')