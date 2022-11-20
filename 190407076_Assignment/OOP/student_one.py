class Student100():
    """Blueprint for 100 Level Students"""
    def __init__(self, name, matric, grades):
        self._name = name
        self._matric = matric
        self._grades = grades
    def name(self):
        return self._name
    def matric(self):
        return self._matric
    def grades(self):
        return self._grades
    def average(self):
        score_sum = 0
        for scores in self._grades.values():
            score_sum += scores
        return score_sum/len(self._grades)

class Student200(Student100):
    """200 Level Student Blueprint"""
    def __init__(self, name, matric, grades, cgpa):
        super().__init__(name, matric, grades)
        self._cgpa = cgpa
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

ASES100 = [
    Student100("Udom Samuel", 210407021, {
        "GEG115" : 78,
        "GEG117" : 89,
        "FSC112" : 75,
        "FSC115" : 80
        }),
    Student100("James Prince", 210407013, {
        "GEG115" : 90,
        "GEG117" : 88,
        "FSC112" : 85,
        "FSC115" : 80
        }),
    Student100("Ademola Eunice", 210407076, {
        "GEG115" : 60,
        "GEG117" : 78,
        "FSC112" : 55,
        "FSC115" : 59
        })
]
for scholar in ASES100:
    print(f"Student name: {scholar.name()} || Matric Number: {scholar.matric()} || Averge Score: {scholar.average()}")

ASES200 = [
    Student200("Levi Udoh", 190407076, {
        "GEG217": 77,
        "GEG219": 80,
        "SSG215": 90,
        "MEG211": 90
    }, 4.7),
    Student200("Adesoye Peace", 190407026, {
        "GEG217": 87,
        "GEG219": 70,
        "SSG215": 90,
        "MEG211": 80
    }, 3.7),
    Student200("Oakara James", 190407016, {
        "GEG217": 66,
        "GEG219": 54,
        "SSG215": 63,
        "MEG211": 54
    }, 2.5),
    Student200("Ademole Simeon", 190407079, {
        "GEG217": 54,
        "GEG219": 34,
        "SSG215": 73,
        "MEG211": 44
    }, 1.2)
]

for scholar in ASES200:
    print(f"Student name: {scholar.name()} || Matric Number: {scholar.matric()} || Averge Score: {scholar.average()} || CGPA: {scholar.cgpa()} || Ranking: {scholar.ranking()} Honors")