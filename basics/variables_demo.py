'''
Created on May 3, 2021

@author: Srikanth
'''

"""
 Python identifiers refer to a name used to identify a variable, function, module, class, module or other objects. 
 There are few rules to follow while naming the Python Variable.

    A variable name must start with either an English letter or underscore (_).
    A variable name cannot start with the number.
    Special characters are not allowed in the variable name.
    The variable's name is case sensitive.
    All the characters except the first character may be an alphabet of lower-case(a-z), upper-case (A-Z), underscore, or digit (0-9).
    Identifier name must not contain any white-space, or special character (!, @, #, %, ^, &, *).
    Identifier name must not be similar to any keyword defined in the language.
    Identifier names are case sensitive; for example, my name, and MyName is not the same.

    Examples of valid identifiers: a123, _n, n_9, etc.
    Examples of invalid identifiers: 1a, n%4, n 9, etc.
"""

'''
Single Assignment
String types 
'''
singleQuotesString = 'String with Single Quotes'
doubleQuotesString = "String with Single Quotes"
 
print(singleQuotesString)   # prints String with Single Quotes
print(doubleQuotesString)   # prints String with Single Quotes
print()

'''
Chained Assignment 
'''
i = j = k = 20
 
print(i)            # prints 20
print(j)            # prints 20
print(k)            # prints 20
print()

'''
Multiple assignments in single line
'''
x, y, z = "A", "B", 100
 
print(x)    # prints A
print(y)    # prints B
print(z)    # prints 100
print()

'''
Multi Type Variable Declaration
'''
_integer = 100 
_float = 80.50
_string = "test"

print(_string, _integer, _float)

# check the type of it using the Python built-in type() function.
print()
print("Using type() function to return the variable type")
print()

print(type(_integer))
print(type(_string))
print(type(_float))
