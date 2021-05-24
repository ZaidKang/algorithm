n=int(input())
list=[]*(n+1)
list.append(0)
list.append(1)
list.append(2)
for i in range(3,n+1):
    list.append(list[i-2]+list[i-1])
print(list[n]%10007)
    