n=int(input())
list=[0]*(n+1)

for i in range(2,n+1):#2부터 n까지
    list[i]=list[i-1]+1

    if i%2==0 and list[i]>list[i//2]+1:
        list[i]=list[i//2]+1

    if i%3==0 and list[i]>list[i//3]+1:
        list[i]=list[i//3]+1

print(list[n])