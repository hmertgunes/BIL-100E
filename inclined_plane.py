# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 10:57:53 2022

@author: Asus
"""

import matplotlib.pyplot as plt
import numpy as np
from math import cos,sin,tan,atan

pi = np.pi
N = 20000
m = 1.0
g = 9.81
h = 1.0e-03 #1*10^(-2)  time step
v0 = 5. #initial horizontal velocity
v2_velocities = np.zeros((2,N),dtype=float)
v2_positions = np.zeros((2,N),dtype=float)
tiny = 1.0e-16
v2_velocities[1,0] = v0
v2_velocities[0,0] = tiny
theta_0 = pi/6
mu = tan(theta_0)
k = 0
Normal = m*g*cos(theta_0)
friction_force = Normal*mu
sin_= sin(theta_0)
phi = 0.0


while( (v2_velocities[1,k]>0.0005*v0 ) and(k<N)):
    phi=atan(v2_velocities[1,k]/v2_velocities[0,k])
    friction_force_x=-friction_force*cos(phi)
    friction_force_y=-friction_force*sin(phi)
    ax=g*sin_+friction_force_x/m
    ay=friction_force_y/m
    v2_velocities[0,k+1]=v2_velocities[0,k]+h*ax
    v2_velocities[1,k+1]=v2_velocities[1,k]+h*ay
    v2_positions[0, k+1]=v2_positions[0,k]+h*ax
    v2_positions[1, k+1]=v2_positions[1,k]+h*ay
    
    k=k+1


print(v2_velocities[0,k-1])
initial_speed=5.
theta_0=pi/4.

# plt.quiver(0,0, v2_positions[0,:k], v2_positions[1,:k])
plt.plot(v2_positions[0,:k], v2_positions[1,:k])
plt.show()




