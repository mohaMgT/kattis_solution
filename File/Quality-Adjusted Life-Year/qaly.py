n = int(input())
temp_sum = 0
for _ in range(n):
    y,q = map(float,input().split())
    temp_sum+=  y*q
print(temp_sum)