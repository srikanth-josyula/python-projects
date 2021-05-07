'''
Created on May 7, 2021

@author: Srikanth
'''

"""""
 finally - The finally keyword is used to create a block of code that will always be executed no matter the else block raises an error or not.
"""""
c = 0  
try: 
    d = 1 / c 
except ZeroDivisionError:
    print("division by zero custom error message")  # division by zero custom error message
except Exception as e:
    print("Generic Exception Occurred " + e)
except:
    print("Something else went wrong")
finally:
    print("The 'try except' is finished")  # Also Prints The 'try except' is finished
