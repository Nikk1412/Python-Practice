## Day 8 : TUPLES
'''
A tuple is:

Ordered

Immutable (cannot be changed)

Written using round brackets ()
'''

subject_list = ("Maths","Science","English")

# You cannot add modify or remove elements from tuple



# 2. Tuple Unpacking
subject1,subject2,subject3 = subject_list
print(subject1)
print(subject2)
print(subject3)

# 3. Multiple Variable Declaration
# Python automatically creates a tuple and unpacks it.
pcb_percentage, pcm_percentage = 2, 1


#4. Variable Swapping 
pcb_group = pcb_percentage
pcm_group = pcm_percentage

pcb_group, pcm_group = pcm_group, pcb_group

print(pcb_group, pcm_group)


# 5. Membership Operator (in)
print("Geography" in subject_list)  # False

#6. Why python is case-sensitive?
# Name and name are treated as different variables
Name = "Nikk"
name = "Python"




## Assignment 1 : Basic lists operations 
fruits = ['Apple','Banana','Orange','Grapes','Mango']

fruits.remove('Banana')
fruits.append('Pineapple')
fruits.insert(2,'Kiwi')
fruits.extend(['Chikoo','Strawberry'])

print(fruits)

## Assignment 2: Methods Practice
numbers = [5, 3, 7, 3, 9]

numbers.append(10)
print(numbers)

numbers.insert(1, 4)
print(numbers)

numbers.remove(3)
print(numbers)

numbers.pop()
print(numbers)

print(numbers.count(3))

numbers.reverse()
print(numbers)

numbers.sort()
print(numbers)


# Assignment 3: extend method

subjects1 = ["Math", "Physics"]
subjects2 = ["Chemistry", "Biology"]

subjects1.extend(subjects2)
print(subjects1)


# Assignment 4 :
# Why is list called mutable?
#- Because we can change, add, or remove elements after creation.

# Difference between append() and extend()?
# append()- adds one item , adds as single element
# extend()- Adds multiple items, Merges list


a = [1, 2]
a.append([3, 4])   # [1, 2, [3, 4]]
a.extend([5, 6])   # [1, 2, [3, 4], 5, 6]
print(a)


## Additional Topics 
# 1. Operator Overloading
print(2 + 3)        # 5
print("Py" + "thon") # Python


#2. Bytearray
'''
Mutable version of bytes

Used in low-level programming
'''
b = bytearray([65, 66, 67])
b[0] = 68
print(b)


#3. Set
# Unordered
# No duplicates
s = {1, 2, 3, 3}
print(s)

##4. Frozenset
# immutable dataset
#Cannot add or remove elements.
fs = frozenset([1, 2, 3])


## Dictionary Understanding 
student = {
    "name": "Nikk",
    "age": 20,
    "course": "Python"
}

print(student.keys())
print(student.values())
print(student.items())


student.pop("age")        # removes specific key
student.popitem()         # removes last inserted item


del student["course"]

student.update({"age": 21})
print(student.get("name"))
print(student.get("marks", "Not Found"))
