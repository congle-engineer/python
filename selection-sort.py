myArray = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(myArray)

for i in range(n - 1):
  minIndex = i
  for j in range(i + 1, n):
    if myArray[j] < myArray[minIndex]:
      minIndex = j
  myArray[i], myArray[minIndex] = myArray[minIndex], myArray[i]

print('Sorted array: ', myArray)
