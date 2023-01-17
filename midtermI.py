# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 09:40:51 2022

@author: Asus
"""


import numpy as np
import matplotlib.pyplot as plt
from math import cos,sin,pi,sqrt
print('problem 1')
def fact(N):
    res=np.ones(N+1,dtype=float)
    for k in range(1,res.size):
        res[k]=k*res[k-1]
    return res
def my_sinh(x,N):
    max_power=2*(N-1)+1
    factorial=fact(max_power)
    x2=x*x
    xp=x#powers of x
    first_term=xp/factorial[1]
    for k in range(1,N):
        xp*=x2#x power updated
        first_term+=xp/factorial[2*k+1]
    return first_term
print(my_sinh(.5,10),' ',np.sinh(.5))
#*************************************
print('problem 2')
vx=np.linspace(-8.,8.,1000)
vy=np.cosh(vx*vx)
bo=vy<10*vx*vx#boolean array
plt.plot(vx[bo],vy[bo])
plt.show()
#**********************Problem 3
print('problem 3')
N=int(1.0e04)
M=np.zeros((4,N),dtype=float)
v0=200.
initial =np.array([0.0,0.0, v0*cos(0.25*pi), v0*sin(0.25*pi)])
M[:,0]=initial[:]
h=30./N
gamma=1.04e-04
#gamma=0.
vt=np.arange(N)*h#instants
for k in range(1,N):
    v=np.array([M[2,k-1],M[3,k-1]])#velocity at instant (k-1)*h
    speed=np.linalg.norm(v)
    x_pr,y_pr, vx_pr,vy_pr=tuple(M[:,k-1])# pr stand for 'previous'
    x_now=x_pr+h*vx_pr
    y_now=y_pr+h*vy_pr
    speed2=speed*speed
    vx_now=vx_pr      -gamma*h*speed2*vx_pr/speed
    vy_now=vy_pr-h*9.8-gamma*h*speed2*vy_pr/speed
    now=np.array([x_now,y_now,vx_now,vy_now])
    M[:,k]=now[:]
x_positions=np.array(M[0])
y_positions=np.array(M[1])
tiny=-0.0001
positive= y_positions>tiny
vt_pos=vt[positive]
print('real flight time=',vt_pos.max(),' ideal=',2.*v0*sin(.25*pi)/9.8)
plt.plot(x_positions[positive],y_positions[positive])
plt.show()
#******************************
print('problem 4')
def integrate(f,a,b,N):
    vx=np.linspace(a,b,N,False)
    h=(b-a)/N
    vy=f(vx)
    return h*vy.sum()
def integrate_multi(f,a,b,N,arg=[]):
    vx=np.linspace(a,b,N,False)
    h=(b-a)/N
    vy=f(vx,*arg)
    return h*vy.sum()
def g(x,y,z):
    return x*x+y*x+z
print('integral of g=',integrate_multi(g,0.,10.,10000,[3.,4.]))
    
    
    

