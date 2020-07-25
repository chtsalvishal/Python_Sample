'''''
temp = int(input('Provide the temperature in F:'))
frac = 5 / 9
Cel = int((temp - 32) * frac)
print('Temperature in Celsius', Cel)

fname = input('Enter the first name:')
lname = input('Enter Last name:')
age = input('Enter Age:')
print('Hey there '+fname+' '+lname+'. Your age is '+age)
'''''

# Fuction of C to F

# Using class from another file created by me.
from Tut1 import *


def to_farenhiet(temperature):
    celsius = int((temperature - 32) * (5 / 9))
    # Return the value
    return celsius


# Display the Temperature
'''''
print('Changed using Function call', to_farenhiet(temp))
num = 0.00
num = "{:.2f}".format(5 / 6)
print(num)
a = "the name is bond"
print(a[7:])
'''''


man = Stu('vishal', 25, 311, 'CSE')
print(f"Details of student {man.name} is {man}")


