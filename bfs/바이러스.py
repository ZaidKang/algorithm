from collections import deque

def bfs(v):
    count=0
    q=deque([v])
    while q:
        value = q.popleft()
        count+=1
        
        for e in adj[value]:
            if not visited[e]:
                visited[e]=True
                q.append(e)

    return count-1

n= int(input())
m= int(input())
adj=[[]for _ in range(n+1)]
visited=[False]*(n+1)
visited[1]=True

for _ in range(m):
    x,y = map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)

print(bfs(1))