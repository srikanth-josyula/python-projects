'''
Created on May 10, 2021

@author: Srikanth
'''
"""
The most Pythonic way to import classes from other directories is by using packages. 

"""
from python_fundamentals.oopsconcepts.abstraction.abs_demo import Polygon

class Triangle(Polygon):
    def sides(self):   
        return("3 sides")   
  
class Pentagon(Polygon):   
    def sides(self):   
        return("5 sides")   
  
class Hexagon(Polygon):   
    def sides(self):   
        return("6 sides")   
  
class square(Polygon):   
    def sides(self):   
        return("4 sides")   
  
# Driver code   

p = Triangle("Triangle")
print("Name of the Polygon   : %s" %(p.polygon_details()))
print("Total Number of Sides : %s" %(p.sides()))
