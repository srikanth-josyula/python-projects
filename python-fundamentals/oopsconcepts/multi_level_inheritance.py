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
        class class1:  
            <class-suite>   
        class class2(class1):  
            <class suite>  
        class class3(class2):  
            <class suite> 
"""

###########################
# MULTI LEVEL INHERITENCE #
###########################

# University Details (Level 1)    
class University:
    def __init__(self, clgname):
        self.clgname = clgname

    def universityDetails(self):
        print("    University Name: %s" % (self.clgname))  
        
        
# Person Details (Level 2 University has many Persons)
class Person(University):
    
    def __init__(self, fname, lname, clgname):
        super().__init__(clgname)  # can also be super.__init__(self, fname, lname) if there is no university Details
        self.firstname = fname
        self.lastname = lname

    def personDetails(self):
        print("    Person FirstName: %s \n    Person LastName: %s" % (self.firstname, self.lastname))
  

# Create a class named Student, which will inherit the properties and methods from the Person class
class Student(Person): # same as in java Student extends Person here In Python Student(Person)
    
    # Add the __init__() function to the Student class:
    def __init__(self,fname, lname, courseid, coursename, clgname):
        
        # super() function that will make the child class inherit all the methods and properties from its parent
        super().__init__(fname, lname,clgname)  # can also be super.__init__(self, fname, lname) if there is no university Details
        self.courseid = courseid
        self.coursename = coursename
        
    def studentDetails(self):
        print("    Course ID: %d \n    Course Name: %s" % (self.courseid, self.coursename)) 


# Use the University class to create an object, and then execute the  method:  
print("Printing only University Details")
x = University("MIT")
print("University Details are :")
x.universityDetails()
print()

# Use the Person class to create an object, and then execute the printname method:  
print("Printing only Parent Details along with Univeristy")
x = Person("John", "Doe", "MIT")
print("Person Details are :")
x.personDetails()
x.universityDetails()
print()

# Use the Student class to create an object, and then execute the printname method
print("Printing Parent Details along Child Details")
s = Student("Mike", "Olsen", 123, "Python Course", "MIT")
print("Course Details are :")
s.personDetails()
s.universityDetails()
s.studentDetails()



"""
OUTPUT :
    Printing only University Details
    University Details are :
        University Name: MIT
    
    Printing only Parent Details along with Univeristy
    Person Details are :
        Person FirstName: John 
        Person LastName: Doe
        University Name: MIT
    
    Printing Parent Details along Child Details
    Course Details are :
        Person FirstName: Mike 
        Person LastName: Olsen
        University Name: MIT
        Course ID: 123 
        Course Name: Python Course
"""

