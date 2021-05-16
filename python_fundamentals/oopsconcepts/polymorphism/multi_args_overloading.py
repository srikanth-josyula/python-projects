


# Function to take multiple arguments
def product(*args):
    ans = 1
    # Traverse through the arguments
    for x in args:
  
        # This will do addition if the 
        # arguments are int. Or concatenation 
        # if the arguments are str
        ans = ans * x
  
    print(ans)
    
product(4, 5) # 20
product(4, 5, 5) # 100