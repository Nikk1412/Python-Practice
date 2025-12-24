# Day 9 : Loops in Python
# if condition:
temperature = 35

if temperature > 30:
    print("Turn on the fan")


#if else condition:
balance = 500
price = 700

if balance >= price:
    print("Purchase successful")
else:
    print("Insufficient balance")


#if elif else condition:
balance = 500
price = 700

if balance >= price:
    print("Purchase successful")
elif balance >= price * 0.8:
    print("Purchase successful with a discount")
else:
    print("Insufficient balance")
    
#nested if condition:
username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Invalid username")


## Ternary operator 
percentage = 35
Pass_percentage = 35 if percentage < 35 else percentage
print("Pass percentage is:", Pass_percentage)

# match-case (Python 3.10+)

choice = 2

match choice:
    case 1:
        print("Start Game")
    case 2:
        print("Load Game")
    case 3:
        print("Exit")
    case _:
        print("Invalid choice")


# Assignment 2

# 1.`Print numbers from 1 to 4 using a for loop`
for obj_item in range(1, 5):
    print(obj_item)
    
# 2. Print list items using a for loop
l1 = ["Red", "Green", "Blue", "White"]
for item in l1:
    print(item)

# 3. enumerate()
# Used to print the index and item of a list.
colors = ["Yellow", "Green", "Blue"]
for index, item in enumerate(colors):
    print(index, item)
    
# 4. zip()
# Used to combine multiple lists.
color = ["Red", "Green", "Blue"]
main_color = ["White", "Black"]
for color_item, main_color_item in zip(color, main_color):
# Print both values and observe how elements are paired.
# Note: Iteration stops at the shortest list.
    print(color_item, main_color_item)
    
# 5. while loop
# Test with any example using the += operator.
# Observe how the loop condition changes with each iteration.
count = 0   
while count < 5:
    print("Count is:", count)
    count += 1

# 6. continue in a for loop with if statement
# Use continue to skip the current iteration based on a condition.
# Print the output and observe which values are skipped.
for item in range(1, 10):
    if item % 2 == 0:
        continue
    print(item) 

# 7. continue and break
for item in range(1, 10):
    if item == 5:
        break
    if item % 2 == 0:
        continue
    print(item)

# Using a list and a for loop.
my_list = [10, 20, 30, 40, 50]
for item in my_list:
    print(item)
# Using a list containing tuples (tuple with 2 values, etc.) and a for loop.
my_list = [(1, 'a'), (2, 'b'), (3, 'c')]
for number, letter in my_list:
    print(number, letter)
# Using a dictionary and a for loop.
my_dict = {'x': 10, 'y': 20, 'z': 30}
for key, value in my_dict.items():
    print(key, value)           


# Assignment 3: for loop with else
students = [("Abc", 2), ("Xyz", 3), ("PQR", 5)]

for name, rollno in students:
    if rollno >= 5:
        print(name)
        break
else:
    print("Nothing found")


# Assignment 4 Walrus Operator
'''
Walrus Operator (:=) — Python 3.8+
The walrus operator (:=) is also called the assignment expression.
It allows you to assign a value to a variable as part of an expression, which helps shrink code into shorter, more readable forms.

'''
while (command := input("Enter command (type exit to stop): ")) != "exit":
    print(f"You entered: {command}")
print("Loop ended")


#Another while + walrus example
while (num := int(input("Enter a number (0 to stop): "))) != 0:
    print(f"Square is {num ** 2}")

print("Program finished")