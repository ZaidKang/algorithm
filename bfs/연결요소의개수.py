from collections import deque


N,M=map(int,input().split())
adj=[[]for _ in range(N+1)]
visited=[False]*(N+1)

for _ in range(M):
    x,y = map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)


def bfs():
    result=0
    for node in adj:
        if not visited[node]:
            visited[node]=True
            q=deque([node])
            result+=1

            while q:
                v=q.popleft()
                
                if not visited[v]:
                    visited[v]=True
                    for e in adj[v]:
                        if not visited[e]:
                            q.append([e])

    print(result)


bfs()