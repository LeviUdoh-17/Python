#Takes the alphabet that form a sentence into a list with special characters or a blank if needed
def sep(word):
    return [char for char in word]
sentOne = 'the quick fox jumped over the lazy dog'
listOne = sep(sentOne)
firstSet = set(listOne)

#Creates the sentence from the list in a reverse process of the tokenization into alphabets using the three examples in the previous class
def reverseTokenization(list):
    newlist = ""
    newSentence = newlist.join(list)
    print(newSentence)

reverseTokenization(listOne)