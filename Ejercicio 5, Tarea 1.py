# -*- coding: utf-8 -*-
"""
Osbaldo Corpus Castillo
348071
Programacion Numerica
Problema 5, Tarea 1, Ejercicio 3-4 pero con funciones jaja
""" 
import numpy as np 
import random

def generar_vector(N):
    return [random.randint(1, 9) for _ in range(N)]
def generar_matriz_filas(X, N):
    matriz = []
    for i in range(N): 
        fila = []
        for j in range(1, N + 1):
            fila.append(X[i] * j)
        matriz.append(fila)
    return matriz
def generar_matriz_columnas(X, N):
    matriz = []
    for i in range(N):
        fila = []
        for j in range(N):
            fila.append(X[j] * (i + 1))
        matriz.append(fila)
    return matriz
def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

N = 5

X=generar_vector(N)
print(f"Vector: {X}")
matriz1 = generar_matriz_filas(X, N)
print("Matriz con múltiplos en las filas:")
imprimir_matriz(matriz1)
matriz2 = generar_matriz_columnas(X, N)
print("Matriz con múltiplos en las columnas:")
imprimir_matriz(matriz2)
