S1="Did"

# TODO: remove spaces
S2 =S1.replace(" ","")

# TODO: reverse string
rev =S2[::-1]

if S2.casefold() == rev.casefold():
    print(S1)
else:
    # TODO: concatenate lowercase strings
    palindrome = (S2.casefold()+rev.casefold())
    print(palindrome)
