# Learning Python
Learning basic of python like data type, list, dictionary, function, class, turtle, interface.

## Note:
Python is a case-sensitive language which is heavily rely on indentation or spacing.

---
## Examples
## Comments
```python
# This is a one-line Python comment - code blocks are so useful!
"""This type of comment is used to document the purpose of functions and classes."""
```

## Declaration/Initialization
```python
# Remember values, not variables, have data types.
# A variable can be reassigned to contain a different data type.
answer = 42
answer = "The answer is 42."
```

## Data Types
```python
boolean = True
number = 1.1
string = "Strings can be declared with single or double quotes."
list = ["Lists can have", 1, 2, 3, 4, "or more types together!"]
tuple = ("Tuples", "can have", "more than", 2, "elements!")
dictionary = {'one': 1, 'two': 2, 'three': 3}
variable_with_zero_data = None
```

#### NOTE: 
Both lists and tuples are sequence data types that can store a collection of items. <br />
**Difference:** <br />
**lists** ---> **mutable** whereas <br />
**tuple** ---> *immutable*.<br />
A mutable data type means that a python object of this type can be modified.


## Simple Logging
```python
print "Printed!"
```

## Conditionals
```python
cake = "okay"
if cake == "delicious":
    print("Yes please!")   
elif cake == "okay":
    print("I'll have a small piece.")   
else:
    print("No, thank you.")
```

## Loops
```python
for item in list:
    print item

while (total < max_val):
    total += values[i]
    i += 2
```

## Range
There are three ways you can call range() :
* range(stop) takes one argument.
* range(start, stop) takes two arguments.
* range(start, stop, step) takes three arguments.
```
for i in range(2, 10, 2):
    print(i)
print('Goodbye!')
```

## Functions
```python
def divide(dividend, divisor):
    quotient = dividend / divisor
    remainder = dividend % divisor
    return quotient, remainder

def calculate_stuff(x, y):
    (q, r) = divide(x,y)
    print q, r
```

## Classes
```python
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def birthday(self):
        self.age += 1
```
