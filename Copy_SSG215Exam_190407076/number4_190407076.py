class Student():
    """Blueprint for 100 Level Students"""
    def __init__(self, name, matric, grades, faculty, department, cgpa):
        self._name = name
        self._matric = matric
        self._grades = grades
        self._cgpa = cgpa
        self._faculty = faculty
        self._department = department
    def cgpa(self):
        return self._cgpa
    def ranking(self):
        rank = ""
        if self._cgpa >= 4.50 and self._cgpa <= 5.00:
            rank = "First Class"
        elif self._cgpa >= 3.50 and self._cgpa <= 4.49:
            rank = "Second Class Upper"
        elif self._cgpa >= 2.40 and self._cgpa <= 3.49:
            rank = "Second Class Lower"
        elif self._cgpa >= 1.50 and self._cgpa <= 2.39:
            rank = "Third Class Lower"
        else:
            rank = "Pass"
        return rank    
    def name(self):
        return self._name
    def matric(self):
        return self._matric
    def grades(self):
        return self._grades
    def faculty(self):
        return self._faculty
    def department(self):
        return self._department
    def average(self):
        score_sum = 0
        for scores in self._grades.values():
            score_sum += scores
        return score_sum/len(self._grades)

class Student_Officials(Student):
    def __init__(self, name, matric, grades, faculty, department, cgpa, title, role):
        super().__init__(name, matric, grades, faculty, department, cgpa)
        self._title = title
        self._role = role
    def title(self):
        return self._title
    def role(self):
        return self._role

class Law_Students(Student):
    def __init__(self, name, matric, grades, faculty, department, cgpa, specialization):
        super().__init__(name, matric, grades, faculty, department, cgpa)
        self._specialization = specialization
    def specialization(self):
        return self._specialization


ASES200 = [
    Student("Levi Udoh", 190407076, {
        "GEG217": 77,
        "GEG219": 80,
        "SSG215": 90,
        "MEG211": 90
    }, "Engineering", "Systems Engineering", 4.7),
    Student("Adesoye Peace", 190407026, {
        "GEG217": 87,
        "GEG219": 70,
        "SSG215": 90,
        "MEG211": 80
    }, "Engineering", "Systems Engineering", 3.7),
    Student("Oakara James", 190407016, {
        "GEG217": 66,
        "GEG219": 54,
        "SSG215": 63,
        "MEG211": 54
    }, "Engineering", "Systems Engineering", 2.5),
    Student("Ademole Simeon", 190407079, {
        "GEG217": 54,
        "GEG219": 34,
        "SSG215": 73,
        "MEG211": 44
    }, "Engineering", "Systems Engineering", 1.2)
]

ASES500 =[
    Student_Officials("Udoh Ukaraobong", 150407045, {
        "SSG512": 89,
        "SSG517": 90,
        "SSG219": 88,
        "MEG514": 95
    }, "Engineering", "Systems Engineering", 4.98, "President", "Oversee the other officials; Represent the faculty in any official term."),
    Student_Officials("Etim Erioluwa", 150407032, {
        "SSG512": 74,
        "SSG517": 57,
        "SSG219": 75,
        "MEG514": 80
    }, "Engineering", "Systems Engineering", 4.51, "Vice President", "Assists the President"),
    Student_Officials("Adewike Daniel", 150401080, {
        "SSG512": 89,
        "SSG517": 70,
        "SSG219": 86,
        "MEG514": 60
    }, "Engineering", "Mechanical Engineering", 4.20, "Tresurer", "Incharge of the finances of that tenure"),
    Student_Officials("Eduador Fikayo", 150407015, {
        "SSG512": 49,
        "SSG517": 60,
        "SSG219": 58,
        "MEG514": 45
    }, "Engineering", "Systems Engineering", 3.89, "Welfare", "Incharge of any leisure, fun, and sporting activities in the department."),
]

Law_Student = [
    Law_Students("James Brown", 150307084, {
        "ASK234": 70,
        "PPY590": 90,
        "WYU328": 70,
        "IPO211": 80
    }, "Law", "Law", 4.6, "Jurisprudence"), 
    Law_Students("Leo Messi", 150307064, {
        "ASK234": 71,
        "PPY590": 92,
        "WYU328": 74,
        "IPO211": 85
    }, "Law", "Law", 4.9, "Land Law"), 
    Law_Students("Cristiano Ronaldo", 150307094, {
        "ASK234": 51,
        "PPY590": 72,
        "WYU328": 54,
        "IPO211": 75
    }, "Law", "Law", 3.9, "Taxation")  
]
for scholar in ASES200:
    print(f"Student name: {scholar.name()} || Faculty: {scholar.faculty()} || Matric Number: {scholar.matric()} || Average Score: {scholar.average()} || CGPA: {scholar.cgpa()} || Ranking: {scholar.ranking()} Honors")
for official in ASES500:
    print(f"Student name: {official.name()} || Faculty: {official.faculty()} || Matric Number: {official.matric()} || Average Score: {official.average()} || CGPA: {official.cgpa()} || Ranking: {official.ranking()} Honors || is a student official. Title: {official.title()} || Role: {official.role()}")
for lawers in Law_Student:
    print(f"Student name: {lawers.name()} || Faculty: {lawers.faculty()} || Matric Number: {lawers.matric()} || Average Score: {lawers.average()} || CGPA: {lawers.cgpa()} || Ranking: {lawers.ranking()} Honors || is a Law student. Specialization: {lawers.specialization()}")
