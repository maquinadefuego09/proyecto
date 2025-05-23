# -*- coding: utf-8 -*-
"""
Created on Thu May 22 22:10:47 2025

@author: osbal
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/ybifoundation/Dataset/main/Salary%20Data.csv')
X = df['Experience Years']
Y = df['Salary']
sum_xiyi = sum(X*Y) 
sum_xi2 = sum(X**2) 
n = len(X) 

ap = (n*sum_xiyi-sum(X)sum(Y))/(n*sum_xi2-sum(X)*2)
a0 = (sum(Y)-a1*sum(X))/n

X_grafica = np.linspace(min(X),max(X),150)
Y_grafica = a0+ap*X_grafica
y_regression = lambda x: a0+ap*x
datos_estimar = [15,30,50]
for dato in datos_estimar:q
    print(f'Años {dato}: salario y regresión {dato})')

plt.plot(X_grafica,Y_grafica)
plt.plot(X,Y,'o')
plt.grid()
plt.show()