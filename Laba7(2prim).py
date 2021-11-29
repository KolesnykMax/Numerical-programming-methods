from numpy import *
linspace
import matplotlib.pyplot as plt
def f(t):
    return t ** 2 * exp(-t ** 2)
t = linspace(0, 3, 51)
y = f(t)
plt.plot(t, y)
plt.show()