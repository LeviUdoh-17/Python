from sqlalchemy import false


class Student:
    def __init__(self, name, matric, grades, units) :
        self._matric = matric
        self._name = name
        self._grades = grades
        self._units = units   
    def name(self):
        return self._name
    def matric(self):
        return self._matric
    def grades(self):
        return self._grades
    def weight(self):
        return self._units

    def gpa(self):
        global idealGrade = 0
        global gottenGrades = 0
        for i in self._units:
            idealGrade += idealGrade + i * 5
        for i in self._grades:
            if self._grades <= 100 and self._grades >= 70:
                equivalentGrade = 'A'
                equivalentUnit = 5
            elif self._grades < 70 and self._grades >= 60:
                equivalentGrade = 'B'
                equivalentUnit = 4
            elif self._grades < 60 and self._grades >= 55:
                equivalentGrade = 'C'
                equivalentUnit = 3
            elif self._grades < 55 and self._grades >= 50:
                equivalentGrade = 'D'
                equivalentUnit = 2
            elif self._grades < 50 and self._grades >= 40:
                equivalentGrade = 'E'
                equivalentUnit = 1
            else:
                equivalentGrade = 'F'
                equivalentUnit = 0
            return equivalentUnit 
        gottenGrades += gottenGrades + (equivalentUnit * (self._units))
            

    g1 = [90, 85, 88, 89, 87, 90, 85, 88, 89, 87, 90, 85, 88, 89, 87]
    g2 = [30, 40, 60, 70, 66, 30, 40, 60, 70, 66, 30, 40, 60, 70, 66]
    g3 = [55, 56, 67, 78, 77, 55, 56, 67, 78, 77, 55, 56, 67, 78, 78]
    w = [2, 3, 2, 3, 3, 3, 2, 2, 2, 3, 1, 2, 2, 1, 1]
    n1 = 'James'
    n2 = 'Jabreal'
    n3 = 'Elon'
    m1 = 'SSG123'
    m2 = 'MEC105'
    m3 = 'ELC005'
