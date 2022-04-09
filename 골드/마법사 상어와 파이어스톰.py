from sys import stdin
from collections import deque
input = stdin.readline

n, q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2**n)]
L = list(map(int, input().split()))
chunk = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global chunk, visited

    queue = deque()
    queue.append((x, y))
    count = 0

    while(queue):
        a, b = queue.popleft()
        count += 1

        for i in range(4):
            if 0<=a+dx[i]<2**n and 0<=b+dy[i]<2**n and visited[a+dx[i]][b+dy[i]]==0 and arr[a+dx[i]][b+dy[i]]>0:
                visited[a+dx[i]][b+dy[i]] = 1
                queue.append((a+dx[i], b+dy[i]))

    chunk = max(chunk, count)


for l in L:
    for i in range(2**l, 2**n+1, 2**l):
        for j in range(2**l, 2**n+1, 2**l):
            tmp = deque()

            for k in range(j - 2**l, j, 1):
                for m in range(i-1, i - 2**l - 1, -1):
                    tmp.append(arr[m][k])

            for k in range(i-2**l, i, 1):
                for m in range(j-2**l, j, 1):
                    arr[k][m] = tmp.popleft()

    melt = [x[:] for x in arr]

    for i in range(2**n):
        for j in range(2**n):
            if arr[i][j] <= 0: continue
            c = 0

            for k in range(4):
                if 0<=i+dx[k]<2**n and 0<=j+dy[k]<2**n and arr[i+dx[k]][j+dy[k]]>0:
                    c += 1
            
            if c<3: melt[i][j] = arr[i][j] - 1
            else: melt[i][j] = arr[i][j]
    
    arr = melt

sm = 0
for i in range(2**n):
    sm += sum(arr[i])

print(sm)

visited = [[0 for _ in range(2**n)] for _ in range(2**n)]

for i in range(2**n):
    for j in range(2**n):
        if arr[i][j]>0 and visited[i][j]==0:
            visited[i][j] = 1
            bfs(i, j)

print(chunk)
