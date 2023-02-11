#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("100days/Mail Merge Project Start/Input/Names/invited_names.txt", "r") as name_file:
    names = name_file.readlines()

with open("100days/Mail Merge Project Start/Input/Letters/starting_letter.txt", "r") as letter_file:
    content = letter_file.readlines()
new_name = []
index = 0
for name in names:
    name_strip = name.strip("\n")
    new_name.append(name_strip)
    print(new_name[index])
    content[0] = content[0].replace(new_name[index-1], new_name[index])
    content[0] = content[0].replace("[name]", new_name[index])
    print(content[0])
    index += 1
    with open(f"100days/Mail Merge Project Start/Output/ReadyToSend/{name_strip}_letter.txt", "w") as new_letter:
        for line in content:
            new_letter.write(line)