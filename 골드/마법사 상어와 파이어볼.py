from sys import stdin
from collections import deque
input = stdin.readline

n, m, k = map(int, input().split())
q = deque()
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for i in range(m):
    q.append(list(map(int, input().split())))

def fix(x):
    if x>=n:
        x %= n
    if x<-n:
        x *= -1
        x %= n
        x *= -1

    return x

def move():
    visited = [[[0 for _ in range(5)] for _ in range(n)] for _ in range(n)]
    #0:짝, 1:홀, 2:질량, 3:속력, 4: 방향

    while(q):
        r, c, mm, s, d = q.popleft()

        r = fix(r + dx[d]*s)
        c = fix(c + dy[d]*s)

        visited[r][c][d%2] += 1
        visited[r][c][2] += mm
        visited[r][c][3] += s
        visited[r][c][4] = d

    merge(visited)

def merge(visited):
    for i in range(n):
        for j in range(n):
            sm = sum(visited[i][j][:2])

            if sm==1:
                q.append((i, j, visited[i][j][2], visited[i][j][3], visited[i][j][4]))
            elif sm>1:
                x = 0 if visited[i][j][0]==0 or visited[i][j][1]==0 else 1
                    
                mm, s = visited[i][j][2:4]
                mm //= 5
                if mm==0: continue
                s //= sm

                for direction in range(x, 8, 2):
                    q.append((i, j, mm, s, direction))

    return

for i in range(k):
    move()

total = 0

while(q):
    tmp = q.popleft()
    total += tmp[2]

print(total)
