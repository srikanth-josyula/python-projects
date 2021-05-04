'''
Created on May 4, 2021

@author: Srikanth
'''
"""
These are number types. They are created when a number is assigned to a variable.
1. int holds signed integers of non-limited length.
2. float holds floating precision numbers and they are accurate upto 15 decimal places.
3. complex number contains the real and imaginary part.
"""
a = 5  
print("The type of a", type(a))  # <class 'int'>
  
b = 40.5  
print("The type of b", type(b))  # <class 'float'>
  
c = 1+3j  
print("The type of c", type(c))  # <class 'complex'>
print(" c is a complex number", isinstance(1+3j,complex)) 