#def sep(word):
#   return [char for char in word]
#sentOne = 'the quick brown fox jumps over the lazy dog'
#listOne = sentOne.split()
#firstList = sep(listOne[0])
#firstSet = set(firstList)
#for word in listOne[1:]:
#    firstSet = set(sep(word)).union(firstSet)

#print(len(firstSet))

def sep(word):
    return [char for char in word]
sentOne = 'the quick fox jumped over the lazy dog'
listOne = sep(sentOne)
print(listOne)
firstSet = set(listOne)
print(firstSet)
print(len(firstSet))