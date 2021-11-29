import numpy as np
from numpy import *
import math
import matplotlib.pyplot as plt

mas_x=[0.15, 0.16, 0.17, 0.18, 0.19, 0.20, 0.21, 0.22, 0.23, 0.24, 0.25]
mas_y=[4.4817, 4.9530, 5.4739, 6.0496, 6.6859, 7.3891, 8.1662, 9.0250, 9.9742, 11.0232, 12.1825]
h = mas_x[1] - mas_x[0]
def y(mas_y,j):
    mas=[]
    for i in range(len(mas_y)):
        mas.append(mas_y[i] - mas_y[i-1])
    mas.pop(0)  
    if j == 1:
        return mas
    else:
        j-=1
        return y(mas, j)
yx1=1/h*((y(mas_y, 1)[1])-(y(mas_y, 2)[1])/2+(y(mas_y, 3)[1])/3-(y(mas_y, 4)[1])/4)
yx2=1/h**2*((y(mas_y, 2)[1])-(y(mas_y, 3)[1])+11/12*(y(mas_y, 4)[1]))
print ("yx1 =", yx1)
print ("yx2 =", yx2)
q = (mas_x[1] - mas_x[0])/0.2
print ("q =", q)
N1= mas_y[0] + q*mas_y[1]-mas_y[0]+(q*(q-1)/math.factorial(2))*(y(mas_y, 1)[0]) + (q*(q-1)*(q-2)/math.factorial(3))*(y(mas_y, 2)[0])+(q*(q-1)*(q-2)*(q-3)/math.factorial(4))*(y(mas_y, 3)[0])+(q*(q-1)*(q-2)*(q-3)*(q-4)/math.factorial(5))*(y(mas_y, 4)[0])+(q*(q-1)*(q-2)*(q-3)*(q-4)*(q-5)/math.factorial(6))*(y(mas_y, 5)[0])+(q*(q-1)*(q-2)*(q-3)*(q-4)*(q-5)*(q-6)/math.factorial(7))*(y(mas_y, 6)[0])+(q*(q-1)*(q-2)*(q-3)*(q-4)*(q-5)*(q-6)*(q-7)/math.factorial(8))*(y(mas_y, 7)[0])+(q*(q-1)*(q-2)*(q-3)*(q-4)*(q-5)*(q-6)*(q-7)*(q-8)/math.factorial(9))*(y(mas_y, 8)[0])+(q*(q-1)*(q-2)*(q-3)*(q-4)*(q-5)*(q-6)*(q-7)*(q-8)*(q-9)/math.factorial(10))*(y(mas_y, 9)[0])+(q*(q-1)*(q-2)*(q-3)*(q-4)*(q-5)*(q-6)*(q-7)*(q-8)*(q-9)*(q-10)/math.factorial(11))*(y(mas_y, 10)[0])
print ("First N =", N1)
N2= mas_y[10] + q*(y(mas_y, 1)[9])+(q*(q-1))/math.factorial(2)*(y(mas_y, 2)[8])+(q*(q-1)*(q-2))/math.factorial(3)*(y(mas_y, 3)[7])+(q*(q-1)*(q-2)*(q-3))/math.factorial(4)*(y(mas_y, 4)[6])+(q*(q-1)*(q-2)*(q-3)*(q-4))/math.factorial(5)*(y(mas_y, 5)[5])+(q*(q-1)*(q-2)*(q-3)*(q-4)*(q-5))/math.factorial(6)*(y(mas_y, 6)[4])+(q*(q-1)*(q-2)*(q-3)*(q-4)*(q-5)*(q-6))/math.factorial(7)*(y(mas_y, 7)[3])+(q*(q-1)*(q-2)*(q-3)*(q-4)*(q-5)*(q-6)*(q-7))/math.factorial(8)*(y(mas_y, 8)[2])+(q*(q-1)*(q-2)*(q-3)*(q-4)*(q-5)*(q-6)*(q-7)*(q-8))/math.factorial(9)*(y(mas_y, 9)[1])+(q*(q-1)*(q-2)*(q-3)*(q-4)*(q-5)*(q-6)*(q-7)*(q-8)*(q-9))/math.factorial(10)*(y(mas_y, 10)[0])
print ("Second N =", N2)

plt.plot(mas_x, mas_y,'ko-', label='x , y')
plt.title('LB_9')
plt.legend(loc='upper left')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(axis='both')
plt.show()



