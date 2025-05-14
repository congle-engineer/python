myArray = [7, 12, 9, 4, 11]
minVal = myArray[0]

for i in myArray:
  if i < minVal:
    minVal = i

print('Lowest value: ', minVal)
