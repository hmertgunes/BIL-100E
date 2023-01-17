# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 12:31:48 2022

@author: Asus
"""
import numpy as np
import matplotlib.pyplot as plt

class Circle:
        def __init__(self,x_,y_,R_):
            self.x=x_#x coordinate of the center of the circle (attribute)
            self.y=y_#y coordinate of the center of the circle (attribute)
            self.R=R_
        def is_in(self,x,y):#returns True if point x,y lies inside the circle
            d2=(self.x-x)**2+(self.y-y)**2
            if (d2<self.R**2):
                return True
            else:
                return False
        def Area(self):
            return np.pi*self.R**2
        def Shift(self,x,y):#will return shifted circle
            x+=self.x
            y+=self.y
            return Circle(x,y,self.R)
        def plot(self):
            vtheta=np.linspace(0.0,2.*np.pi,200)
            plt.axis(aspect='equal')
            vx=self.x+self.R*np.cos(vtheta)
            vy=self.y+self.R*np.sin(vtheta)
            plt.plot(vx,vy)
        def polygone(self)  :#returns a polygone that approximates the circle
            vtheta=np.linspace(0.0,2.*np.pi,200)
            vx=self.x+self.R*np.cos(vtheta)
            vy=self.y+self.R*np.sin(vtheta)
            return vx,vy
c1=Circle(2.,2.,0.5)# an instance of circle
c1.plot()
c2=c1.Shift(0.25,.25)# another  instance of circle(shifted c1)

c2.plot()
plt.axis('equal')