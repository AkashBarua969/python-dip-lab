# Demonstrating type conversion in Python

# Original values
x = 1        # int
y = 2.8      # float
z = 1j       # complex

# Convert from int to float
a = float(x)

# Convert from float to int
b = int(y)

# Convert from int to complex
c = complex(x)

# Display converted values
print(a)           # Output: 1.0
print(b)           # Output: 2
print(c)           # Output: (1+0j)

# Show types of converted values
print(type(a))     # <class 'float'>
print(type(b))     # <class 'int'>
print(type(c))     # <class 'complex'>

# Note: You cannot convert complex numbers into another number type (int/float)
