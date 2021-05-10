'''
Created on May 10, 2021

@author: Srikanth
'''
"""
Abstraction is used to hide the internal functionality of the function from the users. 
The users only interact with the basic implementation of the function, but inner working is hidden. 
User is familiar with that "what function does" but they don't know "how it does."

In Python, an abstraction is used to hide the irrelevant data/class in order to reduce the complexity. 
It also enhances the application efficiency

Syntax
    from abc import ABC  
    class ClassName(ABC): 
    
import - It is used to import modules. (import datetime)
from - It is used to import only a specified section from a module. (from datetime import time)

Abstract Base Classes - An abstract base class is the common application program of the interface for a set of subclasses. 
                        It can be used by the third-party, which will provide the implementations such as with plugins. 
                        It is also beneficial when we work with the large code-base hard to remember all the classes.
                        
                        
Unlike the other high-level language, Python doesn't provide the abstract class itself. We need to import the abc module, 
which provides the base for defining Abstract Base classes (ABC). The ABC works by decorating methods of the base class as abstract. 
It registers concrete classes as the implementation of the abstract base. 
We use the @abstractmethod decorator to define an abstract method or if we don't provide the definition to the method, 
it automatically becomes the abstract method. 
"""
class Polygon:
    
    def __init__(self, name):
        self.name = name
 
    def polygon_details(self):    
        return (self.name)
    
    def sides(self):   
        pass 
    
    
    
    