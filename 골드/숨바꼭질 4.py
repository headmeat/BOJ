from sys import stdin
from collections import deque
input = stdin.readline

n, k = map(int, input().split())
INF = 100001

q = deque()
visited = [INF for _ in range(100001)]
ans = 200002
cnt = 0

q.append((n, 0))
visited[n] = 0

while(q):
    v, t = q.popleft()
    if v==k: 
        ans = min(ans, t)
        cnt += 1
    if v-1>=0 and t+1<=visited[v-1]: 
        q.append((v-1, t+1))
        visited[v-1] = t+1
    if v+1<100001 and t+1<=visited[v+1]: 
        q.append((v+1, t+1))
        visited[v+1] = t+1
    if v * 2 < 100001 and t+1<=visited[v*2]: 
        q.append((v*2, t+1))
        visited[v * 2] = t+1

print(ans)
tmp = k
route = []
c = 10

while(tmp!=n):
    route.append(tmp)
    goto = tmp
    idx = visited[tmp]

    if tmp-1>=0 and visited[tmp-1]<=idx: goto, idx = tmp-1, visited[tmp-1]
    if tmp+1<INF and visited[tmp+1]<=idx: goto, idx = tmp+1, visited[tmp+1]
    if tmp%2==0 and visited[tmp//2]<=idx: goto, idx = tmp//2, visited[tmp//2]

    tmp = goto

route += [tmp]
route.reverse()

print(" ".join(map(str, route)))
