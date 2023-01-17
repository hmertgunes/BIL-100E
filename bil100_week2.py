"""
Created on Tue Sep 27 08:35:14 2022
Bil 100 course week 2 

@author: mert
"""


from math import *
import numpy as np
import matplotlib.pyplot as plt

s = "{:12.2e}".format(2)
r = "{:.3f}".format(pi)
print(r)

#%%
#garbage collecter önemli !!
#fortran lapack
#reel büyüklük ve fiziksel büyüklük 
#matris çarpımı n tane işlem demek, total (2n^3)


a = np.random.random((5000,5000))
b = np.random.random((5000,5000))

from time import time

t1 = time()
c = np.dot(a,b)
t2 = time()
print(t2-t1)


#%%

#tuple
a = (2,"nazmi")

# numpy shape = matlab size

zeross = np.zeros((2,2), dtype=float)
print(zeross.size)

#%%

myfile = open("matrix.csv", "w")
asd = np.zeros((2,2))
asd[0,1] = 3.2
 
myfile.write(str(asd[0,0]) + " , " + str(asd[0,1]) + "\n")
myfile.write(str(asd[1,0]) + " , " + str(asd[1,1]) + "\n")

myfile.close()

myfile2 = open("matrix.csv", "r")
readlines = myfile2.readlines()
m = np.zeros((2,2), dtype=float)
splited =readlines[0].split(" , ")

m[0,0] = float(splited[0])
m[0,1] = float(splited[1])
myfile2.close()



#%%

vx = np.linspace(0., 1., 3, False)
print(vx)

#%%
# integral
vx = np.linspace(0.,1.,int(1.e+06), False)
width = vx[1] - vx[0]
weights = vx*vx
integral = width*weights.sum()
print(integral," error=",  integral-1./3)

#%%

vx = np.linspace(0., 1., 1000)
plt.plot(vx, vx**2,label = "vx**2") 
plt.plot(vx, vx**3, label="vx**3")
plt.plot(vx, vx**4, linestyle="--",  color="k", label="vs**4")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend()
plt.show()


#%%


mymat = np.array([[1.,2.,], [0., 20.]])
for k in range(20):
    print(k)


#%%
v = np.arange(20)
print(v[3:6])


h = np.hstack((v[:5], v[9:]))
print(h)

for k in v[20:2:-1]:
    print(k)
    
for k in v[::-1]:
    print(k)
    
#%%

#izdüşüm bulmak 

#presesyon ve nutasyon



randints = np.random.randint(0,100,100)
print("randints")
print(randints)
r = np.arange(randints.size)
print("r")
print(r[randints %2 == 0])


#%%


















