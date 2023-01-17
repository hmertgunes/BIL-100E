# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 17:50:48 2022

@author: Asus
"""

import numpy as np
#1) Write a program that will open the file 'myfile.dat' read two columns of 
#float separeted by space. The first column will become numpy array vx, 
# the second array vy
#a polynomial of degree N-1 ,P(x)=a_0+a_1*x+a_2*x^2+..+a_{N-1}*x^{N-1})
# will pass through these points. N is the number of poins (number of lines in 
# myfile.dat)
#using linalg.solve from numpy find a numpy array of length N that will contain
#the coefficients a_0,a_1,...

#2) write a function that will return the value of he polynomial associated 
#with va at vx (vx can be a numpy array)
def value(x,va):
    ...
    return ...
#3) Write a function that will return the derivative of polynomail associated 
#with va at x
def Derivative(x,va):
      ...
      return ...
# 4) Write a function that will integrate a function f with respect
# to its first argument from a to b using Riemann sum (\sum_{k=0}^{N-1} h*f(a+k*h)) 
#where h=(b-a)/(N-1); wich function from numpy will compute all the points
      # a+k*h with a single command. How do you call it?
  #the protype of Riemann integration is
def Riemann(f,a,b,n,extra_arguments=[]) :
    ...
    return ...
#Use the function above to integrate function
def decay(t,tau):
    return np.exp(-t/tau)
#from 0 to 1 using 1000 point (kappa is set 3) 
    #################################################
#problem 5
x=2
def topla(x,y):
    x=x+4*y
    print('from topla x is',x)
    return x
y=3.
a=topla(x,y)
print('from main program x is ',x)
b=topla(y,x)
#write output of this program
#
###########problem 6
#let vx be array of 10e05 equidistant points between 1. and 4. 
#find a subarray of vx such as 10.+exp(x)>exp(x^2)
#what s the maximum of this subarray
