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
for scholar in ASES200:
    print(f"Student name: {scholar.name()} || Faculty: {scholar.faculty()} || Department: {scholar.department()} || Matric Number: {scholar.matric()} || Averge Score: {scholar.average()} || CGPA: {scholar.cgpa()} || Ranking: {scholar.ranking()} Honors")
for official in ASES500:
    print(f"Student name: {official.name()} || Faculty: {official.faculty()} || Department: {official.department()} || Matric Number: {official.matric()} || Averge Score: {official.average()} || CGPA: {official.cgpa()} || Ranking: {official.ranking()} Honors || is a student official. Title: {official.title()} || Role: {official.role()}")