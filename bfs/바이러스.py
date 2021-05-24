from collections import deque

def bfs(v):
    count=1
    q=deque([[v,count]])
    while q:
        value = q.popleft()
        v=value[0]
        count=value[1]
        
        if not visited[v]:
            count +=1
            visited[v]=True
            for e in adj[v]:
                if not visited[e]:
                    q.append([e,count])

    return count

   


n= int(input())
m= int(input())
adj=[[]for _ in range(n+1)]
visited=[False]*(n+1)

for _ in range(m):
    x,y = map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)

print(bfs(1))