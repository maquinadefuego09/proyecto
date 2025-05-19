# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 17:58:33 2025
Osbaldo Corpus Castillo
348071
Progrmacion Numerica
@author: osbal
"""

import numpy as np

A = np.array([[1, -0.1, -0.2],[0.1, 7, -0.3],[0.3, -0.2, -10]])
b = np.array([7.85, 19.3, 71.4])

def er(vr, vn):
    return abs((vr - vn) / vr) * 100

print("\nIteraciones por metodo de Jacobi")

x1_v, x2_v, x3_v = 0, 0, 0
n_iter = 5

for k in range(1, n_iter + 1):
    x1 = (-A[0, 1] * x2_v - A[0, 2] * x3_v + b[0]) / A[0, 0]
    x2 = (-A[1, 0] * x1_v - A[1, 2] * x3_v + b[1]) / A[1, 1]
    x3 = (-A[2, 0] * x1_v - A[2, 1] * x2_v + b[2]) / A[2, 2]
    
    print(f"i={k} x1 = {x1:.4f} x2 = {x2:.4f} x3 = {x3:.4f}")
    print(f"error x1 = {er(x1, x1_v):.4f}, error x2 = {er(x2, x2_v):.4f}, error x3 = {er(x3, x3_v):.4f}")
    

    x1_v, x2_v, x3_v = x1, x2, x3
  
print("\nIteraciones por metodo de Gauss-Seidel")


x1_v=b[0]/A[0,0]
x2_v, x3_v = 0, 0
n_iter = 5

# Iteración
for k in range(1, n_iter + 1):
    x1 = (b[0] - A[0,1] * x2_v - A[0, 2] * x3_v) / A[0, 0]
    x2 = (b[1] - A[1,0] * x1_v - A[1, 2] * x3_v) / A[1, 1]
    x3 = (b[2] - A[2,0] * x1_v - A[2, 1] * x2_v) / A[2, 2]
    
    print(f"i={k} x1 = {x1:.4f} x2 = {x2:.4f} x3 = {x3:.4f}")
    print(f"error x1 = {er(x1, x1_v):.4f}, error x2 = {er(x2, x2_v):.4f}, error x3 = {er(x3, x3_v):.4f}")
    
    x1_v, x2_v, x3_v = x1, x2, x3