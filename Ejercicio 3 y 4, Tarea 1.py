# -*- coding: utf-8 -*-
"""
Osbaldo Corpus Castillo
348071
Programacion Numerica
Problema 3 y 4, Tarea 1, Matriz usando multiplos de un vector aleatorio para las columnas
""" 
import numpy as np
import random

N = 4
X = [random.randint(1, 9) for _ in range(N)]
print(f"Vector:{X}")
matriz1 = []
for i in range(N):
    fila = []
    for j in range(1, N + 1):
        fila.append(X[i] * j)
    matriz1.append(fila)
print("Matriz:")
for fila in matriz1:
    print(fila)

matriz2 = []
for i in range(N):
    fila = []
    for j in range(N):
        fila.append(X[j] * (i+1))
    matriz2.append(fila)
print("Matriz:")
for fila in matriz2:
    print(fila)