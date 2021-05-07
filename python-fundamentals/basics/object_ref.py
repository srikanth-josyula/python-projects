'''
Created on May 3, 2021

@author: Srikanth
'''
"""
Python provides the guaranteed that no two objects will have the same identifier. 
The built-in id() function, is used to identify the object identifier.

"""
a = 50  
b = a  

print(id(a))  
print(id(b))  

# Reassigned variable a  
a = 500  
print(id(a))  
