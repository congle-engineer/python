import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = np.mean(speed)

print('mean: ', x)

y = np.median(speed)

print('median: ', y)

z = stats.mode(speed)

print('mode: ', z)

std = np.std(speed)

print('std: ', std)

var = np.var(speed)

print('var: ', var)

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

percentile = np.percentile(ages, 90)

print('percentile: ', percentile)

random = np.random.uniform(0.0, 5.0, 100000)

print('random: ', random)

# plt.hist(random, 100)
# plt.show()

normal = np.random.normal(5.0, 1.0, 100000)

# plt.hist(normal, 100)
# plt.show()

xValues = [5,7,8,7,2,17,2,9,4,11,12,9,6]
yValues = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# plt.scatter(xValues, yValues)
# plt.show()

x = np.random.normal(5.0, 1.0, 1000)
y = np.random.normal(10.0, 2.0, 1000)

# plt.scatter(x, y)
# plt.show()

xValues = [5,7,8,7,2,17,2,9,4,11,12,9,6]
yValues = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(xValues, yValues)

print('r: ', r)

def myfunc(x):
  return slope * x + intercept

# mymodel = list(map(myfunc, xValues))

# plt.scatter(xValues, yValues)
# plt.plot(xValues, mymodel)
# plt.show()

speed = myfunc(10)

print('speed: ', speed)
