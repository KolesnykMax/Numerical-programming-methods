from numpy import *
import matplotlib.pyplot as plt
t = linspace(0, 3, 51)
y = t * exp(-t ** 2)
plt.plot(t, y, 'r-.', label='t*exp(-t^2)')
plt.axis([0, 1, -0.05, 0.5])  # задання [xmin,xmax, ymin, ymax]
plt.xlabel('t')  # позначення вісі абсцис
plt.ylabel('y')  # позначення е вісі ординат
plt.title('Графік функції')  # назва графіка
plt.legend()  # вставка легенди (тексту в label)
plt.show()