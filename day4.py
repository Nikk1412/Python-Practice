### DAY:4 Tuple creation and its importance

##creating tuple using tuple() constructor .
empty_tuple = tuple()
print(empty_tuple)
print()
print()

## Creating single element tuple
single_element = (1,)    # Needs a comma, otherwise Python thinks it's just a value.
print(type(single_element))
print("Single Element tuple:",single_element)
print()
print()


## Creating multi element tuple
multi = (1,2,4,5)
print("Multiple Element tuple:",multi)
print(type(multi))
print()
print()



## Coverting different datatypes into tuples
l= [1,2,3,4]
tuple_from_list=tuple(l)
print("Tuple from list:",tuple_from_list)
print()
print()

string = "Nikhil"
tuple_from_string= tuple(string)
print("Tuple from string:",tuple_from_string)
print()
print()

user_set = {3, 1, 2}
tuple_from_set = tuple(sorted(user_set))
print("Tuple from set:", tuple_from_set)
print()
print()

user_dict = {"a": 1, "b": 2}
keys_tuple = tuple(user_dict.keys())
values_tuple = tuple(user_dict.values())
items_tuple = tuple(user_dict.items())

print("Keys tuple:", keys_tuple)
print("Values tuple:", values_tuple)
print("Items tuple:", items_tuple)
print()
print()


## Problem Statement 2: Read only configuration loader


print("#"*50)
settings=(
		("theme","dark"),
		("tool","vscode"),
		("version",12),
		("backup",True),
)
print(settings)
env_variables =(
		("OS","Linux"),
		("CPU","INTEL"),
		("RAM",16),
)
print(env_variables	)
print("#"*50)


## Tuples cannot be changed / modified
try :
	settings = ("dark", True)
	settings[1] = False  ## Error
except TypeError as e:
	print("Errror :",e)
	print("Tuples cannot be modified , as they are immutable")


## Explain why tuples are safer than lists?
'''
- You cannot change values once created.
- So tuples protect configuration data from accidental changes.
'''

## How immutability prevents runtime bugs
'''
- Once a tuple is created, its data is locked, so nothing in the program can quietly alter it in the background.
- Critical values (like database URLs or tokens) stay protected, because no line of code can rewrite them by accident.
- Immutable data is safe to share across multiple functions or threads, because none of them can corrupt the values.
- Debugging becomes simpler — if configuration cannot change, you don’t waste time searching for where it got modified.
'''





