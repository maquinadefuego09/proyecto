# -*- coding: utf-8 -*-
"""
Spyder Editor

Osbaldo Corpus Castillo
Programacion Numerica 
TAREA 5: DERIVACION  E INTEGRACION NUMÉRICA

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff
from scipy.misc import derivative

fx = lambda x: -x**2-x/2+4
h = [0.2,0.1]
xi = 0
x = symbols('x')
fx_sympy = -x**2-x/2+4
derivada_simbolica = diff(fx_sympy, x)


def derivada_adelante(fx, xi, h):
    fxim1 = fx(xi + h)
    fxim2 = fx(xi + 2 * h)
    return (-fxim2 + 4 * fxim1 - 3 * fx(xi)) / (2 * h)
def derivada_atras(fx, xi, h):
    fxim1 = fx(xi - h)
    fxim2 = fx(xi - 2 * h)
    return (3 * fx(xi) - 4 * fxim1 + fxim2) / (2 * h)
def derivada_centrada(fx, xi, h):
    fxip1 = fx(xi + h)
    fxip2 = fx(xi + 2 * h)
    fxim1 = fx(xi - h) 
    fxim2 = fx(xi - 2 * h)
    return (-fxip2 + 8 * fxip1 - 8 * fxim1 + fxim2) / (12 * h)
def tangente(x):
    return dy_tangente*(x-xi)+y_tangente 

print('               Valores reales o analíticos  \n')
print(f'Su derivada es: {derivada_simbolica}')
for h_i in h:
    print(f'Su derivada con SciPy con h={h_i} es: {derivative(fx, xi, dx=h_i)}')

print('\n           Valores numéricos         ')
for h_i in h:
    print(f'\nLa derivada hacia adelante con h={h_i} es: {derivada_adelante(fx, xi, h_i)}')
    print(f'La derivada hacia atrás con h={h_i} es: {derivada_atras(fx, xi, h_i)}')
    print(f'La derivada centrada con h={h_i} es: {derivada_centrada(fx, xi, h_i)}\n')

y_tangente = fx(xi)
dy_tangente = derivative(fx, xi, dx=0.01)  

x_vals = np.linspace(-2, 4, 500) 
y_vals = fx(x_vals)                 
dy_vals = [derivative(fx, xi, dx=0.01) for xi in x_vals]  
tangente_vals = tangente(x_vals)  

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label="Función $f(x)$", color="blue")
plt.plot(x_vals, dy_vals, label="Derivada $f'(x)$", color="red", linestyle="--")
plt.plot(x_vals, tangente_vals, label="Tangente en $x = {}$".format(xi), color="green", linestyle=":")
plt.scatter([xi], [y_tangente], color="black", zorder=5, label=f"Punto tangente ($x={xi}$, $y={y_tangente}$)")
plt.axhline(0, color="black", linewidth=0.8, linestyle=":")
plt.axvline(0, color="black", linewidth=0.8, linestyle=":")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.legend()
plt.grid(True)
plt.show()


