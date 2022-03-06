from sys import stdin
from collections import deque
input = stdin.readline

n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(v, visited, flag):
    visited[v[0]][v[1]] = flag
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
                visited[a[0]+dx[i]][a[1]+dy[i]] = flag
    
    value = sm // len(stack)
    borders = len(stack)-1

    while(stack):
        a, b = stack.pop()
        arr[a][b] = value

    return borders

count = 0

while(True):#1 day for each loop
    visited = [[0 for _ in range(n)] for _ in range(n)]
    flag = 0
    borders = 0

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                flag += 1
                borders += bfs((i, j), visited, flag)
    
    if borders == 0: break
    count += 1

print(count)
