givenNumber = 11
givenNumberString = str(givenNumber) 
inputLength = len(givenNumberString)


givenStringReverse = ''
givenStringReverseIndex = ''

for charc in reversed(givenNumberString):
    givenStringReverse += charc
    givenStringReverseIndexcount = givenStringReverse.index(charc)
    givenStringReverseIndex += str(givenStringReverseIndexcount)

print(givenStringReverse, givenStringReverseIndex)
romanNumeral = ''
for i in givenStringReverseIndex:
    if i == '0':
        for i in reversed(givenNumberString):
            arabicNumr = int(givenStringReverse)
            print(arabicNumr)
        if arabicNumr <= 3 and arabicNumr >=1:
            romanNumeral = 'i' *  arabicNumr
        elif arabicNumr == 4:
            romanNumeral = 'iv'
        elif arabicNumr == 5:
            romanNumeral = 'v'
        elif arabicNumr < 9 and arabicNumr > 5:
            remainder = arabicNumr - 5
            remainderRoman = ('i') * remainder
            romanNumeral = 'v' + remainderRoman
        elif arabicNumr == 9:
            romanNumeral = 'ix'
        else: 
            continue

    elif i == '1':
        for i in reversed(givenNumberString):
            arabicNumr = int(givenStringReverse)
            print(arabicNumr)
        if arabicNumr <= 3 and arabicNumr >=1:
            romanNumeral = 'x' *  arabicNumr
        elif arabicNumr == 4:
            romanNumeral = 'xl'
        elif arabicNumr == 5:
            romanNumeral = 'l'
        elif arabicNumr < 9 and arabicNumr > 5:
            remainder = arabicNumr - 5
            remainderRoman = ('x') * remainder
            romanNumeral = 'l' + remainderRoman
        elif arabicNumr == 9:
            romanNumeral = 'xc'
        else:
            continue
    
print(romanNumeral)