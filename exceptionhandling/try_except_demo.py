'''
Created on May 7, 2021

@author: Srikanth
'''
"""
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.

This is equivalent to try-catch as of JAVA 
"""

#  try, except - The try-except is used to handle the exceptions. The exceptions are run-time errors. 

a = 0  
try:  
    b = 1/a  
except Exception as e:  
    print(e)     

# try with multi except 
c = 0  
try:  
    d = 1/c 
except ZeroDivisionError:
    print("division by zero custom error message")  # division by zero custom error message
except Exception as e:
    print("Generic Exception Occurred "+e)
except:
    print("Something else went wrong")
    
# try with multi except and else
e = 1  
try:  
    f = 1/e 
except ZeroDivisionError:
    print("division by zero custom error message")  
except Exception as e:
    print("Generic Exception Occurred "+e)
except:
    print("Something else went wrong")
else:
    print("All Good !!")    # prints All Good !!