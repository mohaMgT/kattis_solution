astr = input()
ycount = 0
noycount = 0
for l in astr:
    if l == "a" or l == 'e' or l == 'i' or l == 'o' or l == "u":
        noycount += 1
    if l == 'y':
        ycount += 1
ycount += noycount 
print(noycount, ycount)