n = int(input())
for _ in range(n):
    temp_str = ""
    astr1 = input()
    astr2 = input()
    for i in range(len(astr1)):
        if astr1[i] == astr2[i]:
            temp_str += "."
        else:
            temp_str += "*"
    print(astr1)
    print(astr2)
    print(temp_str)
    print()