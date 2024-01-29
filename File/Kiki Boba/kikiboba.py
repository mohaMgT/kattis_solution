astring = input()
bcount = 0
kcount = 0
for i in astring:
    if i == 'b' or i == 'B':
        bcount+=1
    elif i == 'k' or i == 'K':
        kcount+=1
if bcount == 0 and kcount == 0:
    print("none")
elif bcount == kcount:
    print("boki")
elif bcount < kcount:
    print("kiki")
elif kcount < bcount:
    print("boba")