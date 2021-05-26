# 지도의 크기를 입력받고
# 2차원 배열을 입력받고


# 2차원 배열을 받은거에서 bfs를 통해서 연결노드를 탐색하고 while queue구문 끝나면 단지 수 +1

# 근데 여기서 bfs를 하면서 노드를 탐색할때마다 단지내 집 수를 +1해주고 while queue를 통해서 단지 탐색 끝나면 append
from collections import deque
import sys 

n=int(input())
# graph=[[]for _ in range(N)]
graph = list(list(input().strip()) for _ in range(n))
visited= list(list(False for _ in range(n)) for _ in range(n))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

house_count_list=[]

def bfs():
    count=0
    for i in range(0,n):
        for j in range(0,n):
            if not visited[i][j] and graph[i][j]=='1':
                house_count=0
                visited[i][j]=True
                queue = deque()
                queue.append((i,j))
                
    
                while queue:
                    x,y=queue.popleft()
                    house_count+=1
                    for i in range(4):
                        nx=x+dx[i]
                        ny=y+dy[i]

                        if nx<0 or nx>=n or ny<0 or ny>=n:
                            continue
                        if graph[nx][ny]=='0':
                            continue
                        if graph[nx][ny]=='1' and visited[nx][ny]==False:
                            visited[nx][ny]=True
                            queue.append((nx,ny))
                            
                            

                count+=1
                house_count_list.append(house_count)
                

    print(count)
    for i in range(len(house_count_list)):
        print(house_count_list[i])


bfs()



