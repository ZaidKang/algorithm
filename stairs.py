n=int(input()) 
list=[0]*300

for i in range(n):
    list[i]=int(input())

sum_Max=[0]*300
sum_Max[0]=list[0]
sum_Max[1]=list[0]+list[1]
sum_Max[2]=max(list[1]+list[2],list[0]+list[2])




for i in range(3,n):
    sum_Max[i]=max(list[i]+list[i-1]+sum_Max[i-3],list[i]+sum_Max[i-2])


print(sum_Max[n-1])
