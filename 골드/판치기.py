from sys import stdin
from collections import deque
input = stdin.readline

n, k = map(int, input().split())
coin = input().rstrip()

ans = 10**9

def bfs(head, tail):
    global ans
    q = deque()
    visited = [[0 for _ in range(n+1)] for _ in range(n+1)]
    q.append((head, tail, 0))
    visited[head][tail] = 1

    while(q):
        h, t, flip = q.popleft()

        if h==0: ans = min(ans, flip)

        for idx in range(k+1):
            up, down = idx, k-idx
            if h>=up and t>=down and visited[h-up+down][t+up-down]==0:
                visited[h-up+down][t+up-down] = 1
                q.append((h-up+down, t+up-down, flip+1))

    return

bfs(coin.count("H"), coin.count("T"))
print(ans if ans<10**9 else -1)
