'''
Created on May 8, 2021

@author: Srikanth
'''

"""""
Python is an object oriented programming language. Almost everything in Python is an object, with its properties and methods.

Class -  A Class is like an object constructor, or a "blueprint" for creating objects.
        The class can be defined as a collection of objects. It is a logical entity that has some specific attributes and methods. 
        For example: if you have an employee class, then it should contain an attribute and method, i.e. an email id, name, age, salary, etc.

Object - The object is an entity that has state and behavior. 
         When we define a class, it needs to create an object to allocate the memory.
         
The __init__() Function - Its a constrctor in java
                          All classes have a function called __init__(), which is always executed when the class is being initiated
                          The __init__() function is called automatically every time the class is being used to create a new object.
                          Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created
                          The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
                          It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class
"""""


# class definition
class Person:
    
    def __init__(self, name, age, salary, emailId):
        self.name = name
        self.age = age
        self.salary = salary
        self.emailId = emailId

    def myfunc(self):
        print("Hello my name is " + self.name)

        
# Object definition
p2 = Person("Walker", 36, 42000, 'walker@sample.com')
print(p2.emailId)

p2.myfunc()
