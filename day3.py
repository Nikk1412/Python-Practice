# Day 3
# Understanding Tuples and Immutability in Python:

# Problem Statement:
# Create a tuple that stores and displays a student's information using a tuple.

student_profile = (
	4,
	"Nikhil Mohite",
	9.07,
	False,
	["Database","OOPS","Python"]

)


print("#"*40)
# Display each element of the tuple using indexing.
print("Student ID :",student_profile[0])
print("Student Name :",student_profile[1])
print("GPA :",student_profile[2])
print("Is Enrolled :",student_profile[3])
print("Subjects :",student_profile[4])
print("#"*40)

print()
print()

### Try to modify the tuple elements and fix the errors
# student_profile[1] = 'Nikk'  ## TypeError: 'tuple' object does not support item assignment

print("#"*40)
try:
	student_profile[1]='Nikk'
except TypeError as e:
	print("Error:", e)
	print("Tuples are immutable so they cant be change.")
print("#"*40)

print()
print()


print("#"*40)
print("Now modifying Lists inside tuple :")
student_profile[4].append("Machine Learning")
print("Updated Subjects list :",student_profile[4])
print("We can see that List is modified as LIST is mutable..")
print("#"*40)

print()
print()

print("....Key Learning from Day 3....")
print("1. Tuple cannot be changed because it is immutable.")
print("2. But if the tuple is holding something that can be changed (like a list),you can change that thing.")
