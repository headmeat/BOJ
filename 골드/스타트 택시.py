from sys import stdin
from collections import deque
input = stdin.readline

n,m,fuel = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
people = [[0 for _ in range(n)] for _ in range(n)]
taxi = list(map(int, input().split()))
human = [list(map(int, input().split())) for _ in range(m)]
taxi[0] -= 1
taxi[1] -= 1

for i in range(m):
    for j in range(4):
        human[i][j] -= 1
    people[human[i][0]][human[i][1]] = i+1

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(sw, goto):
    global taxi, fuel
    cands = []
    q = deque()
    q.append((taxi[0], taxi[1], fuel))
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[taxi[0]][taxi[1]] = 1

    while(q):
        x, y, f = q.popleft()

        if sw==0 and people[x][y]>0:
            if f<0: break
            cands.append((-f, x, y))

        if sw==1 and x==human[goto][2] and y==human[goto][3]:
            if f<0: break
            else:
                taxi[0], taxi[1] = x, y
                fuel = f + (fuel-f)*2

            return

        for j in range(4):
            if 0<=x+dx[j]<n and 0<=y+dy[j]<n and arr[x+dx[j]][y+dy[j]] != 1 and visited[x+dx[j]][y+dy[j]] == 0:
                q.append((x+dx[j], y+dy[j], f - 1))
                visited[x+dx[j]][y+dy[j]] = 1

    if len(cands):
        cands.sort(key=lambda x: (x[0], x[1], x[2]))
        a, b, c = cands[0]
        num = people[b][c]
        people[b][c] = 0
        taxi[0], taxi[1] = b, c
        fuel = -a
        return num-1
    else:
        print(-1)
        exit(0)

for i in range(m):
    bfs(1, bfs(0, 0))

print(fuel)
