from sys import stdin
from collections import deque
input = stdin.readline

arr = [[x for x in input().rstrip()] for _ in range(5)]
seat = []
empty = []
possible = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(5):
    for j in range(5):
        seat += [(i, j)]

def bfs(cand):
    global ans

    q = deque()
    visited = [[0 for _ in range(5)] for _ in range(5)]

    x, y = seat[cand[0]]

    q.append((x, y))
    visited[x][y] = 1
    c = 0

    while(q):
        a, b = q.popleft()
        c += 1

        for k in range(4):
            if 0<=a+dx[k]<5 and 0<=b+dy[k]<5 and visited[a+dx[k]][b+dy[k]]==0 and select[a+dx[k]][b+dy[k]]==1:
                visited[a+dx[k]][b+dy[k]] = 1
                q.append((a+dx[k], b+dy[k]))

    if c == 7: ans += 1

    return

def comb(cand, k, c):
    global possible
    if 7 - len(cand) + c < 4: return

    if len(cand)==k:
        bfs(cand)
        return

    for i in range(25):
        if cand and i<=cand[-1]: continue
        
        x, y = seat[i]

        if i not in cand:
            cand += [i]
            select[x][y] = 1
            comb(cand, k, c+1 if arr[x][y]=="S" else c)
            select[x][y] = 0
            del cand[-1]

ans = 0

select = [[0 for _ in range(5)] for _ in range(5)]
comb([], 7, 0)

print(ans)
