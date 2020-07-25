'''
x = int(input('input number x:'))
y = int(input('input number y:'))
print('division x/y:', x / y)
print('multiply x*y', x * y)
print('addition x+y', x + y)
print('subtraction', x - y)
print('floor/Quotient', x // y)
print('Remainder', x % y)

a = [1, 2, 3, 4, 5]
b = [e for e in a if e % 2 != 0]
print(b)
'''

# Enter string until user type quit
# newline = []
# c = 0
# w = ''
# while w != 'quit':
#     w = input()
#     newline.append(w)
# newline = newline[:len(newline) - 1]
# print(newline)
#
# grid = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
# print(grid)

count = 10


class AlphabetStack(Stack):

    def __init__(self, x, y):
        super.__init__()

    def distance(self, other):
        xdifference = (self.x - other.x) ** 2
        ydifference = (self.y - other.y) ** 2
        distance = (xdifference + ydifference) ** 0.5
        return distance

    def __add__(s, other):
        xsum = s.x + other.x
        ysum = s.y + other.y
        return xsum, ysum


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = str(age)

    def grow(self):
        self.age += 1

    def __str__(self):
        return self.name+self.age
# Inheritance.
class Stu(Person):
    def __init__(self, name, age, ID, depart):
        Person.__init__(self, name, age)
        self.stuID = str(ID)
        self.department = depart

    def __str__(self):
        st = Person.__str__(self)
        return st+self.stuID+self.department


#
# man = Person('vishal', 25)
# man = Stu(311, 'CSE')
from Temperature import to_farenhiet
man = Stu('vishal', 25, 311, 'CSE')
print(f"Details of student {man.name} is {man}")

p = P(1, 2)
org = P(0, 9)
print(p.distance(org))
print(P.distance(p, org))
print(P.count)
