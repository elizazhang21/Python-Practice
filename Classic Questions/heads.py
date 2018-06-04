import numpy.random as nr
import numpy as np


res = 0
for i in range(10000):
    step = 1
    sum = 0
    sum += np.ceil(6*nr.uniform())
    sum %= 6

    while(sum != 0):
        sum += np.ceil(6*nr.uniform())
        sum %= 6
        step += 1
    res += step

print(res/10000)
