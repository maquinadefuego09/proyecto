# -*- coding: utf-8 -*-
"""
Osbaldo Corpus Castillo 
Programacion Numerica
Metodo de secante 

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np

def fx(x):
    return (x*8*np.sin(x)*np.exp(-x))-1
def error_relativo(va,vn):
    return np.abs((va-vn)/va)*100

b=0.5
a=-0.3

num_interacciones=6

for i in range (1,num_interacciones):
    fa=fx(a)
    fb=fx(b)
    c= a-(fx(a)*(b-a)/(fx(b)-fx(a)))
    print('=========================================')
    print(f' i={i} | xi={a} | xi+1={c} | error={error_relativo(c,a)} ')
    b=a
    a=c

x=np.linspace(-0.5,0.5,100)
plt.plot(x,fx(x))
plt.plot(c, fx(c), 'go')
plt.grid()
plt.show()

