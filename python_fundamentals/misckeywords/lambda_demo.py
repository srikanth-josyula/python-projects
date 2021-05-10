'''
Created on May 8, 2021

@author: Srikanth
'''

"""
lambda function is a small anonymous function.
        lambda function can take any number of arguments, but can only have one expression.

Syntax - lambda arguments : expression
"""

x = lambda a : a + 10
print(x(5))     # prints 15

x = lambda a, b : a * b
print(x(5, 6))  # prints 30

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))   # prints 13


# using a function 
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))    # prints 22

