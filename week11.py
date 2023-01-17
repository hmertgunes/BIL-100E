import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
N=10
xmax=.4
vx=np.linspace(0.0,xmax,N,False)

ck1=1.0
ck2=0.0   
E = .5 * ck1 * xmax **2 + .5 * ck2 * xmax**4
mat=np.zeros((N,N),dtype=float)
right=np.zeros(N,dtype=float)
def f(x):
    den=2*(.5*ck1*xmax**2 + .5* ck2*xmax**4)
    den2=2*(.5*ck1*x**2 + .5* ck2*x**4)
    s=1./np.sqrt(den-den2)
	
    return s
def intergrand(x,coeff):
    N=coeff.size
    series=-coeff*(xmax-x)**(np.arange(N)+0.5)/(np.arange(N)+0.5)
    return series.sum()
    
def integral(start,end_,coeff):
     return intergrand(end_,coeff)-intergrand(start,coeff)
    
yy=np.zeros(N,dtype=float)
# for k1 in range(vx.size):
#     yy[k1]=f(vx[k1])   
#  	for k2 in range(vx.size):  
#         mat[k1, k2] = (xmax- vx[k1]) ** (k2 -0.5)
for k1 in range(vx.size):
    yy[k1]=f(vx[k1])
    for k2 in range(vx.size):
        mat[k1,k2]=(xmax-vx[k1])**(k2-0.5)

right=f(vx)		
plt.plot(vx,right,vx,yy)
plt.show()
va=np.linalg.solve(mat,right)
res=integral(0.,xmax*(1.-1.0e-15),va)
print(res,0.5*np.pi,res-0.5*np.pi)