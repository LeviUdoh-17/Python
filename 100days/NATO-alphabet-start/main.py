import pandas
# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

# with open("100days/NATO-alphabet-start/nato_phonetic_alphabet.csv", "r") as file:
#     content = (file.readlines())
# print(alphabetic_dicts[1]["letter"])
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
alphabetic_dict = pandas.read_csv("100days/NATO-alphabet-start/nato_phonetic_alphabet.csv")
alphabetic_dicts = {word.letter: word.code for (index, word) in alphabetic_dict.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Input a word: ")
phonetic_list = [alphabetic_dicts[letter] for letter in user_input.upper()]
print(f"Phonetic code words for {user_input} = {phonetic_list}")

