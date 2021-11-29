import matplotlib.pyplot as plt 
from numpy import *
t = linspace(0, 3, 51)
y = t ** 2 * exp(-t ** 2)
plt.plot(t, y, 'g--', label='t^2*exp(-t^2)')
plt.axis([0, 3, -0.05, 0.5]) # [xmin, xmax, ymin, ymax]
plt.xlabel('t') # позначення вісі абсцис
plt.ylabel('y') # позначення е вісі ординат
plt.title('My first normal plot') # назва графіка
plt.legend() # вставка легенди (тексту в label)
plt.show()