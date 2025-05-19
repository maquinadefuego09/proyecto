# -*- coding: utf-8 -*-
"""
Osbaldo Corpus Castillo 
Programacion Numerica
Metodo de biseccion 

@author: osbal 
"""
 
import matplotlib.pyplot as plt
import numpy as np

def fx(x):
    return 2*x*np.cos(2*x)-(x+1)**2
def error(va,vn):
    return np.abs((va-vn)/va)*100

a=-3
b=-2
xa=-2.1913

num_interacciones=5

for i in range(num_interacciones+1):
    a1=a
    b1=b
    xi=(a+b)/2
    f1=fx(xi)
    f2=fx(b)
    f3=fx(xi)
    if f1*f3<0:
        b=xi
    else: 
        a=xi
    print('=========================================')
    print(f'i={i} | a={a} | b={b} | xi={xi} | error={error(xa,xi)}')
    
x=np.linspace(-4,4,100)
plt.plot(x,fx(x))
plt.plot(xi, fx(xi), 'go')
plt.grid()
plt.show()
