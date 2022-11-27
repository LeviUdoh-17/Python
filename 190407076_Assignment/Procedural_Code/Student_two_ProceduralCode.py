studentDictionary = [
      #Lists of students
]
Student_Officials = [
      #Lists of student officials
]

def average(grade):
        """To calculate average values in a dictionary"""
        score_sum = 0
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

def addStudent(student):
        studentDictionary.append(student)

def addStudentOfficial(official):
        Student_Officials.append(official)

addStudent({
        'Name': 'Udoh Levi',
        'Matric Number': 190407076,
        'Grades': {"GEG217": 77, "GEG219": 80, "SSG215": 90, "MEG211": 90},
        'Faculty': 'Engineering',
        'Department': 'Systems Engineering',
        'CGPA': 4.43
        })        
addStudent({
        'Name': 'Adesoye Peace', 
        'Matric Number': 190407026, 
        'Grades': {"GEG217": 87, "GEG219": 70, "SSG215": 90, "MEG211": 80}, 
        'Faculty': "Engineering", 
        'Department': "Systems Engineering", 
        'CGPA': 3.7,
        })
addStudent({
        'Name': "Oakara James",
        'Matric Number': 190407016,
        'Grades': {"GEG217": 66, "GEG219": 54, "SSG215": 63, "MEG211": 54}, 
        'Faculty': "Engineering", 
        'Department': "Systems Engineering",
        'CGPA': 2.5
        })
addStudent({
        'Name': "Ademole Simeon",
        'Matric Number': 190407079, 
        'Grades': {"GEG217": 54, "GEG219": 34, "SSG215": 73, "MEG211": 44}, 
        'Faculty': "Engineering", 
        'Department': "Systems Engineering",
        'CGPA': 1.2
        })
addStudentOfficial({
    "Name": "Udoh Ukaraobong",
    "Matric Number": 150407045, 
    "Grades": {"SSG512": 89, "SSG517": 90, "SSG219": 88,"MEG514": 95}, 
    "Faculty": "Engineering", 
    "Department": "Systems Engineering", 
    "CGPA": 4.98, 
    "Title": "President", 
    "Role": "Oversee the other officials; Represent the faculty in any official term."
    })
addStudentOfficial({
    "Name": "Etim Erioluwa",
    "Matric Number": 150407032, 
    "Grades": {"SSG512": 74, "SSG517": 57, "SSG219": 75, "MEG514": 80},
    "Faculty": "Engineering",
    "Department": "Systems Engineering",
    "CGPA": 4.51, 
    "Title": "Vice President",
    "Role": "Assists the President",
    })
addStudentOfficial({
    "Name": "Adewike Daniel",
    "Matric Number": 150401080,
    "Grades": {"SSG512": 89, "SSG517": 70, "SSG219": 86, "MEG514": 60},
    "Faculty": "Engineering",
    "Department": "Mechanical Engineering",
    "CGPA": 4.20, 
    "Title": "Tresurer",
    "Role": "Incharge of the finances of that tenure",
    })
addStudentOfficial({
    "Name": "Eduador Fikayo",
    "Matric Number": 150407015,
    "Grades": {"SSG512": 49, "SSG517": 60, "SSG219": 58, "MEG514": 45},
    "Faculty": "Engineering",
    "Department": "Systems Engineering",
    "CGPA": 3.89,
    "Title": "Welfare",
    "Role": "Incharge of any leisure, fun, and sporting activities in the department.",
    })
print("Students \n")
for scholar_details in studentDictionary:
        print(f"Name: {scholar_details['Name']} || Faculty: {scholar_details['Faculty']} || Department: {scholar_details['Department']} || Matric Number: {scholar_details['Matric Number']} || Average Score: {average(scholar_details['Grades'].values())} || CGPA: {scholar_details['CGPA']} || Ranking: {ranking(scholar_details['CGPA'])} Honors")
print("Student Officials \n")
for scholar_details in Student_Officials:
        print(f"Name: {scholar_details['Name']} || Faculty: {scholar_details['Faculty']} || Department: {scholar_details['Department']} || Matric Number: {scholar_details['Matric Number']} || Average Score: {average(scholar_details['Grades'].values())} || CGPA: {scholar_details['CGPA']} || Ranking: {ranking(scholar_details['CGPA'])} Honors || is a student official. Title: {scholar_details['Title']} || Role: {scholar_details['Role']}")