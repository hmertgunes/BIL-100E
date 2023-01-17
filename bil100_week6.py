"""
Created on Tue Oct 25 08:28:28 2022

@author: mert
"""

from math import atan, sin, cos
import numpy as np
import matplotlib.pyplot as plt

#sonsuzun arctan'ını makine alamıyor

pi = atan(1.) * 4.

def sinus(degree):
    radian = degree/180 * pi
    return sin(radian)

#%%

# zaman , 0 anındaki komut ve hız
# tuple return, (konum, hız)
# g global değişken g = 9.81
# 0da 0hız ve konum 5 sn için 100 ayrı anda konum ve hız çizdir aynı grafikte
 

g = -9.81
vt = np.linspace(0,1.5,100)


def free_fall(t, x0, v0):
    x = v0*t + 0.5*g*t**2
    v = v0 + g*t
    
    return (x,v)
    

(vkonum, vhiz) = free_fall(vt,0,0)

# plt.plot(vt, vkonum, label="konum", color="r")
# plt.plot(vt, vhiz, label="hiz")
# plt.legend()
# plt.show()


#%%

g = -9.81
 
def egik_atis(t,v0, radian):
    vxinit = v0 * cos(radian)
    vyinit = v0 * sin(radian)
    
    ykonumlar, yhizlar = free_fall(t, 0, vyinit)
    xkonumlar = vxinit * t
    
    return (xkonumlar, ykonumlar)

xkonumlar, ykonumlar = egik_atis(vt, 5, pi/4)

plt.plot(vt, ykonumlar)

