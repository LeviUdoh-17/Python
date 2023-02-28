# #For Loop
# numbers = [1, 2, 3, 4]
# new_list = []
# for n in numbers:
#     add_1 = n+1
#     new_list.append(add_1)
# #list comprehension
# new_number = [n+1 for n in numbers]
# print(numbers, new_number)

# #String as Lists
# name = 'Levi Udoh'
# name_list = [char for char in name]
# print(name_list)

# #range as a sequence
# sequence = range(1, 5)
# new_list = [num*2 for num in sequence]
# print(new_list)

# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# short_names = [name for name in names if len(name)<5]
# print(short_names)
# long_names = [name.upper() for name in names if len(name)>4] 
# print(long_names)

#dictionary comprehension
import random
import pandas
new_names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
students_scores = {student:random.randint(1, 100) for student in new_names}
passed_students = {student:score for student,score in students_scores.items() if score >=60}
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}
students_data_frame = pandas.DataFrame(student_dict)
print(students_data_frame)
for(index, row) in students_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)