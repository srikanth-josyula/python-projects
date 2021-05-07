'''
Created on May 7, 2021

@author: Srikanth
'''

"""""
Assert - It can be used for debugging the code. It tests a condition and returns True , if not, the program will raise an AssertionError.
         It is merely a Boolean expression that has a condition or expression checks if the condition returns true or false.
         If it is true, the program does not do anything, and it moves to the next line of code.
Syntax
        assert condition, error_message(optional)    
        
"""""

# Sample
x = "hello"
 
assert x == "goodbye", "x should be 'hello'"  # AssertionError: x should be 'hello'


# working example

def avg(scores):    
    assert len(scores) != 0,"The List is empty."     # AssertionError: The List is empty 
    return sum(scores)/len(scores)    
    
scores2 = [67,59,86,75,92]    
print("The Average of scores2:",avg(scores2))    
    
scores1 = []    
print("The Average of scores1:",avg(scores1))    