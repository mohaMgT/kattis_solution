n = int(input())
t = list(map(int,input().split()))
count = 0
for i in t:
    if i <0:
        count= count+1
print(count)