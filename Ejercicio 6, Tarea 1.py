# -*- coding: utf-8 -*-
"""
Osbaldo Corpus Castillo
348071
Programacion Numerica
Problema 6, Tarea 1, Graficode tres funciones:
""" 

import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(-2,2,100)

y1=x
y2=x**2
y3=x**3

plt.figure(figsize=(10,10))

plt.plot(x,y1,label='y=x', color='blue', linestyle='dashed')
plt.plot(x,y2,label='y=x^2', color='green', linestyle='dashdot')
plt.plot(x,y3,label='y=x^3', color='red', linestyle='dotted')

plt.title('Grafica de tres funciones')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
