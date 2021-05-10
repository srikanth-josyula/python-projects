'''
Created on May 8, 2021

@author: Srikanth
'''

"""
A class needs to be instantiated if we want to use the class attributes in another class or method. 
        A class can be instantiated by calling the class using the class name.
        The syntax to create the instance of the class is given below.

        <object-name> = <class-name>(<arguments>)    
            
The self-parameter refers to the current instance of the class and accesses the class variables. 
        We can use anything instead of self, but it must be the first parameter of any function which belongs to the class.

"""

class Person:    
    id = 10   
    name = "john walker"    
    
    def display (self):    
        print("ID: %d \nName: %s"%(self.id,self.name))     
        
# Creating a p instance of Person class  
p = Person()    
p.display()    


# Deleting the property of object  
del p.id  

# Deleting the object itself  
del p 
 
p.display()  # throws AttributeError: id,  because we have deleted the object