import pandas as pd

data = pd.read_csv("100days/NATO-alphabet-start/nato_phonetic_alphabet.csv")
#Todo 1. Create a dictionary format
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#Todo 2. Create a list of phonetic words from a word that the user inputs.
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()