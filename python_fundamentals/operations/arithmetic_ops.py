'''
Created on May 3, 2021

@author: Srikanth
'''


# Declaring a Addition function  
def add(): 
    # Defining local variables. They has scope only within a function  
    a = 20  
    b = 30  
    c = a + b  
    print("The sum is:", c)  

    
# Declaring a Sub function  
def sub(): 
    # Defining local variables. They has scope only within a function  
    a = 30  
    b = 20  
    c = a - b  
    print("The difference is:", c)  

  
# Declaring a multiplication  function  
def mul(): 
    # Defining local variables. They has scope only within a function  
    a = 30  
    b = 20  
    c = a * b  
    print("The multiplication is:", c) 

    
# Declaring a division  function  
def div(): 
    # Defining local variables. They has scope only within a function  
    a = 30  
    b = 20  
    c = a / b  
    print("The division is:", c) 

    
# In Python, % is the modulus operator. It is used to find the remainder when first operand is divided by the second  
def mod(): 
    # Defining local variables. They has scope only within a function  
    a = 30  
    b = 20  
    c = a % b  
    print("The modulus is:", c) 

#In Python, ** is the exponentiation operator. It is used to raise the first operand to power of second. 
def exp(): 
    # Defining local variables. They has scope only within a function  
    a = 2  
    b = 3  
    c = a ** b  
    print("The exponentiation of (2^3) is:", c) 
            
# In Python, // is used to conduct the floor division. It is used to find the floorof the quotient when first operand is divided by the second.. 
def floordiv(): 
    # Defining local variables. They has scope only within a function  
    a = 3  
    b = 2  
    c = a // b  
    print("The floor division is:", c)             
            
# Calling a function  
add()  
sub()  
mul()  
div()
mod()
exp()
floordiv()