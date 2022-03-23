# https://docs.python.org/3/reference/datamodel.html
class Person:

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def bmi(self):
        return self.w / (self.h / 100) ** 2

    def __str__(self):
        return str(self.bmi())

    def __repr__(self):
        return "{}/{}".format(self.w, self.h)

    def __eq__(self, other):
        return (self.h - self.w) == (other.h - other.w)

# 偷偷執行 __init__
p1 = Person(80, 175)
print(p1.bmi())
# print(p1) -> str(p1) -> p1.__str__()
print(p1)
# repr(p1) -> p1.__repr__()
print([p1])
p2 = Person(70, 165)
# p1.__eq__(p2)
print(p1 == p2)