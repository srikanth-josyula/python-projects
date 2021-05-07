'''
Created on May 7, 2021

@author: Srikanth
'''
"""
The frozen sets are the immutable form of the normal sets. It means we cannot remove or add any item into the frozen set
"""

frozenSet1 = frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9}) 
frozenSet2 = frozenset({'srikanth', 2, 3, 4, 5.3, 6, 7, 8, 9, 'josyula'})

 
print(frozenSet1)       #prints frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
print(frozenSet2)       #prints frozenset({'josyula', 2, 3, 4, 5.3, 6, 7, 8, 9, 'srikanth'}) not in order

# Adding element to the set    
frozenSet1.add(10)          # AttributeError: 'frozenset' object has no attribute 'add'
print(frozenSet1)  
  
#Removing element from the set  
frozenSet1.remove(2)  
print(frozenSet1)           # AttributeError: 'frozenset' object has no attribute 'remove'