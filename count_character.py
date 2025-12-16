## Count character occurances in String
s1 = "Nikhil Mohite"

count_characters = {}

for ch in s1:
    if ch in count_characters:
        count_characters[ch] += 1
    else:
        count_characters[ch] =1
print(count_characters)

#{'N': 1, 'i': 3, 'k': 1, 'h': 2, 'l': 1, ' ': 1, 'M': 1, 'o': 1, 't': 1, 'e': 1}