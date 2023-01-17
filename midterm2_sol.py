# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 09:35:42 2022

@author: Asus
"""

import numpy as np
import matplotlib.pyplot as plt
#this part of the program produces data (examinee are not required to generate
# data,they are going to use existiong data)
vx=np.linspace(0.,1.,10)
vy=np.cosh(vx)
out=open('myfile.dat','w')
for k in range(vx.size):
    str_=str(vx[k])+' '+str(vy[k])+'\n'
    out.write(str_)
out.close()
#################################solutio
######reading the data
in_=open('myfile.dat','r')
l=in_.readlines()
vx=np.zeros(len(l),dtype=float)
vy=np.array(vx)
for k in range(len(l)):
    row_splitted=l[k].split()
    vx[k]=float(row_splitted[0])
    vy[k]=float(row_splitted[1])
# plt.plot(vx,vy,np.linspace(0.,1.0,100),np.cosh(np.linspace(0.,1.0,100)))
# plt.show()
mat=np.zeros((vx.size,vx.size),dtype=float)
current=np.ones(vx.size,dtype=float)#first column is ones
for k in range(vx.size):
    mat[:,k]=current
    current*=vx
    
va=np.linalg.solve(mat,vy)
def value(x,va):
    if(type(x)==np.ndarray):
        s=np.zeros(x.size,dtype=float)
        current=np.ones(x.size)# current is the current power of x
    else:
        s=0.
        current=1.
    for k in range(va.size):
        s+=va[k]*current
        current*=x
    return s
def Derivative(x,va):
    if(type(x)==np.ndarray):
        s=np.zeros(x.size,dtype=float)
        current=np.ones(x.size)# current is the current power of x
    else:
        s=0.
        current=1.
    for k in range(1,va.size):
        s+=k*va[k]*current
        current*=x
    return s
               
    
vx=np.linspace(0.,1.,100)

plt.plot(vx,value(vx,va),vx,np.cosh(vx))
plt.xlabel('vx')
plt.ylabel('value(vx,va) and np.cosh(vx)')
plt.show()
plt.plot(vx,Derivative(vx,va),vx,np.sinh(vx))
plt.xlabel('vx')
plt.ylabel('Derivative  and np.sinh(vx)')
def Riemann(f,a,b,N,args=[]):
    vx=np.linspace(a,b,N,False)
    vy=f(vx,*args)
    h=(b-a)/N#more accurate than h=vx[1]-vx[0] if N is large
    return h*vy.sum()
def decay(t,tau):
    return np.exp(-t/tau)
integral=Riemann(decay,0.,1.,1000,[3.])
print('integral=',integral,' ',-(np.exp(-1./3.)-1.)*3.)
#####################################################
#################Problem 5
#will print 14 local x(right side)=2,y=3 [first line of the output]
#will  print from the main program x is 2 [second line of the output]
#it will print 11

vx=np.linspace(1.,4.,int(1.0e05))
larger=10.+np.exp(vx)>np.exp(vx**2)
subarray=vx[larger]
print(subarray.max())

    
