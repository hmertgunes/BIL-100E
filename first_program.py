# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 10:30:43 2022

@author: Asus
"""

import numpy as np
N=20
for k in range(10):
    print('k=',k)
    print('hello')
print("I'm outside of the loop")
s=0
for k in range(11):
    s=s+k
print('sum=',s,' ',np.arange(11).sum())
fact=np.ones(N+1,dtype=float)
for k in range(1,N+1):
    fact[k]=fact[k-1]*k
powers=1.0
s=0.0
x=2.
for k in range(N+1):
    s+=powers/fact[k]
    powers*=x
print(s,' ',np.exp(x), 'error=',s-np.exp(x))