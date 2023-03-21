from audioop import mul


def multiplication(a, b, c=None, d=None):
    if c and d:
        return a*b*c*d
    elif c:
        return a*b*c
    else:
        return a*b

a = 2
b = 3
c = 4
d = 5
f = multiplication(a, b, c, d)
print(f)