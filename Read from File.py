# User input
f = open('shape.txt', 'r')

length = float(f.readline())
breadth = float(f.readline())

# Calculations
areaRec = length * breadth
areaTri = (3 / 2) * breadth * length

# Output to new file
areaFile = open('areaFile.txt', 'r+')
areaFile.write('Area of Rectangle:' + str(areaRec) + '\n')
areaFile.write('Area of Rectangle:' + str(areaTri) + '\n')
#areaFile.close()

# Read the file to show contents.
#print('File contains:\n')
#areaFile = open('areaFile.txt', 'r')
areaFile.seek(0)
print(areaFile.read(100))
#print(areaFile.read())


# Close file
f.close()
areaFile.close()
# end