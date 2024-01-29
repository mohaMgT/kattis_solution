astring= input()
flag = False
for i in range(len(astring)-1):
    if astring[i] == 's' and astring[i+1] == 's':
        flag = True
        break
if flag :
    print("hiss")
else :
    print("no hiss")
