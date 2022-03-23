class Person:
    pass

p1 = Person()
p1.height = 175
print(p1.height)

print(round(4.234234, 2))
# 字典: dic 操作:[key]  dic["height"]
# 函式型態: round 操作:(4.234, 2)
b = round
print(b(5.6713, 1))
p1.bmi = round
print(p1.bmi(7.27))