import numpy as np
from numpy import *
import math
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
x = array([0.4, 0.6, 0.9, 1.4, 2],dtype = float)
y = array([2.45, 1.63, 0.95, 0.73, 1.95],dtype = float)
h = []
mas_k = []
m = []
a = []
b = []
c = []
d = []
def H(x):
    i = 0
    while i <= 3:
        h.append(x[i+1]-x[i])
        i+=1
    return h
print (H(x))
def K(y,h):
    i = 2
    while i <= 4:
        mas_k.append (3*((y[i]-y[i-1])/h[i-1]-(y[i-1]-y[i-2])/h[i-2]))
        i+=1
    return mas_k
print (K(y,h))
def M(h):
    i = 1
    while i <= 3:
        m.append(2*(h[i-1]+h[i]))
        i+=1
    return m
print (M(h))
def funk_abcd(mas_k,m,h):
    i=0
    a=[(mas_k[i]/m[i])]
    b=[(h[i]/m[i])]
    while i < len(y)-3:
        a.append((mas_k[i+1]-h[i]*a[i])/(m[i+1]-h[i]*b[i]))
        b.append(h[i+1]/(m[i+1]-h[i]*b[i]))
        i+=1
    return a ,b
def funk_asbcd(mas_k,m,h,y):
    i=0
    a=[0, (mas_k[i]/m[i])]
    sb=[0, (h[i+1]/m[i])]
    c=[0]
    d=[]
    b=[]
    while i < len(y)-3:
        a.append((mas_k[i+1]-h[i+1]*a[i+1])/(m[i+1]-h[i+1]*sb[i+1]))
        sb.append(h[i+2]/(m[i+1]-h[i+1]*sb[i+1]))
        i+=1
    i=len(y)-2
    while i >= 0:
        c.insert(0, a[i]-sb[i]*c[0])
        i-=1
    i=0
    while i < len(y)-1:
        d.append((c[i+1]-c[i])/(3*h[i]))
        i+=1
    i=0
    while i < len(y)-1:
        b.append((y[i+1]-y[i])/h[i]-(c[i+1]+2*c[i])*h[i]/3)
        i+=1
    i=0
    s=[]
    while i<len(y)-1:
        s.append(a[i]+b[i]*(avr_x-x[i])+c[i]*(avr_x-x[i])+d[i]*(avr_x-x[i])**3)
        i+=1
    print ("S =",s)
    print ("B =",b)
    print ("D =",d)
    print ("C =",c)
    print ("A =",a)
    print ("SB =",sb)
    return a, sb, c, d, b
i = 0
avr_x = 0
while i <= 4:
    avr_x += x[i]
    i += 1
avr_x = avr_x / 5
print ("X =",avr_x)
print("H =",H(x))
print("K =",K(y,H(x)))
print("M =",M(H(x)))
funk_asbcd(K(y,H(x)),M(H(x)),H(x),y)
spl = UnivariateSpline(x, y)
xs = linspace(0, 4.5, 1000)
plt.plot(x, y, 'ro', xs, spl(xs), 'g')
plt.title('LB_9')
plt.legend(loc='upper left')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()