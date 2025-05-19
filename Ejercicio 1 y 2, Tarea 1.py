# -*- coding: utf-8 -*-
"""
Osbaldo Corpus Castillo 
348071
Programacion Numerica
Problema 1 y 2, Tarea 1, Verificacion de un numero entero positivo, generacion
de vector con numeros aleatorios
"""
import numpy as np
import random

N = 9
if  not isinstance(N, int):
    print("No es un número entero")
elif N <= 0:
    print("No es un número positivo")
else:
    print("Si es un entero positivo")
    X = [random.randint(1, 9) for _ in range(N)]
    print(f"Vector: {X}")
    
    