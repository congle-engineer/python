def partition(array, low, high):
  print("=========================================")
  pivot = array[high]

  print('array: ', array)
  print('pivot: ', pivot)
  
  print('low: ', low)
  print('high: ', high)

  i = low - 1

  for j in range(low, high):
    print('j: ', j)
    if array[j] <= pivot:
      i += 1
      print('i: ', i)
      print('array[i]: ', array[i])
      print('array[j]: ', array[j])
      array[i], array[j] = array[j], array[i]

  print('i + 1: ', i + 1)
  print('array[i + 1]: ', array[i + 1])
  print('array[high]: ', array[high])
  array[i + 1], array[high] = array[high], array[i + 1]

  print("=========================================\n")

  return i + 1

def quickSort(array, low = 0, high = None):
  if high is None:
    high = len(array) - 1

  if low < high:
    pivotIndex = partition(array, low, high)
    print('pivotIndex: ', pivotIndex)
    quickSort(array, low, pivotIndex - 1)
    quickSort(array, pivotIndex + 1, high)

myArray = [64, 34, 25, 12, 22, 11, 90, 5]

quickSort(myArray)

print('Sorted array: ', myArray)
