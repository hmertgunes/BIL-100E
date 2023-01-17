"""
Created on Tue Sep 20 23:09:55 2022

@author: mert
"""

# import the library in order to calculate sin values of an array 
import numpy as np



# writing function
def random_sin_write():
    
    sin_list = np.sin(np.random.randint(1,360,size=(20,1)))
    
    with open("practice.txt", "w") as ans:
        
        for idx, value in enumerate(sin_list):
            ans.write(str(idx+1) +"-" + str(value) + "\n")
        
        ans.close()

    return "Writing Process Done!"

    

# reading function
def random_sin_read():
    
    with open("practice.txt", "r") as ans:
        
        lines = ans.readlines()
        ans.close()

    for i in lines:
        print(i)
                    
    return "Reading Process Done!" 



# Export as array again
def array_again():
    
    with open("practice.txt", "r") as ans:
        
        lines = ans.readlines()
        ans.close()
        
        final_array = []

        for i in lines:
            final_array.append(float(i[i.find("[")+1 : i.find("]")]))
            
        final_array = np.array(final_array).reshape((20,1))
        
    return final_array
        
        
        
        
        
        
        
        