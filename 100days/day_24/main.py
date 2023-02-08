#This is to read my_file.txt on the terminal.
# with open("100days/day_24/my_file.txt") as file:
#     contents = file.read()
#     print(contents)
#This is to add text to an already existing text
with open("100days/day_24/my_file.txt", mode='a') as file:
    file.write("New text")
# This is used to overwrite or create a text file with text
with open("100days/day_24/new_file.txt", mode='w') as file:
    file.write("New")
