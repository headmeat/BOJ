from sys import stdin
input = stdin.readline

INF = 10 ** 15

def getMin(dp, visited):
    mn = INF
    idx = -1

    for i in range(1, len(dp)):
        if visited[i] == 0:
            mn = min(dp[i], mn)
            idx = i
    return idx

def update(n):
    for i in matrix[n]:
        if i[0] == start: continue
        dp[i[0]] = min(dp[n] + i[1], dp[i[0]])

N, M = map(int, input().split())
start = int(input())
dp = [INF for _ in range(N+1)]
matrix = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    a, b, w = map(int, input().split())
    matrix[a].append((b, w))
    if a == start: dp[b] = min(dp[b], w)

visited[start] = 1

while ( True ):
    idx = getMin(dp, visited)
    if idx == -1: break
    else:
        visited[idx] = 1
        update(idx)

print(visited)

for i in range(1, N+1):
    if i == start: print(0)
    else:
        if dp[i] == INF: print("INF")
        else: print(dp[i])
