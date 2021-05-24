list=[]*9
check=[False]*9
result=[]*7

for i in range(9):
    list.append(int(input()))

def recursive(index):
    #탈출조건
    if index==9:
        sum=0
        count=0
        
        for i in range(0,9):
            if check[i]:
                sum=sum+list[i]
                count=count+1
                result.append(list[i])
        if sum==100 and count==7:
            result.sort()
            for i in range(len(result)):
                print(result[i])

        else:
            result.clear()

        return 

    #경우의 수 발생
    check[index]=True
    recursive(index+1)

    check[index]=False
    recursive(index+1)

recursive(0)
