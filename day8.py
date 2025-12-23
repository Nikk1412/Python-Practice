

#  Day 8 – 

##  What is a Tuple?

# A tuple is a collection of values that:
# #  Are ordered
# #  Are immutable (cannot be changed after creation)
# #  Use round brackets ()


tuple_subject_list = ("Math", "Sci", "English")
# Once created, you cannot add, remove, or change elements in a tuple.


## Tuple Unpacking

# Tuple unpacking allows assigning multiple values in one line.

(subject1, subject2, subject3) = tuple_subject_list

print(subject1)   # Math
print(subject2)   # Sci
print(subject3)   # English


## Multiple Variable Declaration (Tuple Declaration)

pcb_percentage, pcm_percentage = 2, 1
# Python internally treats this as tuple unpacking.

##  Variable Swapping (Without Third Variable )

pcb_group = pcm_percentage
pcm_group = pcb_percentage

# Swap
pcb_group, pcm_group = pcm_group, pcb_group

##  Membership Operator (in)
# Used to check if an element exists.
print("Geography" in tuple_subject_list)


## Why Python is Case-Sensitive?

# Python treats:
# name ≠ Name ≠ NAME
# Because they are different identifiers.



#  Assignments – Day 8
##  Assignment 1 – Basic List Operations


fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

fruits.remove("Banana")
fruits.append("Pineapple")
fruits.append("Papaya")
fruits.insert(2, "Kiwi")

print(fruits)


##  Assignment 2 – Method Practice
numbers = [10, 20, 30, 20, 40]

numbers.append(50)
print(numbers)

numbers.insert(2, 15)
print(numbers)

numbers.remove(20)
print(numbers)

numbers.pop()
print(numbers)

print(numbers.count(20))

numbers.reverse()
print(numbers)

numbers.sort()
print(numbers)




## Assignment 3 – Extend Method


subjects1 = ["Math", "Physics"]
subjects2 = ["Chemistry", "Biology"]

subjects1.extend(subjects2)

print(subjects1)
#  extend() adds elements one by one, not as a nested list.



## Assignment 4 – Thinking Questions

### Why is list called mutable?
# Because we can change, add, or remove elements after creation.



### 🔹 Difference between append() and extend()?
'''
append()  -->  Adds single element , Can add list as one item              
extend() --->  Adds multiple elements, Merges lists
'''
     
    
### What happens if we use wrong index?
# IndexError: list index out of range




##  Operator Overloading

print(10 + 20)     # Adds numbers
print("Hi" + "Bye")  # Concatenates strings
#  Same operator, different behavior.



## 2️ bytearray
b = bytearray([65, 66, 67])
b[0] = 97
print(b)




## 3️ Set

#  Unordered ,  No duplicates, Mutable
my_set = {1, 2, 3, 3}
print(my_set)


## Frozenset

#  Immutable version of set
#  Cannot add or remove elements.

fs = frozenset([1, 2, 3])

# Dictionary – 
student = {
    "name": "Nikk",
    "age": 22,
    "course": "BTech CSE"
}

print(student.keys())
print(student.values())
print(student.items())

## Difference: pop() vs popitem()

student.pop("age")     # Removes specific key
student.popitem()      # Removes last inserted item


## del Keyword
del student["course"]




## update() and get()
#  get() avoids errors if key not found.

student.update({"city": "Pune"})
print(student.get("name"))

