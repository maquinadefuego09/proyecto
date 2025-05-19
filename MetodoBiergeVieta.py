# -*- coding: utf-8 -*-
"""
Editor de Spyder

Osbaldo Corpus Castillo 
Programacion Numerica
Metodo de Birge-Vieta

Este es un archivo temporal.
"""
import numpy as np


def error (va,vn):
    return np.abs((va-vn)/va)*100

a= np.array([1, -5, 5, -1])
x0= 0.8
b= np.empty(len(a))
c= np.empty(len(a))

iteracciones=10
n=len(a)
for i in range(1,iteracciones+1):
    for j in range(n):
        if j==0 :
            b[j]=a[j]
            c[j]=a[j]
        else:
            b[j]=a[j]+x0*b[j-1]
            c[j]=b[j]+x0*c[j-1]
        xo=x0
    x0=x0-(b[n-1]/c[n-2])
    print(f'Iteraccion: {i} | xi={xo} |')
    
