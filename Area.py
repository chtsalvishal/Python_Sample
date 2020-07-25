# User input
length = float(input('Enter the Length of Rectangle:'))
breadth = float(input('Enter the Breadth of Rectangle:'))

# Calculations
areaRec = length * breadth
areaTri = (2 / 2) * breadth * length

# User Output
print('Area of Rectangle of Length ' + str(length) + ' and Breadth ' + str(breadth) + ' is ' + str(areaRec))
print('Area of Triangle of Length ' + str(length) + ' and Breadth ' + str(breadth) + ' is ' + str(areaTri))

# Alternate way to do the above

# Display Rectangle Area
Display1 = 'Area of Rectangle of Length {} and Breadth {} is {}'
print(Display1.format(length, breadth, areaRec))

# Display Triangle Area
Display2 = 'Area of Triangle of Length {} and Breadth {} is {}'
print(Display2.format(length, breadth, areaTri))
