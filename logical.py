# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 09:59:40 2022

@author: Asus
"""

import numpy as np
bo=3>4
print(bo)
not_bo=not bo
bo_or=not_bo or bo
print('bo_or=',bo_or)
bo_and=not_bo and bo
print('bo_and=',bo_and)
vint=np.zeros(10,dtype=int)
vint[:]=np.random.random(10)*100.
#vint=np.random.random(10)
bo=vint%2==0
indices=np.arange(vint.size)
print('even integers=',vint[bo])
print('even integers=',vint[~bo])
print('indices of even elements=',indices[bo])
bo2=np.zeros(10,dtype=bool)
