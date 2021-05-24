N, M = map(int, input().split()) #근데 이렇게 하면 N은 의미 없는 변수가 되는거 아님?
value = list(map(int, input().split()))
length=len(value)

for i in range(length-2):
    for j in range(i+1,length-1):
        for k in range(j+1,length):
            if value[i]+value[j]+value[k]>M:
                continue
            else:
                sum=max(sum,value[i]+value[j]+value[k])


print(sum)

#https://pacific-ocean.tistory.com/130
#열받네 씨발