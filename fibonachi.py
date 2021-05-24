n=int(input())
list=[0,1]
for i in range(n):
    list.append(list[i]+list[i+1])
print(list[n])