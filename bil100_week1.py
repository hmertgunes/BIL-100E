"""
Created on Tue Sep 20 09:56:49 2022
Nazmi Postacıoğlu bil 100 week-1

@author: mert

"""
#%%

z = 1.0 + 1.0j

ans = open("answer.txt", mode="w")
ans.write(str(z))
ans.close()
    

with open("answer1.txt", mode="w") as ans1:
    ans1.write("nazmi postacioglu \n")
    ans1.write(str(z) *2)
    ans1.close()
    

a = "nazmi"
b = "mert"

#%%

# from math import * vs import math

"""
mutlak = abs(z)
print(math.cos(z))
"""

# imajiner sayıların abs'si büyüklüğüne eşittir
# liste a = b gibi bir iş yaparken değerleri değil sadece adresleri kopyalar
a = [1,2,3]

b = a  # bağımlı liste
# bağımsız liste
c = list(a)

#%% 

with open("answer.txt", "r") as ans:
    lines = ans.readlines()
    ans.close()

# çıkan stringi complex yapalım.


#%%










