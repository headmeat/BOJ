from sys import stdin
from collections import deque
input = stdin.readline

T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))
    adj = [[] for _ in range(N+1)]
    cnt = [0 for _ in range(N+1)]
    dp = [0 for _ in range(N+1)]

    for _ in range(len(dp)): dp[_] = D[_]

    for i in range(1, K+1):
        a, b = map(int, input().split())
        adj[a].append(b)
        cnt[b] += 1

    W = int(input())

    queue = deque()

    for i in range(1, N+1):
        if cnt[i] == 0: queue.append(i)

    while(queue):
        v = queue.popleft()

        if v == W:
            print(dp[v])
            break

        for n in adj[v]:
            cnt[n] -= 1

            dp[n] = max(dp[n], dp[v] + D[n])

            if cnt[n] == 0: 
                queue.append(n)
