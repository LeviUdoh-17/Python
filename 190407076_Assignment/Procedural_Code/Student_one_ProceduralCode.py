student100 = [
      #Lists of students
]
student200 = [
      #Lists of student officials
]

def average(grade):
        """To calculate average values in a dictionary"""
        score_sum = 0
        isTrue = True
        for score in grade:
            score_sum += score
        return score_sum/len(grade)
def ranking(cgpa):
        rank = ""
        if cgpa >= 4.50 and cgpa <= 5.00:
                rank = "First Class"
        elif cgpa >= 3.50 and cgpa <= 4.49:
                rank = "Second Class Upper"
        elif cgpa >= 2.40 and cgpa <= 3.49:
                rank = "Second Class Lower"
        elif cgpa >= 1.50 and cgpa <= 2.39:
                rank = "Third Class Lower"
        else:
                rank = "Pass"
        return rank                        

def addStudent100(student):
        student100.append(student)

def addStudent200(official):
        student200.append(official)

addStudent100({
        'Name': "Udom Samuel",
        'Matric Number': 210407021,
        'Grades': {"GEG115" : 78, "GEG117" : 89, "FSC112" : 75, "FSC115" : 80}
        })        
addStudent100({
        'Name': "James Prince", 
        'Matric Number': 210407013, 
        'Grades': {"GEG115" : 90, "GEG117" : 88, "FSC112" : 85, "FSC115" : 80}
        })
addStudent100({
        'Name': "Ademola Eunice",
        'Matric Number': 210407076,
        'Grades': {"GEG115" : 60, "GEG117" : 78, "FSC112" : 55, "FSC115" : 59}
        })

addStudent200({
    "Name": "Levi Udoh",
    "Matric Number": 190407076, 
    "Grades": {"GEG217": 77, "GEG219": 80, "SSG215": 90, "MEG211": 90},
    "CGPA": 4.7
    })
addStudent200({
    "Name": "Adesoye Peace",
    "Matric Number": 190407026, 
    "Grades": {"GEG217": 87, "GEG219": 70, "SSG215": 90, "MEG211": 80},
    "CGPA": 3.7
    })
addStudent200({
    "Name": "Oakara James",
    "Matric Number": 190407016,
    "Grades": {"GEG217": 66, "GEG219": 54, "SSG215": 63, "MEG211": 54},
    "CGPA": 2.5
    })
addStudent200({
    "Name": "Ademola Simeon",
    "Matric Number": 190407079,
    "Grades": {"GEG217": 54, "GEG219": 34, "SSG215": 73, "MEG211": 44},
    "CGPA": 1.2
    })
print("\n100 Level Students: \n")
for scholar_details in student100:
        print(f"Name: {scholar_details['Name']} || Matric Number: {scholar_details['Matric Number']} || Average Score: {average(scholar_details['Grades'].values())}")
print("\n200 Level Students: \n")
for scholar_details in student200:
        print(f"Name: {scholar_details['Name']} || Matric Number: {scholar_details['Matric Number']} || Average Score: {average(scholar_details['Grades'].values())} || CGPA: {scholar_details['CGPA']} || Ranking: {ranking(scholar_details['CGPA'])} Honors")