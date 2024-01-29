astr = input()
str_temp = ""
pre = None
for l in astr:
    if pre == None:
        pre = l
        str_temp += l
    else:
        if l != pre:
            pre = l
            str_temp += l
print(str_temp)
    