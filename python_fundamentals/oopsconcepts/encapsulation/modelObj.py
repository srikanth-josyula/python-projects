'''
Created on May 10, 2021

@author: Srikanth
'''
class Model:
    def __init__(self, value=0):
        
        # private value
        self.__value = value

    # getter method
    def get_value(self):
        return self.__value

    # setter method
    def set_value(self, a):
        self.__value = a

class Main:
    
    model_obj = Model()
    # Before using setter
    print(model_obj.get_value())

    # After using setter
    model_obj.set_value(2021)
    print(model_obj.get_value())