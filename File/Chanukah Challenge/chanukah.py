p = int(int(input()))
for i in range(p):
    temp_lst = list(map(int,input().split()))
    print(temp_lst[0],int(temp_lst[1]*(temp_lst[1] + 1)/2 + temp_lst[1]))
