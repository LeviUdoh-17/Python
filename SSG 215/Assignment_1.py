Given_Range = range(1,61)
for num in Given_Range:
    if num % 3 == 0:
        print("Multiple of 3")
    elif num % 4 == 0:
        print("Multiple of 4")
    elif num % 3==0 and num % 4==0:
        print("Multiple of 3 and 4")
    else:
        print(num)