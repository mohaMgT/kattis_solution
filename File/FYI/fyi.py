astring = input()
flag = True
for i in astring[0:3]:
    if i != '5':
        flag = False
        break
if flag :
    print(1)
else:
    print(0)