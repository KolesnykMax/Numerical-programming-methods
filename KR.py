import matplotlib.pyplot as plt
import numpy as np

from scipy import interpolate
from scipy import integrate

speed = [25, 35, 45, 30, 60, 120, 100, 100, 70, 75, 80, 65]
time = np.linspace(0, 11, num = 12)
print('Масив time:')
for i in time:
    print(i, end=' ')
print()

fig = plt.figure()
f = interpolate.interp1d(time, speed, kind='cubic')
plt.plot(time, f(time), 'o', speed)
plt.title('cubic')
plt.grid()

v, err = integrate.quad(f, 0, 11, limit=10000)
print('Інтеграл cubic: ')
print(v)

fig = plt.figure()
f = interpolate.interp1d(time, speed, kind='quadratic')
plt.title('quadratic')
plt.plot(time, f(time), 'ro', speed)
plt.grid()

v, err = integrate.quad(f, 0, 11, limit=10000)
print('Інтеграл quadratic: ')
print(v)

plt.show()