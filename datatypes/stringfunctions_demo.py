'''
Created on May 4, 2021

@author: Srikanth
'''
"""
1. The operator + is used to concatenate two strings as the operation "hello"+" python" returns "hello python".
2. The operator * is known as a repetition operator as the operation "Python" *2 returns 'Python Python'.
"""

# String concatenation 
str1 = "Srikanth"
str2 = "Josyula"

print("Concatenation of two strings is " + str1 + str2)

# String Repetition 
str3 = "Srikanth repeate"

print("Repetition of two strings is " + (str3 * 2))

# String Constructor 

print("Constructor of String data type " + str("Srikanth"))

# Type conversion from other data type to string 
int1 = 100
print("Data type before conversion")
print(type(int1))
str4 = str(100) # return <class 'int'>
print("Data type after conversion")
print(type(str4)) # return <class 'str'>
print("Type Conversion of Int to String " + str4)

# Index of Functionality in python
str5="Srikanth"
print("4th Char from the string is "+str5[4]) # returns 'a'

# Sub String Functionality in python
str5="Srikanth"
print("Sub-String of 0,4 is "+str5[0:4]) # returns 'Srik'


