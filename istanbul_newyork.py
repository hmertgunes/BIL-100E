# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 10:50:01 2022

@author: Asus
"""
import numpy as np
from math import pi,acos
import  matplotlib.pyplot as plt
#from mpl_toolkits import mplot3d 
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(figsize=(4,4))

ax = fig.add_subplot(111, projection='3d')


def cosd(x):
    return np.cos(pi*x/180.)
def sind(x):
    return np.sin(pi*x/180.)
theta_ist=90.-41.0082
phi_ist=28.978
theta_new=90.-40.712
phi_new=-74.006
R0=6.371e06
R=1.0
ist=np.array([R*sind(theta_ist)*cosd(phi_ist),\
   R*sind(theta_ist)*sind(phi_ist) ,R*cosd(theta_ist)])
new=np.array([R*sind(theta_new)*cosd(phi_new),\
   R*sind(theta_new)*sind(phi_new) ,R*cosd(theta_new)])
gamma=acos((ist*new).sum() /R**2 )
distance=R*gamma 
normal=np.cross(ist,new)
normal=normal/np.linalg.norm(normal)
j_star=np.cross(normal,ist)
vgamma=np.linspace(0,gamma,200)
vx=ist[0]*np.cos(vgamma)+j_star[0]*np.sin(vgamma)
vy=ist[1]*np.cos(vgamma)+j_star[1]*np.sin(vgamma)
vz=ist[2]*np.cos(vgamma)+j_star[2]*np.sin(vgamma)
ax.plot3D(vx, vy, vz, 'gray')
ax.scatter(0.0,0.0,R)
ax.scatter(0.0,0.0,-R)
plt.zlim(-1.,1.)
plt.xticks(np.linspace(-R,R,6))
plt.yticks(np.linspace(-R,R,5))
#ax.zticks(np.linspace(-R,R,5))
#ax.plot(vx,vy)
s="{:12.4e}".format(distance*R0)
print(s)
