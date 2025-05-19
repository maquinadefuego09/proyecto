# -*- coding: utf-8 -*-
"""

Osbaldo Corpus Castillo
Programacion Numerica 
TAREA 5: DERIVACION E INTEGRACIÓN NUMÉRICA

@author: osbal
"""

import numpy as np
from sympy import symbols, cos, exp, integrate
x = symbols('x')

f1 = 2*cos(2*x)     
f2 = -x**2-x/2+4       
f3 = exp(-x**2)               

f1_np = lambda x: 2*np.cos(2*x)
f2_np = lambda x: -(x**2)-(x/2)+4
f3_np = lambda x: np.exp(-x**2) 

a = [0,0.5,0]              
b = [np.pi/4,1.5,1]      

funciones_analiticas = [f1, f2, f3]
funciones_numericas = [f1_np, f2_np, f3_np]

def error (va,vn):
    return np.abs((va-vn)/va)*100

def simpson_13(f, a, b):
    x1 = a + (b - a) / 2     
    I = (b - a) * ((f(a) + 4 * f(x1) + f(b)) / 6)
    return round(I, 4)

def simpson_68(f,a,b):
    h=(b-a)/3
    x1= a+h
    x2=a+(2*h)
    I=(b-a)*(f(a)+3*(f(x1)+f(x2))+f(b))/8
    return round(I, 4)
def trapecio_simple(f, a, b):
    I = (b-a)*(f(a)+f(b))/2  
    return round(I, 4)
def trapecio_multiple2(f, a, b, n):
    h=(b-a)/n   
    x1=a+h               
    I = (b-a)*((f(a)+2*(f(x1))+f(b))/(2*n))
    return round(I, 4)
def trapecio_multiple4(f, a, b, n):
    h = (b - a) / n   
    x1=a+h
    x2=a+2*h
    x3=a+3*h               
    x_vals = np.linspace(a, b, n + 1) 
    I = (b-a)*((f(a)+2*(f(x1)+f(x2)+f(x3))+f(b))/(2*n))
    return round(I, 4)
def trapecio_multiple6(f, a, b, n):
    h=(b-a)/n   
    x1=a+h
    x2=a+2*h
    x3=a+3*h
    x4=a+4*h               
    x5=a+5*h                              
    x_vals = np.linspace(a, b, n + 1) 
    I = (b-a)*((f(a)+2*(f(x1)+f(x2)+f(x3)+f(x4)+f(x5))+f(b))/(2*n))
    return round(I, 4)

def integral_definida(funcion,a,b):
    integral = integrate(funcion, x)  
    valor_integral = integral.subs(x,b)-integral.subs(x,a)  
    return round(valor_integral, 4)

print('          Funcion e integral           ')
for i, funcion in enumerate(funciones_analiticas):
    integral = integrate(funcion, x)  
    valor_definida = integral_definida(funcion, a[i], b[i]) 
    print(f' \nFuncion {i+1}= {funcion}')
    print(f'Su integral es:{integral}')
    print(f'Su valor analitico es: {valor_definida}')

print('\n         Calculo con los metodos y error relativo      ')
n_subintervalos1 = 4 
n_subintervalos2 = 2
n_subintervalos3 = 6  

for i in range(len(a)):
    print(f'\nFuncion {i+1} ')
    resultado_trap_simple = trapecio_simple(funciones_numericas[i], a[i], b[i])
    print(f'1)  Trapecio simple es: {resultado_trap_simple}')
    resultado_trap_multiple2 = trapecio_multiple2(funciones_numericas[i], a[i], b[i], n_subintervalos2)
    print(f'2)  Trapecio múltiple con {n_subintervalos2} trapecios es: {resultado_trap_multiple2}')
    resultado_trap_multiple4 = trapecio_multiple4(funciones_numericas[i], a[i], b[i], n_subintervalos1)
    print(f'3)  Trapecio múltiple con {n_subintervalos1} trapecios es: {resultado_trap_multiple4}')    
    resultado_trap_multiple6 = trapecio_multiple6(funciones_numericas[i], a[i], b[i], n_subintervalos3)
    print(f'4)  Trapecio múltiple con {n_subintervalos3} trapecios es: {resultado_trap_multiple6}')
    resultado_simpson13 = simpson_13(funciones_numericas[i], a[i], b[i])
    print(f'5)  Simpson 1/3 es: {resultado_simpson13}')
    resultado_simpson68 = simpson_68(funciones_numericas[i], a[i], b[i])
    print(f'6)  Simpson 6/8 es: {resultado_simpson68}')
