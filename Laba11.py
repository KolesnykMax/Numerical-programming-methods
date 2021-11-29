import numpy as np
from numpy import *
import math
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import sympy as sp
def taylor(x):
    y=0
    d1=sp.diff(f,x)
    d2=sp.diff(d1,x)
    d3=sp.diff(d2,x)
    d4=sp.diff(d3,x)
    print('d1 =', d1)
    print('d2 =', d2)
    print('d3 =', d3)
    print('d4 =', d4)
    y += f + d1*x + d2*(x-0)**2/2 + d3*(x-0)**3/6 + d4*(x-0)**4/24
    print ("y=", y )
    pohibka = d4 / math.factorial(4)
    print ("Pohibka =", pohibka)
    return y
x = sp.symbols ("x")
f = sp.sin(4*x)
taylor_x = taylor(x)
pl = sp.plot (f,taylor_x, (x, -1, 1), label = 'Taylor') 
