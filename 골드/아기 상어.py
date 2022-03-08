from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
shark_size = 2
shark_loc = [0, 0]
eat_count = 0
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
count = 0

def bfs(start):
    q = deque()
    q.append((start[0], start[1], 0))
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[start[0]][start[1]] = 1

    while(q):
        a, b, d = q.popleft()

        if 0<arr[a][b]<9:
            distances.append((a, b, d))

        for i in range(4):
            tmp_x, tmp_y = a+dx[i], b+dy[i]

            if 0<=tmp_x<n and 0<=tmp_y<n and visited[tmp_x][tmp_y] == 0 and arr[tmp_x][tmp_y]<=shark_size:
                visited[tmp_x][tmp_y] = 1
                q.append((tmp_x, tmp_y, d+1))

    return 0

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9: shark_loc[0], shark_loc[1] = i, j

while(True):
    goto = [-1, -1]
    minimum = 401
    rem = -1
    distances = []

    bfs(shark_loc)
    distances.sort(key = lambda x: (x[2], x[0], x[1]))

    for i in range(len(distances)):
        x, y, d = distances[i]

        if 0<d<minimum and  arr[x][y]<shark_size:
            minimum = d
            goto[0], goto[1] = x, y
            rem = i

    if rem != -1:
        arr[shark_loc[0]][shark_loc[1]] = 0
        shark_loc[0], shark_loc[1] = goto[0], goto[1]
        arr[shark_loc[0]][shark_loc[1]] = 0
        count += minimum
        eat_count += 1

        if eat_count == shark_size:
            shark_size += 1
            eat_count = 0

    else: break

print(count)
