n = int(input())
sum_temp = 0
for _ in range(n):
    str_temp = input()
    ypow = str_temp[-1]
    xnum = str_temp[0:len(str_temp)-1]
    sum_temp += int(xnum)**int(ypow)
print(sum_temp)