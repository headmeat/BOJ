from sys import stdin
from collections import deque
input = stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    adj = [x-1 for x in list(map(int, input().split()))]
    cnt = [0 for _ in range(n)]
    ans = 0
    q = deque()

    for neighbor in adj:
        cnt[neighbor] += 1

    for i in range(len(cnt)):
        if cnt[i]==0: q.append(i)

    while(q):
        v = q.popleft()
        ans += 1

        cnt[adj[v]] -= 1

        if cnt[adj[v]] == 0: q.append(adj[v])

    print(ans)
