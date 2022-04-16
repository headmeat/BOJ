from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
score = 0

def bfs(i, j):
    global visited, mx, biggest, rainbows

    q = deque()
    stack = []
    color = arr[i][j]
    q.append((i, j))
    count = 1
    c = 1
    r = 0

    while(q):
        x, y = q.popleft()
        for k in range(4):
            xd, yd = x + dx[k], y + dy[k]
            if 0<=xd<n and 0<=yd<n and (arr[xd][yd]==0 or (arr[xd][yd]==color)) and visited[xd][yd]==0:
                q.append((xd, yd))
                visited[xd][yd] = 1
                count += 1

                if arr[xd][yd]==color: c += 1
                else: stack.append((xd, yd))

    while(stack):
        x, y = stack.pop()
        visited[x][y] = 0
        r += 1

    if count==mx and r>=rainbows:
        mx = count
        rainbows = r
        biggest = [i, j]
    elif count>mx:
        mx = count
        rainbows = r
        biggest = [i, j]

    return

def break_bad(i, j):
    v = [[0 for _ in range(n)] for _ in range(n)]
    v[i][j] = 1
    color = arr[i][j]
    arr[i][j] = -2
    q = deque()
    q.append((i, j))

    while(q):
        x, y = q.popleft()
        for k in range(4):
            xd, yd = x+dx[k], y+dy[k]
            if 0<=xd<n and 0<=yd<n and v[xd][yd]==0 and (arr[xd][yd]==color or arr[xd][yd]==0):
                q.append((xd, yd))
                arr[xd][yd] = -2

def gravity(i, j):
    color = arr[i][j]
    x = i

    for k in range(i, n):
        if 0<=k+1<n and arr[k+1][j]==-2:
            x = k+1
        else: break

    if x>i:
        arr[i][j] = -2
        arr[x][j] = color

def rotate():
    global arr

    tmp = [[0 for _ in range(n)] for _ in range(n)]
    q = deque()

    for k in range(n):
        for i in range(n):
            q.append(arr[k][i])

        for i in range(n):
            x = q.pop()
            tmp[i][k] = x

    arr = tmp

while(True):
    mx = 2
    rainbows = 0
    biggest = [-1, -1]
    visited = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j]>0 and visited[i][j] == 0:
                visited[i][j] = 1
                bfs(i, j)

    if biggest[0] == -1: break

    break_bad(biggest[0], biggest[1])
    score += mx ** 2

    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if arr[i][j]>=0: gravity(i, j)

    rotate()

    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if arr[i][j]>=0: gravity(i, j)

print(score)
