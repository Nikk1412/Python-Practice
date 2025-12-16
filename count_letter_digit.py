text = "Nikhil Mohite is 23 Years Old and Has 6000 Rs"
## We had to count letters and digits in string

# using for loop we can iterate through string 
## isalpha() -> checks for letters
##isdigit() --> check for Numbers
count_alpha = 0
count_digits = 0
for ch in text:
    if ch.isalpha():
        count_alpha += 1
    elif ch.isdigit():
        count_digits += 1

    
print("Total letters:",count_alpha)
print("Total digits:",count_digits)