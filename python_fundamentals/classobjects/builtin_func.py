'''
Created on May 8, 2021

@author: Srikanth
'''
"""
The built-in functions defined in the class are described in the following table

1    getattr(obj,name,default)    It is used to access the attribute of the object.
2    setattr(obj, name,value)    It is used to set a particular value to the specific attribute of an object.
3    delattr(obj, name)    It is used to delete a specific attribute.
4    hasattr(obj, name)    It returns true if the object contains some specific attribute.

Along with the other attributes, a Python class also contains some built-in class attributes which provide information about the class

1    __dict__    It provides the dictionary containing the information about the class namespace.
2    __doc__    It contains a string which has the class documentation
3    __name__    It is used to access the class name.
4    __module__    It is used to access the module in which, this class is defined.
5    __bases__    It contains a tuple including all base classes.
"""

class Person:  
    def __init__(self, name, id, age):  
        self.name = name  
        self.id = id  
        self.age = age  
        
# creates the object of the class Student  
p = Person("John", 101, 26)

# reset the value of attribute age to 23  
setattr(p, "age", 23)    

# prints the modified value of age  
print(getattr(p, 'age'))  

# prints true if the person contains the attribute with name id  
print(hasattr(p, 'id'))  

# deletes the attribute age  
delattr(p, 'age')    
print(p.age)    # AttributeError: 'Person' object has no attribute 'age' # this will give an error since the attribute age has been deleted  

print(p.__doc__)    # prints None
print(p.__dict__)   # prints {'name': 'John', 'id': 101, 'age': 23} 
print(p.__module__) # prints __main__ 