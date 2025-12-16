n= int(input("Enter Number :")) ## 1221
temp = n
rev = 0
while n >0:
    r = n % 10  # get last digit  
    rev =  rev * 10 + r  
    n = n // 10 # remove last digit
print("Reversed Number",rev) ## check answer

if rev == temp:
    print("palindrome number") 
else:
    print("not palindrome")