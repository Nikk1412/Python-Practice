# DAY 5
# Assignment 1 : Changing References but Not Changing the Object
roll_no = 20
old_roll_no = roll_no

print("Before Chnage : ")
print("Roll No:",roll_no,"id:",id(roll_no))  #id : 140733718350872 (same id)
print("old_roll_no :",old_roll_no,"id:",id(old_roll_no))  #id :140733718350872 (same id)


roll_no = 21

print("After Change:")
print("roll_no:",roll_no,"id:",id(roll_no))  #id : 140735032675384  ( new id )
print("old_roll_no :",old_roll_no,"id:",id(old_roll_no))  #id : 140735032675352 (same id)

'''
Reassigning a variable creates a new object

Variables are references, not storage boxes
'''

## Assignment 2 : Same Object But Multiple Names
'''
Python variables do not store values.
They store pointers to objects in memory.
'''
roll_no = 20
old_roll_no = roll_no

'''
There is only one object — integer 20.
Two names refer to it.
'''

roll_no = 20
old_roll_no = roll_no

print("roll_no =", roll_no, "id:", id(roll_no))
print("old_roll_no =", old_roll_no, "id:", id(old_roll_no))

print("\nroll_no is old_roll_no:", roll_no is old_roll_no)

## Learning :
'''
Multiple names can reference the same memory location

Python reduces memory duplication
'''
