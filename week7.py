# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 10:05:41 2022

@author: Asus
"""

from math import pi,sqrt
import numpy as np
x=4.
R=1.0
def f(x):
#    x=input('enter x')# never do this.
    return float(x)*float(x)
 
def g():
    x=input('enter x')# this is okey
    return float(x)*float(x)
def surface(r):
    pi=3.14#local variable pi(3.14) overrides global variable
    s=r**2*pi
    return s
def circle(r):
    p=2.*pi*r
 #   pi=3.14 local pi can not be defined because global pi has been used 
    s=pi*r**2
    return (p,s)
def sqr(x):
    x=x*x
    print('printing local x=',x)
    return x
def parabola(x,a,b,c):
    return a*x**2+b*x+c
def magnitude(x,y=0):# 0 is the default value for y,y is optional input
        return sqrt(x*x+y*y)
def integration(f,a,b,n):#f function to be integrated, integral from a to b
    # n is the number of integration points
    vx=np.linspace(a,b,n,False)
    h=vx[1]-vx[0]
    return (f(vx).sum()*h)
def integration2(f,a,b,n,args=[]):#f function to be integrated, integral from a to b
    # n is the number of integration points
    vx=np.linspace(a,b,n,False)
    h=vx[1]-vx[0]
    return (f(vx,*args).sum()*h)
def fcircle(x):
    return np.sqrt(1.-x*x)
def latitude_surface_area(x,z):
    s=np.sqrt(R**2-z**2-x**2)
    return s
y=sqr(x)
print('global x=',x)
print('y=',y)
print('surface=',surface(1.))
c,a=circle(1.)
res=circle(1.)
a=2.
b=0.
c=0.
y=parabola(10.,b,c,a)
y=f(3.)
print('f(x)=',y)
print('mag',magnitude(4.,3,))
print('mag',magnitude(4.))
int_=integration(fcircle,0.,1.,100000)
print('int_=',int_,' ',pi*.25)
vec=[4.,3.]
print('mag with *vec',magnitude(*vec))
# let's compute the surface area of a latitude at z=R/2. 
z=R/2
Arg=[R/2.]
a=-(R**2-z**2)**0.5#(R**2-z**2)**0.5 is radius of latitude
b=-a
res=4.*integration2(latitude_surface_area,0.,b,10000,Arg)
print('lat. sur.=',res,' ',pi*(R**2-z**2))

