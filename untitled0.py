# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 14:41:48 2020

@author: EQUIPO 36
"""

import numpy as np
import math
import matplotlib.pyplot as plt

x = [1,3,5,2,4,6,1,3,6,4]
y = [2,4,6,1,3,5,4,2,3,5]
x_promedio = sum(x)/len(x)
y_promedio = sum(y)/len(y)
d=[]
c=[]
e=[]
for i in range(len(x)):
  d.append((x[i]-x_promedio)**2)
  i=i+1
des_x=np.sqrt(sum(d)/len(x))

for i in range(len(y)):
  c.append((y[i]-x_promedio)**2)
  i=i+1
des_y=np.sqrt(sum(c)/len(y))

for i in range(len(x)):
  e.append(y[i]*x[i])
  i=i+1
cova=(sum(e)/len(x)-x_promedio*y_promedio)
print(des_x)
print(des_y)
print(cova)

rho= (cova/(des_x*des_y))
print(rho)

b=rho*(des_y/des_x)
a=y_promedio-b*x_promedio

def f1(x):
  return a+b*x
print(b)
print(a)

plt.plot(x,y,'o')
plt.plot(x,[f1(i) for i in x])
print(x)
print(y)

#Sx = np.sqrt(sum(abs(x-x_promedio)^2)/len(x))
#print(x_promedio,y_promedio)
#print(Sx)

#Resultado será 13
