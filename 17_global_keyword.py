# Using global keyword to create or modify global variables inside a function

# Example 1: Creating global variable inside a function
def myfunc1():
    global x
    x = " fantastic place to live and explore"

myfunc1()
print("Raozan is" + x)  # Output: Raozan is fantastic place to live and explore

# Example 2: Changing an existing global variable from inside a function
x = " a modern upazila of Chattogram."

def myfunc2():
    global x
    x = "fantastic place to live and explore"

myfunc2()
print("Raozan is " + x)  # Output: Raozan is fantastic place to live and explore
