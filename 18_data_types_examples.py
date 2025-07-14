# Python Built-in Data Types with examples

# Getting the type of a variable using type()
x = 5
print(type(x))  # <class 'int'>

# Different built-in data types in Python
x = "Hello World"                      # str
print(type(x))

x = 20                                 # int
print(type(x))

x = 20.5                               # float
print(type(x))

x = 1j                                 # complex
print(type(x))

x = ["apple", "banana", "cherry"]     # list
print(type(x))

x = ("apple", "banana", "cherry")     # tuple
print(type(x))

x = range(6)                           # range
print(type(x))

x = {"name" : "John", "age" : 36}     # dict
print(type(x))

x = {"apple", "banana", "cherry"}     # set
print(type(x))

x = frozenset({"apple", "banana", "cherry"})  # frozenset
print(type(x))

x = True                               # bool
print(type(x))

x = b"Hello"                           # bytes
print(type(x))

x = bytearray(5)                       # bytearray
print(type(x))

x = memoryview(bytes(5))              # memoryview
print(type(x))

x = None                               # NoneType
print(type(x))

# Setting specific data types using constructors
x = str("Hello World")
x = int(20)
x = float(20.5)
x = complex(1j)
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = range(6)
x = dict(name="John", age=36)
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))
x = bool(5)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))
