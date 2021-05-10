'''
Created on May 7, 2021

@author: Srikanth
'''

"""""
nonlocal -  It is used to declare that a variable is not local. 
            It is used to work with variables inside nested functions, where the variable should not belong to the inner function.
            
nonlocal vs global ?
"""""
def myfunc1():
    x = "John"
    def myfunc2():
        nonlocal x
        x = "hello"
    myfunc2()
    return x
 
print(myfunc1())