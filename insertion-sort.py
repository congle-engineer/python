myArray = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(myArray)

for i in range(1, n):
  insertIndex = i
  currentValue = myArray[i]
  for j in range(i - 1, -1, -1):
    if myArray[j] > currentValue:
      myArray[j + 1] = myArray[j]
      insertIndex = j
    else:
      break
  myArray[insertIndex] = currentValue

print('Sorted array: ', myArray)
