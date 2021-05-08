'''
Created on May 8, 2021

@author: Srikanth
'''

"""
Inheritance is an important aspect of the object-oriented paradigm.
Inheritance provides code reusability to the program because we can use an existing class to create a new class instead of creating it from scratch
In inheritance, the child class acquires the properties and can access all the data members and functions defined in the parent class.
A child class can also provide its specific implementation to the functions of the parent class. 
In python, a derived class can inherit base class by just mentioning the base in the bracket after the derived class name.

syntax
    Class Base1:
        Body of the class

    Class Base2:
        Body of the class

    Class Derived(Base1, Base2):
        Body of the class
"""


########################
# MULTIPlE INHERITENCE #
########################

# University Details (Level 1)    
class University:

    def universityDetails(self, clgname):
        print("    University Name: %s" % (clgname))  
        
        
# Person Details (Level 2 University has many Persons)
class Person:

    def personDetails(self, fname, lname):
        print("    Person FirstName: %s \n    Person LastName: %s" % (fname, lname))
  

# Create a class named Student, which will inherit the properties and methods from the Person class
class Student(Person,University): 

    def studentDetails(self, courseid, coursename):
        print("    Course ID: %d \n    Course Name: %s" % (courseid, coursename)) 

# Use the University class to create an object, and then execute the  method:  
print("Printing only University Details")
u = University()
print("University Details are :")
u.universityDetails("MIT")
print()

# Use the Person class to create an object, and then execute the  method:  
print("Printing only Parent Details along with Univeristy")
x = Person()
print("Person Details are :")
x.personDetails("John", "Doe")
print()

# Use the Stident class to create an object, and then execute the  method:  
print("Printing only Parent Details along with Univeristy")
s = Student()
print("Student Details are :")
s.personDetails("John", "Doe")
s.studentDetails(123, "Python Course")
s.universityDetails("MIT")


"""
OUTPUT :
    Printing only University Details
    University Details are :
        University Name: MIT
    
    Printing only Parent Details along with Univeristy
    Person Details are :
        Person FirstName: John 
        Person LastName: Doe
    
    Printing only Parent Details along with Univeristy
    Student Details are :
        Person FirstName: John 
        Person LastName: Doe
        Course ID: 123 
        Course Name: Python Course
        University Name: MIT
"""
