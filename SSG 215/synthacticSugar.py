def listDict(listIn):
    cDict = {}
    for num in set(listIn):
        cDict[num] = listIn.count(num)
    return cDict

listIn = 'Levi is coding'
print(listDict(listIn))
 

