# Code for finding out longer string 
s1 = input("Enter String 1: ")
s2 = input("Enter String 2: ")

if len(s1) > len(s2): # find out length of string and compare 
    print("String 1 is longer:", s1)
elif len(s2) > len(s1):
    print("String 2 is longer:", s2)
else:
    print("Both strings are equal in length")
    
    

## Using for loop
s3 = "Python"
s4 = "Programming"

count1=0
count2=0
## using for loop iterate through the string
for i in s3: 
    count1 +=1
print(count1) 

for i in s4:
    count2 +=1
print(count2)

if count1 > count2:
    print("s3 is longer")
elif count2 >count1:
    print("S4 is longer")
else:
    print("Both are equal")
