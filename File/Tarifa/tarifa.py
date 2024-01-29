x = int(input())
n = int(input())
left = 0

for _ in range(n):
    temp = int(input())
    left += x
    if left - temp >0:
        left -= temp
    else:
        left = 0

print(left + x )
