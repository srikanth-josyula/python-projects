'''
Created on May 4, 2021

@author: Srikanth
'''

"""
1. Dictionary is an unordered set of a key-value pair of items. 
2. It is like an associative array or a hash table where each key stores a specific value. 
3. Key can hold any primitive data type, whereas value is an arbitrary Python object.

4. The items in the dictionary are separated with the comma (,) and enclosed in the curly braces {}.
"""

dictMap = {1:'a', 2:'b', 3:'c', 4:'d'};     
  
# Printing dictionary  
print (dictMap)  # prints {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
  
# Accesing value using keys  
print("1st entry is "+dictMap[1])   # prints 1st entry is a  
print("4th entry is "+ dictMap[4])  # prints 4th entry is d
  
print (dictMap.keys())      # prints dict_keys([1, 2, 3, 4])  
print (dictMap.values())    # prints dict_values(['a', 'b', 'c', 'd'])