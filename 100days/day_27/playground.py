#Unlimited positional arguments
def add(*arg):
    sum = 0
    for num in arg:
        sum += num
    return sum

print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 5))

def calculate(n, **kwargs):
    print(n, kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
calculate(2, add=2, multiply=3)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

myCar = Car(make="Honda", model="Elantra")
print(myCar.model)
