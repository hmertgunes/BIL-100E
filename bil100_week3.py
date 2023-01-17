"""
Created on Tue Oct  4 08:36:48 2022
Bil 100 course week 3

@author: mert
"""

#%%

import numpy as np
import math

vx = np.array([1.,2.,3.])
vy = vx
vy2 = vx + 1.0
vy3 = np.array(vx)
v2x = vx*vx

magnitude = math.sqrt((vx*vx).sum())
magnitude2 = np.linalg.norm(vx)
magnitude3 = math.sqrt(np.dot(vx, vx))

#%%
# dot product, matris çarpımları
# 2 vektör cross sonra çıkanla scaler = hacim

a = np.array(vx) + 2.
b = np.array(vx)  
ab = np.cross(a, b)


#%%
# HINGE EXAMPLE

A = np.array([1.,2.,10.])
Q = np.array([2.,2.,3.])
F = np.array([2.,1.,-10.])
P = np.array([1.,1.,2.])
PA = A - P
n_hat = np.array([1.,1.,1.]) * (1 / math.sqrt(3.))
t_hat = PA / np.linalg.norm(PA) # büyüklüğünü bulan formül

# n_hat . (OP x T + OQ x F) = 0

# t = 

T = np.dot(-n_hat , np.cross(Q, F)) / np.dot(n_hat, np.cross(P, t_hat))
print(T)

# %%

def cosd(x):
    return np.cos(math.pi*x / 180.)

def sind(x):
    return np.sin(math.pi*x / 180.)

R = 6.371e06

# istanbul (41.0082° N, 28.9784° E)
x = R * sind(90. - 41) * cosd(28.98)
y = R * sind(90. - 41) * sind(28.98) 
z = R * cosd(90. -41)

ist = np.array((x,y,z))

# new york (40.7128° N, 74.0060° W)
x1 = R * sind(90. - 40) * cosd(-74.)
y1 = R * sind(90. - 40) * sind(-74.)
z1 = R * cosd(90. - 40)

newy = np.array((x1, y1, z1))


tht = math.acos(np.dot(ist, newy) / (np.linalg.norm(ist) * np.linalg.norm(newy)))
distance = R * tht
angle = tht * 180. / math.pi


normal = np.cross(ist, newy)
normal = normal / np.linalg.norm(normal)


j_star = np.cross(ist, newy)
v_tht = np.linspace(0, tht, 200)

vx = ist[0] * np.cos(v_tht) + j_star[0] * np.sin(v_tht)
vx = ist[1] * np.cos(v_tht) + j_star[1] * np.sin(v_tht)
vx = ist[2] * np.cos(v_tht) + j_star[2] * np.sin(v_tht)





















