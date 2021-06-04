from collections import deque
import sys
read = sys.stdin.readline


N,M=map(int,read().split())
adj=[[]for _ in range(N+1)]
visited=[False]*(N+1)

for _ in range(M):
    x,y = map(int,read().split())
    adj[x].append(y)
    adj[y].append(x)


def bfs():
    count=0
    for i in range(1,N+1):
        if not visited[i]:
            visited[i]=True
            q=deque([i])

            while q:
                v=q.popleft()
                
                for e in adj[v]:
                    if visited[e]==False:
                        visited[e]=True
                        q.append(e)

            count+=1    

    print(count)


bfs()