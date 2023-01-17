# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 10:23:51 2022

@author: Asus
"""

import matplotlib.pyplot as plt
import numpy as np
from math import pi

N = 10
M = np.zeros((N,N))
xmax = 0.4
vx = np.linspace(0, xmax, N, False)

a=1.
b=0

def fe(x):
    return 0.5*a*x**2 + 0.5*b* x**4

E = fe(xmax)

def f(x):
    return 1./np.sqrt(2*(E - fe(x)))

right = np.zeros(N)
for k1 in range(M.shape[0]):
    right[k1] = f(vx[k1])
    for k2 in range(M.shape[1]):
        M[k1,k2] = (xmax - vx[k1]) ** (k2 - 0.5)
    
A = np.linalg.solve(M, right)

def fitted(x, a):
    mysum = 0*x
    for k in range(a.size):
        mysum += a[k] * (xmax - x) ** (k - 0.5)
    return mysum

vx = np.linspace(0, xmax, 100, False)
plt.plot(vx, fitted(vx, A), vx, f(vx))

def integrate(A, xmax, N):
    p = (np.arange(N) + 0.5)
    return (A * (xmax ** p / p)).sum()

myint = integrate(A, xmax, N)
print(str(myint) + " " + str(pi/2))
    