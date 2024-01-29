n = int(input())
for _ in range(n):
    m = int(input())
    int_temp = 1
    for i in range(1,m+1):
        int_temp = i * int_temp
        int_temp = int(str(int_temp)[-1])
    print(int_temp)