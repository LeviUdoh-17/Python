# # File  not Found
# try:
#     #Something that could go wrong
#     file = open("100days/day_30/a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     #Do this if something is wrong
#     file = open("100days/day_30/a_file.txt", "w")
#     file.write("Something there")
# except KeyError as errormessage:
#     print(f"The Key {errormessage} doesn't exist")
# else:
#     content=file.read
#     print(content)
# finally:
#     #How to raise an error
#     raise TypeError("This is the error I made up")

#Where should a error be raised
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be more than 3 meters.")

bmi = weight / height ** 2
print(bmi)