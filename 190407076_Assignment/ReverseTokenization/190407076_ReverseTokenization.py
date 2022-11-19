# Take the alphabets that form a sentence into a 
# list with special characters or blanks if needed.

# Create the sentence from this list in a reverse 
# process of the tokenization into alphabets using 
# three examples in the calss of Thursday Jan 13.

# def seperate(word):
#     """Appends the characters in a string to a list"""
#     newList = []
#     for char in word:
#         newList.append(char)
#     return newList
# word = "Programmers"
# print(seperate(word))

# def seperateSentence(sentence):
#     """Seperates the words into a list"""
#     newList = [char for char in sentence if sentence != ' ']
#     newWord = ''.join([x for x in sentence])
#     result = [newList, newWord]
#     return result
# sentence = "Programmers are solution providers"
# print(seperateSentence(sentence)[0])
# print(seperateSentence(sentence)[1])

another_sentence = "This is my third assignment"
wlist = another_sentence.split()
clist = []
for word in wlist:
    for char in word:
        clist.append(char)
print(clist)
print(' '.join(wlist))
