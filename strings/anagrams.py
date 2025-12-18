S1 = 'satte'
S2 = "Taste"

s1 = S1.lower()
s2 = S2.lower()

# TODO: Write a for loop to check each letter and compare counts. If any mismatch, print 'not anagrams' and break.
for x in s1:
    print(x)
    if s1.isalpha():
        if s1.count(x) != s2.count(x):
            print("Not Anagrams")

            break
else:
    print('Anagrams')
