
'''
Created on May 7, 2021

@author: Srikanth
'''
"""""""""""""""""""""
FOR Loop Operations
"""""""""""""""""""""
# For - It is used to create a for loop. A for loop can be used to iterate through a sequence, like a list, tuple, etc.

my_list = ["srikanth", "sri", "josyula"]

for x in my_list:
    print(x)
    
    
# Looping Through a String

for x in "srikanth":
    print(x)
    
# break - With the break statement we can stop the loop before it has looped through all the items

for x in my_list:
    print(x)
    if x == "srikanth": 
        break
    
"""""""""""""""""""""
WHILE Loop Operations
"""""""""""""""""""""  
# while - It is used to create a while loop. The loop continues until the conditional statement is false.  

x = 0
 
while x < 9:
    print(x)
    x = x + 1

# The break Statement
i = 1

while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
    
# Else in While loop

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")