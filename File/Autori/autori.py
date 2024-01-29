astring = input()
temp = astring[0]
for i,j in enumerate(astring):
    if j == '-':
        temp += astring[i+1]
print(temp)