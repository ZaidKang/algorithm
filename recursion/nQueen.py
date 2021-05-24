import sys
read=sys.stdin.readline

def sol(left, center, right,queen):
    global count
    if queen== n:
        count += 1
        return
        
    for i in range(queen):
        left[i] -= 1
        right[i] += 1

    for i in range(n):
        if i not in left and check[i] and i not in right:
            check[i]=False
            #다음칸으로 이동
            sol(left+[i], center+[i], right+[i], queen+1)
            check[i]=True
    return

n = int(input())

count = 0
check=list(True for _ in range(n))

sol([], [], [],0)
print(count)