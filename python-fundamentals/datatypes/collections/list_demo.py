'''
Created on May 4, 2021

@author: Srikanth
'''
"""
1. In Python, list is an ordered sequence of some data written using square brackets([ ]) and commas(,). 
2. A list can contain data of different types.
3. We can use slice [:] operators to access the data of the list. The concatenation operator (+) and repetition operator (*) works with the list in the same way as they were working with the strings.
"""

list1  = [1, "one", 2, "two"]
   
#Checking type of given list  
print(type(list1))   # returns <class 'list'>
  
#Printing the list1  
print (list1)  # [1, 'one', 2, 'two']
  
# List slicing  
print (list1[3:])  # printing 3 value from list ['two']
  
# List slicing  
print (list1[0:2]) # retuns 0-2 index elements from list [1, 'one']  
  
# List Concatenation using + operator  
print (list1 + list1)  # returns [1, 'one', 2, 'two', 1, 'one', 2, 'two']
  
# List repetation using * operator  
print (list1 * 3)  # returns [1, 'one', 2, 'two', 1, 'one', 2, 'two', 1, 'one', 2, 'two']

list1[0] = 0 
print(list1) # returns [0, 'one', 2, 'two'], we can modify in list but not in tuple