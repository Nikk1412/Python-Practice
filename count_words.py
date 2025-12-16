# Count words in String
s1= 'Python is easy and I love Python'
## Words are separated using Spaces
# Using split() function we separate out the words in String

words= s1.split()

print(words) # ['Python', 'is', 'easy', 'and', 'I', 'love', 'Python']

print(len(words)) #7



## USing for loop logic
count =0

for words in s1.split(): 
    count = count+1
print("Total words : ",count) #7
    
    