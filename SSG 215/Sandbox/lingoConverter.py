language = input('Greeting in what language: ')
def lingo_converter(language) :
    if language == 'French' :
        return 'Bonjour'
    elif language == 'Spanish' :
        return 'Hola'
    elif language == 'Engish':
        return 'Hello'
    else:
        return 'Coming soon'

print(f'{lingo_converter(language)} Levi')
