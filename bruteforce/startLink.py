import sys
read = sys.stdin.readline


n=int(input())
mat = list(list(map(int,read().split())) for _ in range(n))
check=[False]*n
team1=[]
team2=[]
answer=2147000000

def recursion(cnt,j):
    global answer
    #탈출조건
    if cnt==n/2:
        sum1=0
        sum2=0
        print(check)

        for i in range(n):
            if check[i]:
                team1.append(i)
            else:
                team2.append(i)

        for i in range(len(team1)):
            for j in range(i+1,len(team1)):
                a,b = team1[i],team1[j]
                sum1+=(mat[a][b]+mat[b][a])

        for i in range(len(team2)):
            for j in range(i+1,len(team2)):
                a,b = team2[i],team2[j]
                sum2+=(mat[a][b]+mat[b][a])
        
        
        print(team1,team2, abs(sum1-sum2))


        answer=min(answer,abs(sum1-sum2))
        team1.clear()
        team2.clear()
        return

    for i in range(j,n):
        if check[i]==False:
            check[i]=True
            recursion(cnt+1,i+1)
            check[i]=False

          

recursion(0,0)
print(answer)

