from sys import stdin
from collections import deque
input = stdin.readline

n, k = map(int, input().split())
coin = input().rstrip()
ht = [coin.count("H"), coin.count("T")]

def bfs(x, y):
    global k
    if x==0:
        print(0)
        exit(0)

    q = deque()
    visited = [[0 for _ in range(n+1)] for _ in range(n+1)]
    visited[x][y] = 1
    q.append((x, y, 0))

    while(q):
        a, b, c = q.popleft()

        for idx in range(1, k+1):
            if 0<=a+idx<=n and 0<=b-(k-idx)<=n and visited[a+idx][b-(k-idx)]==0:
                visited[a+idx][b-(k-idx)] = 1
                q.append((a+idx, b-(k-idx), c+1))
                if a-k==0:
                    print(c+1)
                    exit(0)
            if 0<=a-idx<=n and 0<=b+(k-idx)<=n and visited[a-idx][b+(k-idx)]==0:
                visited[a-idx][b+(k-idx)] = 1
                q.append((a-idx, b+(k-idx), c+1))

    return

bfs(ht[0], ht[1])

print(-1)
