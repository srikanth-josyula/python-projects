'''
Created on May 4, 2021

@author: Srikanth
'''
"""
1. A tuple is similar to the list in many ways. Like lists, 
2. tuples also contain the collection of the items of different data types. 
3. The items of the tuple are separated with a comma (,) and enclosed in parentheses ().
4. A tuple is a read-only data structure as we can't modify the size and value of the items of a tuple.
"""

tup1  = (1, "one", 2, "two")  
  
# Checking type of tup  
print (type(tup1))    # return <class 'tuple'>
  
#Printing the tuple  
print (tup1)  # return (1, 'one', 2, 'two')
  
# Tuple slicing  
print (tup1[1:])   # return ('one', 2, 'two') 
print (tup1[0:1])  # return (1,)
  
# Tuple concatenation using + operator  
print (tup1 + tup1)     # returns (1, 'one', 2, 'two', 1, 'one', 2, 'two')
  
# Tuple repatation using * operator  
print (tup1 * 3)    # returns (1, 'one', 2, 'two', 1, 'one', 2, 'two', 1, 'one', 2, 'two') 
  
# Adding value to tup. It will throw an error.  
tup1[2] = "hi"  # TypeError: 'tuple' object does not support item assignment