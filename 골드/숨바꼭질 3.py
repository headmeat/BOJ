from sys import stdin
from collections import deque
input = stdin.readline

n, k = map(int, input().split())
INF = 100001

q = deque()
visited = [INF for _ in range(100001)]
ans = 200002

q.append((n, 0))
visited[n] = 0

while(q):
    v, t = q.popleft()
    if v==k: ans = min(ans, t)
    if v-1>=0 and t+1<visited[v-1]: 
        q.append((v-1, t+1))
        visited[v-1] = t+1
    if v+1<100001 and t+1<visited[v+1]: 
        q.append((v+1, t+1))
        visited[v+1] = t+1
    if v * 2 < 100001 and t<visited[v*2]: 
        q.append((v*2, t))
        visited[v * 2] = t

print(ans)
