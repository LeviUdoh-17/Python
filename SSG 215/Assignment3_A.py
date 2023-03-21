count = 1
while count <= 60 :
    if count % 3 == 0  and count % 4 == 0:
        print('Multiple of 3 and 4')
    elif count % 3 == 0:
        print('Multiple of 3')
    elif count % 4 == 0:
        print('Multiple of 4')
    else:
        print(count)
    count = count + 1
 
