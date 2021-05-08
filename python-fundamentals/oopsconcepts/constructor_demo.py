'''
Created on May 8, 2021

@author: Srikanth
'''
"""
A constructor is a special type of method (function) which is used to initialize the instance members of the class.
    Parameterized Constructor
    Non-parameterized Constructor

Constructor definition is executed when we create the object of this class. 
Constructors also verify that there are enough resources for the object to perform any start-up task.

In Python, the method the __init__() simulates the constructor of the class. This method is called when the class is instantiated. 
It accepts the self-keyword as a first argument which allows accessing the attributes or method of the class.

The constructor overloading is not allowed in Python.
"""

""""""""""
Constructor - parameterized
"""""""""""

class Person: 
        
    #  Constructor - parameterized  
    def __init__(self, name, id): 
        print("This is parametrized constructor")  
        print()
        self.id = id  
        self.name = name    
    
    def display (self): 
        print("ID: %d \nName: %s" % (self.id, self.name)) 
          
        
# Creating a p instance of Person class  
p1 = Person("John Walker", 101)    
p1.display()

""""""""""
Constructor - Non parameterized
"""""""""""
class Person2: 
        
     # Constructor - non parameterized  
    def __init__(self): 
        print()
        print("This is non parametrized constructor")  
        print()   
    
    def display (self, name, id): 
        print("ID: %d \nName: %s" % (id, name)) 
          
        
# Creating a p instance of Person class  
p2 = Person2()    
p2.display("Sam Wilson", 102)


""""""""""
Constructor - Default
"""""""""""

class Person3:  
    
    id = 103  
    name = "Steve Rogers"  
  
    def display(self):  
        print("ID: %d \nName: %s" % (self.id,self.name))  
  
p3 = Person3()  
print()
p3.display() 

""""""""""
Constructor - More than One Constructor in Single class
"""""""""""

class Person4:  
    def __init__(self):  
        print("The First Constructor")  
    def __init__(self):  
        print("The second contructor")  

#  The first method is not accessible by the p4 object. 
#  Internally, the object of the class will always call the last constructor if the class has multiple constructors.
p4 = Person4()  # prints The second contructor