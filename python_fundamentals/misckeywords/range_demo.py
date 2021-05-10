'''
Created on May 7, 2021

@author: Srikanth
'''
"""""
The range () function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), 
and stops before a specified number.

syntax range(start, stop, step)
start    Optional. An integer number specifying at which position to start. Default is 0
stop    Required. An integer number specifying at which position to stop (not included).
step    Optional. An integer number specifying the incrementation. Default is 1

"""""
x = range(6)
for n in x:
    print(n) # prints 0 1 2 3 4 5 

for y in range(1, 9):
    print(y) # prints 1 2 3 4 5 6 7 8
    
    
p = range(3, 10, 2)
for n in p:
    print(n) # prints 3 5 7 9