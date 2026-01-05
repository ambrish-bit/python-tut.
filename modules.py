# <> Modules in python
'''A module is a file that contains Python code (variables, functions, classes).
It helps to organize large programs into small, manageable parts.

👉 Any .py file is a module.
For example: math.py, game.py, student.py

You can reuse the code from a module using import.'''
# in simple words module is use for add the external code which is already defined

# there are 4 types of module in python
# 1. math
import math

a = math.factorial(5)
print(a)
b = math.floor(7.6)
print(b)
c = math.sqrt(196)
print(c)


# 2. keyword
import keyword
print(keyword.kwlist)


# 3. random
import random
print(random.randint(1,100))


# 4. datetime
import datetime
print(datetime.datetime.now())


# if we want to know how many modules are there in the python
# then we have to write help('module')
help('modules')