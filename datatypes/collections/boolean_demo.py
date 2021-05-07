'''
Created on May 7, 2021

@author: Srikanth
'''
"""
Boolean type provides two built-in values, True and False. 
These values are used to determine the given statement true or false. 
It denotes by the class bool. True can be represented by any non-zero value or 'T' whereas false can be represented by the 0 or 'F'. 
"""

# Python program to check the boolean type  
print(type(True))       # prints <class 'bool'> Capital T
print(type(False))      # prints <class 'bool'> Capital F

#print(false)            # NameError: name 'false' is not defined

print(bool(1))  #True
print(bool(0))  #False

x = True
y = False
 
print(x)    #True
print(y)    #False