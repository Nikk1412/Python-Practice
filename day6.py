# Day 6

## Reference Counting
# Python internally counts how many references point to an object.

x = 257
y =x
z= x


import sys

x = 257
y = x
z = x

print("Value:", x)
print("refcount of 257:", sys.getrefcount(257)) ## refcount of 10 : 6

'''
getrefcount(1) will be at least 2 extra references because:

Python creates internal temporary references

Passing the object into the function adds one more

'''


# Assignment 2 :
x = 257
y = x

del x
del y
'''
Now no variable refers to integer 10.
Once references reach zero, object becomes eligible for cleanup by Garbage Collector.
'''

import sys

x = 257
y = x
print("refcount before delete:", sys.getrefcount(257)) #6

del x
print("refcount after deleting x:", sys.getrefcount(257)) #5

del y
print(sys.getrefcount(257))# 4

'''
Cleanup may not be immediate

Python may hold cached integers

## Learning :- 

GC reclaims memory when reference count becomes zero

Python delays cleanup for optimization
'''



## Assignment 3: Integer Caching  
# (Python caches integers from -5 to 256.)

a = 70
b = 70
print(a, b)
print(id(a), id(b))
print(a is b)  # True


x = 9000
y = 9000
print(id(x), id(y))
print(x is y)  #It may return false
'''
Python optimizes memory with Integer Caching

Small ints are reused, not recreated
'''
