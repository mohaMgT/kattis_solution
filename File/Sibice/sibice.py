import math
n,w,h = list(map(int,input().split()))
for _ in range(n):
    temp = int(input())
    if temp <= w or temp <= h or temp <= math.sqrt(w**2 + h**2):
        print("DA")
    else:
        print("NE")