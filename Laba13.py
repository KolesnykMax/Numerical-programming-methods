from scipy import integrate
from numpy import *
import math 


def pryamougol(x):
    return x / (sqrt(x + 3))

v, err = integrate.quad(pryamougol, 0.4, 1.2)

def kvadr_func(pryamougol, a, b, n):
    h = (b - a) / n
    rt = h * ((pryamougol(a)+h/2) + (pryamougol(b - h)+h/2))
    for i in range(1, n - 1):
        rt += pryamougol(a + i * h)/10
    return rt

def right_kvadr_func(pryamougol, a, b, n):
    h = (b - a) / n
    rkf = h * (pryamougol(a) + pryamougol(b - h))
    for i in range(2, n):
        rkf += pryamougol(a + i * h) / 10
    return rkf

def left_kvadr_func(pryamougol, a, b, n):
    h = (b - a) / n
    lkf = h * (pryamougol(a) + pryamougol(b - h))
    for i in range(1, n-1):
        lkf += pryamougol(a + i * h) / 10
    return lkf

print("Средний квадрат = ", kvadr_func(pryamougol, 2, 1.2, 10))
print("Левый квадрат = ", left_kvadr_func(pryamougol, 2, 1.2, 10))
print("Правый квадрат = ", right_kvadr_func(pryamougol, 2, 1.2, 10))
print('Проверка квадратов = ', v)

def trapezoid(x):
    return x / (sqrt(0.5 * x ** 2 + 1.5))

def trap_func(trapezoid, a, b, n):
    h = (b - a) / n
    sum = 0.5 * (trapezoid(a) + trapezoid(b))
    for i in range(1, n):
        sum += trapezoid(a + i * h)
    return sum * h

v, err = integrate.quad(trapezoid, 1.2, 2)
print("Трапеция = ", trap_func(trapezoid, 1.2, 2, 20))
print('Проверка трапеции = ', v)

def simpson(x):                                                                             ## НЕ ГОМЕР
    return (2*x + 0.5) * math.sin(2 * x)

def simp_func(simpson, a, b, n):
    h = (b - a) / n
    k = 0.0
    x = a + h
    for i in range(1, n // 2 + 1):
        k += 4 * simpson(x)
        x += 2 * h

    x = a + 2 * h
    for i in range(1, n // 2):
        k += 2 * simpson(x)
        x += 2 * h
    return (h / 3) * (simpson(a) + simpson(b) + k)

print("Симпсон = ", simp_func(simpson, 0.4, 1.2, 8)) 
v, err = integrate.quad(simpson, 0.4, 1.2)
print('Проверка симпсона= ', v)