'''
Created on May 10, 2021

@author: Srikanth
'''
"""
Protected members - Protected members are those members of the class that cannot be accessed outside the class but can be accessed from within the class and its subclasses. 
                    To accomplish this in Python, just follow the convention by prefixing the name of the member by a single underscore '''_'''.
                    
Private members   - Private members are similar to protected members, the difference is that the class members declared private should neither be accessed outside the class 
                    nor by any base class. In Python, there is no existence of Private instance variables that cannot be accessed except inside a class. 
                    However, to define a private member prefix the member name with double underscore '''__'''.
"""
#Creating a base class

class Base:
    def __init__(self):
         
        # public member
        self.a = "public"
        
        # Protected member
        self._b = "protected"
        
        # private member
        self.__c = "private"
 
# Creating a derived class   
class Derived(Base):
    
    def __init__(self):
         
        # Calling constructor of Base class
        Base.__init__(self)
        
obj1 = Derived()
obj2 = Base()
 
# Calling members Outside class
print("Calling member of Base class from Derived Class : "+obj1.a)
print("Calling member of Base class from Outside Class : "+obj2.a)
print()
print("Calling member of Base class from Derived Class : "+obj1._b)
print("Calling member of Base class from Outside Class : "+obj2._b)
print()
print("Calling member of Base class from Derived Class : "+obj1.__c) # prints AttributeError: 'Base' object has no attribute '__c'
print("Calling member of Base class from Outside Class : "+obj2.__c) # prints AttributeError: 'Base' object has no attribute '__c'