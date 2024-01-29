m = int(input())
n = int(input())
lst = []
empty = 0
for i in range(n):
    lst.append(input())
for i in range(n):
    for cell in lst[i]:
        if cell == ".":
            empty+=1
print(empty/(n*m))
