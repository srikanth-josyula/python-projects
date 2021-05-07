'''
Created on May 4, 2021

@author: Srikanth
'''
a = 1  
print("The type of a", type(a))  # <class 'int'>
print("a is a int number", isinstance(a,int)) # return boolean True

b = 40.5  
print("The type of b", type(b))  # <class 'float'>
print("b is a float number", isinstance(b,float)) # return boolean True 

c = 1+3j  
print("The type of c", type(c))  # <class 'complex'>
print("c is a complex number", isinstance(c,complex)) # return boolean True

d = "Sri"  
print("The type of d", type(d))  # <class 'str'>
print("d is a string", isinstance(d,str)) # return boolean True
print("d is a int", isinstance(d,int)) # return boolean True