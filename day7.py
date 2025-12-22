# Case 1: Same Reference with Mutable Datatype
list1 = [1, 2, 3, 4, 5]     # original list
list2 = list1               # same reference

# Modify list using list1
list1[2] = 99               # change the 3rd element

print("list1 =", list1)
print("list2 =", list2)


# CASE 2 — Changing Reference (Two Separate Lists)
# When lists are separate, one operation does not affect the other.

# Case 2: Changing reference
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]   # separate list

x[2] = 99

print("x =", x)
print("y =", y)



# Case 2 — Using Copy (not direct assignment)
a = [1, 2, 3, 4, 5]
b = a.copy()      # new list created

a[1] = 50

print("a =", a)
print("b =", b)



##Assignment 2 — copy() vs deepcopy()
'''
copy() = shallow copy

Copies outer list only

deepcopy()

Copies everything, including inner objects
'''
import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)       # shallow copy
deep = copy.deepcopy(original)      # deep copy

original[0][0] = 99                 # modify nested element

print("Original:", original)
print("Shallow:", shallow)
print("Deep:", deep)



## Assignment 3 — Use of == (Equality Operator)
# == checks value equality
a = 10
b = 10
print(a == b)   # True




## Assignment 4 — Use of is (Identity Operator)
# is checks memory address 
x = [1,2,3]
y = x
print(x is y)   # True


y = [7,8,6]
print(x is y)   # False Now y refers to a new list box.



