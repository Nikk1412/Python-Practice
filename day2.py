# Day 2 –

## Immutable Datatypes:
'''When I chnage an immutable value, Python creates a new object.

 The id() changes, which creates a  new memory location.

 The original object is not modified.
''' 

'''

Variables are references to objects, not the objects themselves.

Reassigning a variable just points it to a new object.

That's why immutable types look like they change.

'''

# 1. Numeric
num = 10
print("Numeric value:", num, "Type:", type(num), "ID:", id(num))
num = 20  # change value
print("After change:", num, "Type:", type(num), "ID:", id(num))
print()

# 2. Boolean
flag = True
print("Boolean value:", flag, "Type:", type(flag), "ID:", id(flag))
flag = False
print("After change:", flag, "Type:", type(flag), "ID:", id(flag))
print()

# 3. String
text = "Hello"
print("String value:", text, "Type:", type(text), "ID:", id(text))
text = "Hello World"
print("After change:", text, "Type:", type(text), "ID:", id(text))
print()

# 4. Bytes
b = b"ABC"
print("Bytes value:", b, "Type:", type(b), "ID:", id(b))
b = b"XYZ"
print("After change:", b, "Type:", type(b), "ID:", id(b))
print()


### Mutable Datatypes

'''
We can change the  contents without creating a new object

The id() remains the same

This proves they are mutable.
'''


'''
id() gives the memory reference of an object.

Immutable types → new id() after reassignment

Mutable types → same id() after modification

This helps to understand how Python manages memory.
'''


# 1. List
my_list = [10, 20, 30]
print( my_list)
print("Access by index [1]:", my_list[1])
print("List ID before change:", id(my_list))

my_list.append(40)  # modifying list
print("List after append:", my_list)
print("List ID after change:", id(my_list))
print()

# 2. Dictionary
my_dict = {"name": "Nikk", "age": 25}
print("Dictionary:", my_dict)
print("Access by key 'name':", my_dict["name"])
print("Dict ID before change:", id(my_dict))

my_dict["city"] = "Delhi"  # modifying dictionary
print("Dictionary after adding item:", my_dict)
print("Dict ID after change:", id(my_dict))


