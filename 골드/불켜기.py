from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
lights = [[0 for _ in range(n)] for _ in range(n)]
lights[0][0] = 1
turn = [[[] for _ in range(n)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0

for _ in range(m):
    a, b, c, d = map(int, input().split())
    turn[a-1][b-1].append((c-1, d-1))

def bfs(x, y):
    global ans

    q = deque()
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[x][y] = 1
    q.append((x, y))

    while(q):
        a, b = q.popleft()

        for k in turn[a][b]:#현 위치에서 다른 방들의 불을 켜고
            aa, bb = k
            lights[aa][bb] = 1

            if visited[aa][bb] == 1: continue
            for k in range(4):
                if 0<=aa+dx[k]<n and 0<=bb+dy[k]<n and visited[aa+dx[k]][bb+dy[k]]==1:
                    q.append((aa, bb))
                    visited[aa][bb] = 1

        for k in range(4):#현 위치로부터 이동 가능한 곳이 생겼는지 살펴보고 이동
            if 0<=a+dx[k]<n and 0<=b+dy[k]<n and visited[a+dx[k]][b+dy[k]]==0 and lights[a+dx[k]][b+dy[k]] == 1:
                visited[a+dx[k]][b+dy[k]] = 1
                q.append((a+dx[k], b+dy[k]))

    return

bfs(0, 0)

for i in range(len(lights)):
    ans += sum(lights[i])

print(ans)
