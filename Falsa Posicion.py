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

for i in range(num_interacciones):
    f1=fx(a)
    f2=fx(b)
    xi=b-((f2*(a-b))/(f1-f2))
    f3=fx(xi)
    if f1*f3<0:
        b=xi
    else: 
        a=xi
    print('=========================================')
    print(f'i={i+1} | f(a)={f1} | fx(b)={f2}| a={a} | b={b} | xi={xi} | error={error(xa,xi)}')
    
x=np.linspace(-3,-1,100)
plt.plot(x,fx(x))
plt.plot(xi, fx(xi), 'go')
plt.grid()
plt.show()
