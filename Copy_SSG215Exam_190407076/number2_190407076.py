#The strings are defined and are also converted to lists and then into a set
string1 = "The quick brown fox jumped over the lazy dog".split()
string2 = "a brown dog and a lazy fox are similar in nature".split()
string3 = "Dami is so lazy that she could not make an effort to get brown sugar".split()
listmain = []
stringcount = []
stringbag = []
for i in range(1):
    listmain.append(string3)
for i in range(1):
    listmain.append(string2)
for i in range(1):
    listmain.append(string1)
#print(listmain)
count= 0
def characterCount(string):
#i want to find out the amount of times the words in listmain occurs in string1
    for i in range(len(string)):
        stringcount.append(0)
        # print(stringcount)
#i have added all the words in the string to the string bag
    for i in string:
       stringbag.append(i) 
# now counting
    for i in string:
        if i == stringbag[count]:
            stringcount.append(stringcount[count]+1)
            print(stringcount)
characterCount(string1)
print("done")
# newSet = string1.union(string2.union(string3))
# print(newSet)
