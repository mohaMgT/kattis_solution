lstTemp = []
for _ in range(5):
    lstTemp.append(sum(list(map(int,input().split()))))
print(lstTemp.index(max(lstTemp))+1 ,max(lstTemp) )