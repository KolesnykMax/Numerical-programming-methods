from numpy import *
import matplotlib.pyplot as plt
def f(x):
    return 5*cos(10*x)*sin(3*x)/(x**(1/2))
x = linspace(0, 5, 51)
y = f(x)
plt.plot(x, y, 'ko-', label='5*cos(10*x)*sin(3*x)/(x**(1/2))')
plt.axis([0, 5, -7.5, 7.5])
plt.title('Laba7')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(axis='both')
plt.legend(loc='upper right')
plt.show()