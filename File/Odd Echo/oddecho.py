n = int(input())
lst_str = []
for i in range(n):
    lst_str.append(input())
for i in range(n):
    if i % 2 == 0:
        print(lst_str[i])
