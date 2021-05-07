'''
Created on May 7, 2021

@author: Srikanth
'''

# If - It is used to represent the conditional statement. The execution of a particular block is decided by if statement.

x = 5

if x > 3:
    print("it is true")
    
# else - The else statement is used with the if statement. 
#        When if statement returns false, then else block is executed
n = 11  

if(n%2 == 0):  
    print("Even")  
else:  
    print("odd")  
    
# elif - Else If, It is used in conditional statements and is short for else if.
i = 5
 
if i > 0:
    print("Positive")
elif i == 0:
    print("ZERO")
else:
    print("Negative")
    
# short IF 
a = 20
b = 10
if a > b: print("a is greater than b")

# Short Hand If ... Else
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# Nested If
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")