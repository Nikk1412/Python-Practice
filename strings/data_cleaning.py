scan = 'These+notes#reveal9Newton seeking-out an{underlying structure to/the\pyramid}'
clean = ''
for x in scan:
    if x.isalpha() or x.isspace():
        clean= clean + x
    else:
        clean = clean + " "

#TODO:Write the  Data Cleaning Logic using for loop below

        
print(clean)
