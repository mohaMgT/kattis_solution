n,m = list(map(int,input().split()))
temp_sum = 0
for _ in range(n):
    temp_sum += int(input()) 
if m >= temp_sum:
    print("Jebb")
else:
    print("Neibb")