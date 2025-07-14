# Local variable vs Global variable with the same name

# Global variable
x = "a modern upazila of Chattogram"

def myfunc():
    # Local variable with same name 'x'
    x = "fantastic place to live and explore"
    print("Raozan is " + x)  # Uses local x

# Call the function
myfunc()

# Outside the function, global x is used
print("Raozan is " + x)