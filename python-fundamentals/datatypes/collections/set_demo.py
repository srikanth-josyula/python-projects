'''
Created on May 4, 2021

@author: Srikanth
'''
"""
1. Python Set is the unordered collection of the data type. 
2. It is iterable, mutable(can modify after creation), and has unique elements. 
3. In set, the order of the elements is undefined; it may return the changed sequence of the element. 
4. The set is created by using a built-in function set(), or a sequence of elements is passed in the curly braces and separated by the comma. 
5. It can contain various types of values.
6. Unlike list, there is no index for set elements. It means we can only loop through the elements of the set
"""

# Creating Empty set  
set1 = set()  
  
set2 = {'srikanth', 2, 3, 4, 5.3, 6, 7, 8, 9, 'josyula'} 

print(set1)           # prints set()
print(set2)           # prints {2, 3, 4, 5.3, 6, 7, 8, 9, 'josyula', 'srikanth'} not ordered
print(type(set1))     # prints <class 'set'>
print(type(set2))     # prints <class 'set'>


# Adding element to the set    
set2.add(10)          # prints {2, 'srikanth', 3, 4, 5.3, 6, 7, 8, 9, 10, 'josyula'}
print(set2)  
  
#Removing element from the set  
set2.remove(2)  
print(set2)           # prints {'srikanth', 3, 4, 5.3, 6, 7, 8, 9, 10, 'josyula'}