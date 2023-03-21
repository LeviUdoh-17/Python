class Student:
    def __init__(self, name, matric, grades):
         self._matric = matric
         self._name = name
         self._grades = grades
    def name(self):
        return self._name
    def matric(self):
        return self._matric
    def grades(self):
        return self._grades
    def avg(self):
        sum = 0
        for num in self._grades:
            sum+=num
        return sum/len(self._grades)

g1 = [50, 56, 90, 92, 93, 45]
g2 = [20, 30, 46, 90, 80, 76]
g3 = [40, 87, 67, 34, 35, 13]
g4 = [32, 45, 65, 45, 87, 29]
n1 = 'Amanda'
n2 = 'Levi'
n3 = 'Emmanuel'
n4 = 'Ereoluwa'
m1 = 'SSG123'
m2 = 'MEC105'
m3 = 'ELC005'
m4 = 'IOT001'

studentList = [Student(n1, m1, g1), Student(n2, m2, g2), Student(n3, m3, g3), Student(n4, m4, g4)]
nameList = {}
for student in studentList:
    nameList[student.avg()] = student.name()
for keys in sorted(nameList.keys()):
    print(keys, nameList[keys])
    