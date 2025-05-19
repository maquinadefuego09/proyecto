# -*- coding: utf-8 -*-
"""
Osbaldo Corpus Castillo 
Programacion Numerica
Metodo de Newton-Raphson

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np

def fx(x):
    return (8*x*np.sin(x)*np.exp(-x))-1

def gx(x):
    return (8*np.exp(-x))*(np.sin(x)+(x*np.cos(x))-(x*np.sin(x)))

def error_relativo(va, vn):
    return np.abs((va - vn) / va) * 100

a = 0.3
num_interacciones = 6

for i in range(1, num_interacciones):
    f1 = fx(a)
    f2 = gx(a)
    b = a - (f1 / f2)
    print('=========================================')
    print(f'i={i} | xnueva={b} | error={error_relativo(b,a)}')
    a = b  

x=np.linspace(-0.8,0.8,100)
plt.plot(x,fx(x))
plt.plot(x,gx(x))
plt.plot(a, fx(a), 'go')
plt.plot(a, gx(a), 'go')
plt.grid()
plt.show()
