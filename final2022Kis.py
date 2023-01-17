# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 10:46:41 2023

@author: Asus
"""
from cmath import phase
from math import sqrt,cos,sin
import numpy as np

class Square:
    def __init__(self,zc,za=1.0+1.0j):
        if(type(zc)==complex):#this test is necessary for section (f)
            self.a=sqrt(za.imag**2+za.real**2)
            self.phi=phase(za)
            self.xc=zc.real
            self.yc=zc.imag
        else:
            if(type(zc)==Square):
                self.a=zc.a
                self.xc=zc.xc
                self.yc=zc.yc
                self.phi=zc.phi
            else:
                exit('error in calling constructor Square')
    def perimeter(self):
        return 4.*self.a
    def shift(self,xshift,yshift):
        zc=complex(self.xc+xshift,self.yc+yshift)
        za=self.a*complex(cos(self.phi),sin(self.phi))
        return Square(zc,za)
    def rotate(self,x,y,theta):
        z0=complex(cos(theta),sin(theta))
        z1=complex(x,y)
        res=z0*z1
        return (res.real,res.imag)
    def is_in(self,x,y):
        (xr,yr)=self.rotate(x,y,-self.phi)
        (xcr,ycr)=self.rotate(self.xc,self.yc,-self.phi)
        box= ((xcr-self.a/2)<xr) and ((xcr+self.a/2)>xr)#boolean varibal
        boy= ((ycr-self.a/2)<yr) and ((ycr+self.a/2)>yr)
        return ( box and boy)
##section(g)
z=complex(1.,0.)
zz=z+0.
s1=Square(z,zz)
s2=Square(s1)#independent copy of s1
s2.a=100# s1 is not affected because s2 is an independent copy
print('no operation made on s1.a=',s1.a)
s3=s1 #s1 and s3 share the same memory
s3.a=100.
print('second time, no operation made on s1.a=',s1.a)
#######################
###########problem 2
def polynom2(vx,vy):
    m=np.zeros((vx.size,vx.size),dtype=float)
    N=vx.size
    xcurrent=np.ones(N,dtype=float)
    for k in range(N):
        m[:,k]=xcurrent
        xcurrent=vx*xcurrent#xcurrent will be x_0^k,x_1^k,x_2^k...
    return np.linalg.solve(m,vy)
#################problem 3
def P(x,C):
    s=0.0#s start life a  float , may become an array later on
    xpower=1.0+0.*x
    
    for k in range(C.size):
        s=s+xpower*C[k]
        xpower=xpower*x
    return s
#######################problem 4
def PdP(x,C):
    s=0.0#s start life a  float , may become an array later on
    xpower=1.0+0.*x
    ds=0.0
    powers=[xpower]*C.size# a list of length C.size that will contain the 
    #powers of x
    for k in range(1,C.size):
        powers[k]=x*powers[k-1]# x can be a float or numpy array
    for k in range(C.size):
        s=s+C[k]*powers[k]
    for k in range(1,C.size):
        ds=ds+C[k]*powers[k-1]*k
    return (s,ds)
vx=np.linspace(0.0,1.,10)
vy=np.exp(vx)
C=polynom2(vx, vy)
X=np.ones(3,dtype=float)*( vx[8]+vx[9])*.5# interpolate to the middle of ( vx[8]+vx[9])*.5
(exp_,dexp)=   PdP(X,C)   # evaluate polynom at X and  its derivative 
exact=np.exp(X)
print(exp_-exact,dexp-exact)
############################
#problem 5
def Lagrange(x,vx,vy):
    s=0.
    for k1 in range(vx.size):
        pr=1.0
        for k2 in range(vx.size):
            if(k2!=k1):
                pr=pr*(x-vx[k2])/(vx[k1]-vx[k2])
        s=s+pr*vy[k1]
    return s
exp_=Lagrange(X,vx,vy)
print('lagrange error=',exp_-exact)
  
    