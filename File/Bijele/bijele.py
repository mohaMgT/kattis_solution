defau = [1,1, 2, 2, 2, 8]
n = list(map(int, input().split()))
for i in range(len(n)):
    n[i] = defau[i] - n[i]

for i in n:
    print(i,end= " ")

