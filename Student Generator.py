# Kyan paste the student generator code here
import random
class1 = 0
class2 = 0
class3 = 0
class4 = 0
class5 = 0
class6 = 0


def reset_classes():
    global class1
    global class2
    global class3
    global class4
    global class5
    global class6
    class1 = 0
    class2 = 0
    class3 = 0
    class4 = 0
    class5 = 0
    class6 = 0


def random_class():
    global class1
    global class2
    global class3
    global class4
    global class5
    global class6
    # Maybe use numerical id for classes instead of string?
    x = random.randint(1, 7)
    if x == 1 and class1 == 0:
        return "class1"
    elif x == 2 and class2 == 0:
        return "class2"
    elif x == 3 and class3 == 0:
        return "class3"
    elif x == 4 and class4 == 0:
        return "class4"
    elif x == 5 and class5 == 0:
        return "class5"
    elif x == 6 and class6 == 0:
        return "class6"
    else:
        random_class()


class Student:
    def __init__(self, number, vce, eng, p1, p2, p3, p4, b1, b2, ls):
        self.number = number
        self.vce = vce
        self.eng = eng
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.b1 = b1
        self.b2 = b2
        self.ls = ls


students = []
for s in range(100):
    s += 1
    p = {}
    for y in range(1, 7):
        p[f"p{y}"] = random_class()
    students.append(Student(s, False, 50, p["p1"], p["p2"], p["p3"], p["p4"], p["p5"], p["p6"], 50))
    reset_classes()
print(students[0].p1)
print(students[0].p2)
print(students[0].p3)
print(students[0].p4)
print(students[0].b1)
print(students[0].b2)




