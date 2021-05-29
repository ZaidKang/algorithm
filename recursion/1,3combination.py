nums=[1,2,3]
check=[False]*3

def recursive(index):
    if index==3:
        for i in range(len(check)):
            if check[i]:
                print(nums[i], end='')
        print('\n')
         #개행문자 어디에 넣는지만 좀 조심    
        return     

    #경우의 수 발생
    check[index]=True
    recursive(index+1)

    check[index]=False
    recursive(index+1)




recursive(0)