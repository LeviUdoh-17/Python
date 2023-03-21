#def plus(a, b, c=None, d=None):
 #   if c and d:
 #       return a+b+c+d
  #  elif c:
   #     return a+b+c
    #else:
     #   return a+b
    
#a = 4
#b = 3
#c = -3
#d = -4
#f = plus(a, b)
#h = plus(a, b, c, d)

#print(f, h)

import operator

def plus(a, b, c=None, d=None):
    if c and d:
        return operator.add(operator.add(a,b), operator.add(c,d))
    elif c:
        return operator.add(operator.add(a, b), c)
    else:
        return operator.add(a,b)

a = 1
b = 2
c = 3
d = 4
print(plus(a, b, c))
