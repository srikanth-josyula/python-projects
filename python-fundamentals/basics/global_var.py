'''
Created on May 3, 2021

@author: Srikanth
'''

x = 10  # global variable

'''
Global variables can be used throughout the program, and its scope is in the entire program. 
We can use global variables inside or outside the function.

A variable declared outside the function is the global variable by default. 
Python provides the global keyword to use global variable inside the function. 
If we don't use the global keyword, the function treats it as a local variable.
''' 


def myfunc():
    
    x = 20  # local variable chnage global varibale
    print("x is inside " + str(x))  # prints x is 20
    
    y = 10  # local variable
    print("Sum of x and y inside = " + str(x))  # prints Sum of x and y = 30
    
    global z 
    z = 10  # global variable created inside function
    print("z is inside " + str(z))  # prints x is 20


myfunc() 

print("x is outside " + str(x))  # prints x is 10 as Local variables are bounded within function scope
print("Sum of x and y = " + str(x + y))  # NameError: name 'y' is not defined
print("z is outside " + str(z)) 

