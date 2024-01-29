v = int(input())
n = int(input())
lstOver = []
for _ in range(n):
    lstOver = list(map(str,input().split()))
    if v <= int(lstOver[1]):
        print(lstOver[0], "opin")
    else:
        print(lstOver[0],"lokud")
    