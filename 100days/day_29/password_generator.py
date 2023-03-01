import string
import random

def generate_password():
    alphabets = string.ascii_lowercase
    alphabets_c = string.ascii_uppercase
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    special_characters = ['!', '@', '#', '$', '%', '&', '*', '_', '.']
    character_distribution = ['alphabets', 'alphabets_c', 'numbers', 'special_characters']
    random.shuffle(character_distribution)
    random_alphabets, random_numbers, random_special_characters, random_alphabets_c  = '', '', '', ''
    password = ''
    for elements in character_distribution:
        if elements == 'alphabets':
            for characters in alphabets:
                if len(random_alphabets)<6:
                    random_alphabets += random.choice(alphabets)
            password += random_alphabets
        if elements == 'numbers':
            for characters in numbers:
                if len(random_numbers)<5:
                    random_numbers += str(random.choice(numbers))
            password += random_numbers
        if elements == 'alphabets_c':
            for characters in alphabets_c:
                if len(random_alphabets_c)<2:
                    random_alphabets_c += random.choice(alphabets_c)
            password += random_alphabets_c
        if elements == 'special_characters':
            for characters in special_characters:
                if len(random_special_characters)<2:
                    random_special_characters += random.choice(special_characters)
            password += random_special_characters
    return password