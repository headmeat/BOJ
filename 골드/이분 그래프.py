from sys import stdin
from collections import deque
input = stdin.readline

def bfs(start):
    q = deque()
    q.append(start)

    while(q):
        node = q.popleft()
        color = visited[node]
        
        for neighbor in adj[node]:
            if visited[neighbor] == 0:
                visited[neighbor] = 1 if color==2 else 2
                q.append(neighbor)
            elif visited[neighbor]==color: return "NO"

    return "YES"

for _ in range(int(input())):
    v, e = map(int, input().split())
    adj = [[] for _ in range(v)]

    for i in range(e):
        a, b = map(int, input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)

    visited = [0 for _ in range(v)]#1 or 2
    
    ans = "YES"

    for i in range(v):
        if visited[i]==0: 
            visited[i] = 1
            if bfs(i) == "NO": ans = "NO"

    print(ans)
