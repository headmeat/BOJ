from collections import deque
from sys import stdin
input = stdin.readline

n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(v):
    visited[v[0]][v[1]] = 1
    stack = [v]
    queue = deque()
    queue.append(v)
    sm = arr[v[0]][v[1]]

    while(queue):
        a = queue.popleft()

        for i in range(4):
            x, y = a[0]+dx[i], a[1]+dy[i]

            if 0<=x<n and 0<=y<n and visited[x][y] == 0 and l<=abs(arr[a[0]][a[1]] - arr[x][y])<=r:
                queue.append((x, y))
                sm += arr[x][y]
                stack.append((x, y))
                visited[x][y] = 1
    
    borders = len(stack)
    value = sm // borders

    if len(stack)>1:
        while(stack):
            a, b = stack.pop()
            arr[a][b] = value
            jwapyo.append((a, b))

    return borders-1

count = 0
jwapyo = deque()

for i in range(n):
    for j in range(0 if i%2==0 else 1, n, 2):
        jwapyo.append((i, j%n))

while(count<=2000):#1 day for each loop
    visited = [[0 for _ in range(n)] for _ in range(n)]
    borders = 0

    for i in range(len(jwapyo)):
        i, j = jwapyo.popleft()
        if visited[i][j] == 0:
            borders += bfs((i, j))

    if borders == 0: break
    count += 1

print(count)
