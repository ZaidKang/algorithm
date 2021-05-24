
N=int(input()) #배열 사이즈 입력받기
arr=list(map(int,input().strip().split()))#배열 data입력받기
fix_arr=[]*N
sum=0


def recursion(index):
    if index==N:
        global minimum_value

        for i in range(N-1):
            sum=sum+abs(fix_arr[i]-fix_arr[i+1])
            minimum_value=min(sum,minimum_value)


    check[index]=True
    recursion(index+1)

    check[index]=False
    recursion(index+1)

recursion(0)




