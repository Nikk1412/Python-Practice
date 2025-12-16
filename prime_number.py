## prime number code 
n = int(input("Enter number:"))
count =0
for i in range(1,n+1):  ##prime has only two factors i.e divisible by 1 and number itself 
    
    if n % i ==0:
        count += 1
if count ==2:
    print("Prime Number")
else:
    print("Not prime")