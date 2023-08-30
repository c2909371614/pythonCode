#coding = utf-8


import matplotlib.pyplot as plt
import numpy as np
import math

def getRates(step = 2):
    rateE = range(5, 100, step)
    rateA = []
    failRate = 1
    for i in range(0, len(rateE)):
        failRate *= 1 - rateE[i]/100
        rateA.append(round(1 - failRate, 3))
    hue = []
    print((rateA, len(rateA)))
    return rateE, rateA


fig, axes = plt.subplots(2, 2)
rateE, rateA = getRates(2)
# plt.plot(range(1, len(rateE)+1), rateA)
axes[0, 0].plot(range(1, len(rateE)+1), rateA)
axes[0, 0].set_title("step 2")
axes[0, 1].plot(np.dot(rateE, 0.01), rateA)

rateE, rateA = getRates(3)
# plt.plot(range(1, len(rateE)+1), rateA)
axes[1, 0].plot(range(1, len(rateE)+1), rateA)
axes[1, 1].plot(np.dot(rateE, 0.01), rateA)
axes[1, 0].set_title("step 3")
plt.show()

            
