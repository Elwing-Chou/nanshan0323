# https://docs.python.org/3/reference/datamodel.html
class Person:

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def bmi(self):
        return self.w / (self.h / 100) ** 2

    def __str__(self):
        return str(self.bmi())

class Student(Person):

    def __init__(self, w, h, n):
        Person.__init__(self, w, h)
        self.n = n

    def study(self):
        print("loss weight")
        self.w = self.w - 1

    def __str__(self):
        # self.__str__()
        return "{}:{}".format(self.n, Person.__str__(self))

s1 = Student(80, 175, "Elwing")
print(s1.bmi())
s1.study()
print(s1.w)

# 1. class: 設計圖型態  2. 主詞是設計圖, self自己帶
b = Student
s2 = b(80, 175, "Bob")
print(Student.bmi(s2))
print(s2)