# -*- coding: utf-8 -*-
"""
Created on Thu May 22 22:23:40 2025
Osbaldo Corpus Castillo
348071
Progrmacion Numerica
@author: osbal
"""

import numpy as np
import matplotlib.pyplot as plt

x1, x2 = 3, 5
y1, y2 = 19, 99

def interpolacion_lineal(x):
    return y1 + ((y2 - y1) / (x2 - x1)) * (x - x1)

x_estimar = 4
f4 = interpolacion_lineal(x_estimar)
print(f"f(4) estimado (lineal): {f4}")

x_vals = np.array([x1, x2])
y_vals = np.array([y1, y2])
x_line = np.linspace(2.5, 5.5, 100)
y_line = interpolacion_lineal(x_line)

plt.plot(x_vals, y_vals, 'o', label='Datos usados')
plt.plot(x_line, y_line, label='Interpolación lineal', color='yellow')
plt.plot(x_estimar, f4, 'ro', label='f(4) estimado')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Interpolación Lineal')
plt.legend()
plt.show()


valores_x = np.array([2, 3, 5])
valores_y = np.array([6, 19, 99])

def interpocuad(x, x_vals, y_vals):
    total = 0
    n = len(x_vals)
    for i in range(n):
        term = y_vals[i]
        for j in range(n):
            if i != j:
                term *= (x - x_vals[j]) / (x_vals[i] - x_vals[j])
        total += term
    return total

x_estimar = 4
f4 = interpocuad(x_estimar, valores_x, valores_y)
print(f"f(4) estimado (cuadrática): {f4}")

f4_lineal = 59.0
error_relativo = abs((f4 - f4_lineal) / f4_lineal) * 100
print(f"Error relativo con respecto a la estimación lineal: {error_relativo}%")

x_line = np.linspace(2, 5, 200)
y_line = [interpocuad(x, valores_x, valores_y) for x in x_line]

plt.plot(valores_x, valores_y, 'o', label='Datos usados')
plt.plot(x_line, y_line, label='Interpolación cuadrática', color='yellow')
plt.plot(x_estimar, f4, 'ro', label='f(4) estimado')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Interpolación Cuadrática')
plt.legend()
plt.show()


valores_x = np.array([1, 2, 3, 5, 7])
valores_y = np.array([3, 6, 19, 99, 291])

def coeffs(x, y):
    n = len(x)
    coef = np.copy(y).astype(float)
    for j in range(1, n):
        coef[j:n] = (coef[j:n] - coef[j - 1:n - 1]) / (x[j:n] - x[0:n - j])
    return coef

def eval(x_eval, x_data, coef):
    n = len(coef)
    result = coef[-1]
    for i in range(n - 2, -1, -1):
        result = result * (x_eval - x_data[i]) + coef[i]
    return result

coef = coeffs(valores_x, valores_y)
x_estimar = 4
f4 = eval(x_estimar, valores_x, coef)
print(f"f(4) estimado (Newton grado 4): {f4}")

x_line = np.linspace(1, 7, 300)
y_line = [eval(x, valores_x, coef) for x in x_line]

plt.plot(valores_x, valores_y, 'o', label='Datos usados')
plt.plot(x_line, y_line, label='Interpolación Newton grado 4', color='purple')
plt.plot(x_estimar, f4, 'ro', label='f(4) estimado')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Interpolación de Newton (grado 4)')
plt.legend()
plt.show()
