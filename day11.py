# day11.py


# def addition(1, 2):   # invalid syntax

def addition(a, b):
    result = a + b
    print(result)

addition(1, 2)

# 2. Nested Functions & non local


def offer():
    base_offer = 30

    def special_base_offer():
        nonlocal base_offer
        base_offer = 50

    special_base_offer()
    print("special offer", base_offer)

offer()


'''
If you comment out nonlocal base_offer:

Output

special offer 30

Reason:
Without nonlocal, Python creates a new local variable inside the inner function instead of modifying the outer one.

'''


## Global vs Nonlocal Scope


base_offer = 15

def special_offer():
    base_offer = 25

    def prime_customer():
        global base_offer
        base_offer = 50

    prime_customer()

special_offer()
print("final offer", base_offer)


# Output (with global)
# final offer 50

# Change global base_offer to nonlocal base_offer:

# Output
# final offer 15
'''
Reason:

global modifies the variable outside all functions
nonlocal modifies the variable in the nearest outer function only
'''


#Assignment 2: Handling Arguments

# 1. Function with Arguments


def special_offer(percentage):
    print("Offer", percentage)

special_offer("20%")




# 2. Positional vs Keyword Arguments


def rgb(red, green, blue):
    print(red, green, blue)

rgb("50", "70", "80")
rgb(blue="40", red="55", green="70")




# 3. *args and kwargs


def special_offer1(*special, **prime_offer):
    print("special", special)
    print("primeoffer", prime_offer)

special_offer1(
    "15%", "20%",
    primeoffer1="60%",
    fridayprimeoffer="70%"
)


'''
Output


special ('15%', '20%')
primeoffer {'primeoffer1': '60%', 'fridayprimeoffer': '70%'}
'''



## Assignment 3: Array to Function (No Loop)
'''
Condition

No loops
One function
Array passed as parameter
Printed only once, even if function is called multiple times
'''



def print_array(arr):
    if not hasattr(print_array, "printed"):
        print(arr)
        print_array.printed = True

print_array([10, 20, 30])
print_array([10, 20, 30])
print_array([10, 20, 30])


# Output

# [10, 20, 30]




## Assignment 4: return Keyword

# Returning Nothing (None)


def return_nothing():
    pass

print(return_nothing())


# Output :None





# Returning a Single Value


def return_single_value():
    return 100

print(return_single_value())




# Early Return


def offer(totalamount):
    if totalamount > 500:
        return "15% discount"
    return "5% discount"

print(offer(5000))
print(offer(100))




# Returning Multiple Values


def multiple_value():
    return 44, 55, 11

value1, value2, value3 = multiple_value()
print(value1, value2, value3)