from sys import stdin
from collections import deque
input = stdin.readline

n, m, k = map(int, input().split())
lifeordeath = [1 for _ in range(m)]
alive = m
arr = [list(map(int, input().split())) for _ in range(n)]
sharks = [[-1, -1] for _ in range(m)]
shark_heads = list(map(int, input().split()))
priority = [[list(map(int, input().split())) for _ in range(4)] for _ in range(m)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#전처리
for i in range(m):
    shark_heads[i] -= 1
    for j in range(4):
        for l in range(4):
            priority[i][j][l] -= 1

for i in range(n):
    for j in range(n):
        if 0<arr[i][j]<m+1: 
            sharks[arr[i][j]-1] = [i, j]
            arr[i][j] = [arr[i][j]-1, k]
        else: arr[i][j] = [-1, 0]

def move(num):
    direction = shark_heads[num]
    x, y = sharks[num][0], sharks[num][1]

    for i in priority[num][direction]:
        if 0<=x+dx[i]<n and 0<=y+dy[i]<n and arr[x+dx[i]][y+dy[i]][1] == 0:
            sharks[num] = [x+dx[i], y+dy[i]]
            shark_heads[num] = i
            return

    for i in priority[num][direction]:
        if 0<=x+dx[i]<n and 0<=y+dy[i]<n and arr[x+dx[i]][y+dy[i]][0] == num:
            sharks[num] = [x+dx[i], y+dy[i]]
            shark_heads[num] = i
            return

c = 0

while(alive>1 and c<=1000):
    c += 1

    #이동
    for i in range(m-1, -1, -1):
        if lifeordeath[i] == 1: move(i)

    #겹침 여부 확인
    for i in range(m):
        if lifeordeath[i] == 0: continue

        for j in range(i+1, m):
            if lifeordeath[j] == 0: continue

            if sharks[i] == sharks[j]:
                lifeordeath[j] = 0
                alive -= 1

    #시간 지남
    for i in range(n):
        for j in range(n):
            if arr[i][j][1] > 0: arr[i][j][1] -= 1
            if arr[i][j][1] == 0: arr[i][j][0] = -1

    for i in range(m):
        if lifeordeath[i] == 1:
            x, y = sharks[i]
            arr[x][y] = [i, k]

if c == 1001: print(-1)
else: print(c)
