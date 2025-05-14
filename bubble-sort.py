myArray = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(myArray)

# print(range(n - 1))

for i in range(n - 1):
  swapped = False
  for j in range(n - i - 1):
    if myArray[j] > myArray[j + 1]:
      myArray[i], myArray[j + 1] = myArray[j + 1], myArray[j]
      swapped = True
    if not swapped:
      break

print('Sorted array: ', myArray)
