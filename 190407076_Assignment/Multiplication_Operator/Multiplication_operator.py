# __Homework 1___
# _Create and test a functional equivalent of the multiplication operation that is capable of up to five arguments._
# >>>>
def Multipy(num1, num2, num3=None, num4=None, num5=None):
    """Multipys the given parameters"""
    if (num3 and num4 and num5):
        result = num1*num2*num3*num4*num5
    elif (num3 and num4):
        result = num1*num2*num3*num4
    elif (num3):
        result = num1*num2*num3
    else:
        result = num1*num2
    return result
print(Multipy(2, 4, 6, 8, 10))
print(Multipy(1, 3, 5, 7))
print(Multipy(2, 4, 6))
print(Multipy(1, 3))