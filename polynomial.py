# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 18:30:12 2022

@author: Asus
https://www.programiz.com/python-programming/operator-overloading
"""

import numpy as np

         
class Polynome:

    def     __init__(self,coeff_,a_=0.0,root_=False):
# root_ is False then coeff_ contains coefficient of the polynomial
        #example: coeff=[1.,2.,4.] is associated with polynomial 1.*x+2.*x^2+4.*x^3
        #if coeff is a float then the associated polynomial is polynomial of
        #degree 0 p=Polynome(5.) will return a polynomial of degree 0 whose value is 
        #equal to 5. everywhere
       if(root_==False): 
           if (type(coeff_)==float):
               self.coeff=np.array([coeff_])#attribute coeff defined,polynomial of degree 0
           else:
             if (type(coeff_)==Polynome):# will make a copy of the argument
                 self.coeff=np.array(coeff_.coeff)#attribute coeff defined
             else:
                 self.coeff=np.array(coeff_)#attribute coeff defined
           self.degree=self.coeff.size-1
           self.rootknown=False
       else:# root_ is true then array coeff_ (first argument) contains the 
           # roots of the polynomial it will proceed to multiplication
           #a_*(x-x0)*(x-x1)*(x-x2).... in order to find coefficient of x^0,x^1
           #x^2 extra.. (see line below) a_ is coefficient of x^(highest degree)
           self.Roots=np.array(coeff_)
           self.a=a_
           p1=Polynome([-self.Roots[0],1.])
           for k in range(1,self.Roots.size):
               p2=Polynome([-self.Roots[k],1.])
               p1=p2*p1
           self.coeff=np.array(p1.coeff*self.a)    
               
         
        
    def value(self,x):
        if(type(x)==float):
            current=1.0
            s=0.0
            for k in range(self.coeff.size):
                s+=self.coeff[k]*current
                current*=x
            return s
        else:
            current=np.ones(x.size)
            s=np.zeros(x.size)
            for k in range(self.degree+1):
                s+=self.coeff[k]*current
                current*=x
            return s
    def  __add__(self, other):
        max_=max(self.degree+1,other.degree+1)
        min_=min(self.degree+1,other.degree+1)
        res=Polynome(np.zeros(max_))
        res.coeff[:min_]=self.coeff[:min_]+other.coeff[:min_]
        if (max_==self.degree+1):#this polynom has higher degree than the other
           res.coeff[other.degree+1:] =self.coeff[other.degree+1:]#copy the lement of the
               #larger polynom to te result
        else:
            res.coeff[self.degree+1:]=other.coeff[self.degree+1:]
            
                   
        return res
    def __mul__(self,other):
        res=Polynome(np.zeros(self.degree+other.degree+1,dtype=float))
        for k in range(res.degree+1):
            s=0
            for kk in range(k+1):
                if((kk<self.coeff.size) and (k-kk<other.coeff.size) ):
                    s+=self.coeff[kk]*other.coeff[k-kk]
            res.coeff[k]=s
        return res
    def Print(self):
        str_=str('')
        for k in range(self.coeff.size):
            if (self.coeff[k]>0.):current='+'+str(self.coeff[k])
            else:
              current=str(self.coeff[k]) 
            x=str('')  
            if(k>0):
                x='x^'+str(k)
            str_=str_+current+x
            
        str_=str_+'\n'
        #print(self.coeff)
        print(str_)
    def IntegrateValue(self,a,b) : 
        s=0.
        for k in range(self.coeff.size):
            s=s+self.coeff[k]*(b**(k+1)-a**(k+1))/(k+1.)
        return s
    def Integral(self):
        result=Polynome(np.zeros(self.coeff.size+1,dtype=float))
        for k in range (1,self.coeff.size+1):
            result.coeff[k]=self.coeff[k-1]/k
        return result
    def Derivative(self):
        result=Polynome(np.zeros(self.coeff.size-1,dtype=float))
        for k in range(result.degree+1):
            result.coeff[k]=self.coeff[k+1]*(k+1)
        return result
            
p=Polynome([1.,1.,2.])  #p(x)=1.+1*x+2.*x^2
print(p.value(2.),1.+2.+2*2**2.,'p value at 2')  
print(p.value(np.ones(3)),'value of the polynomial at [1.,1.,1.]')   
pc=Polynome(2.)#pc(x)=2. (polynomial of degree 0)
print(pc.value(3.),' poly of degree 0 alway equal to 2')
p_sum=p+pc
print(p_sum.value(2.),'p_sum value at 2')
p_sum2=pc+p
print(p_sum2.value(2.),'p_sum2 value at 2')
p3=Polynome(p)#p3 is independent copy of p (lying at a different memory location)
p4=p
p4.coeff[0]=1000.
print(p.value(0.),' p affected by assignment p4=p and p4.coeff[0]=1000')

p1=Polynome([1.,1.,1])
p2=Polynome([1.,-1.])
p12=p1*p2
p12.Print()
p12=p2*p1
p12.Print()
print(p1.IntegrateValue(1.,2.))
pz=p1.Integral()
pz.Print()
pzz=p1.Derivative()
pzz.Print()
Roots=np.ones(3,dtype=float)
mul=Polynome(Roots,1.,True)
mul.Print()
