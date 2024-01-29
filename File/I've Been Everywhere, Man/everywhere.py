outer = int(input())
for _ in range(outer):
    n = int(input())
    lst_temp = []
    count = 0
    for _ in range(n):
        temp = input()
        if temp not in lst_temp:
            count += 1
            lst_temp.append(temp)
    print(count)