from collections import deque

N = int(input())
arr = [[int(x) for x in input()] for _ in range(N)]

queue = deque()
start = (0, 0)
queue.append((0, 0))

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    arr[x][y] = 0
    cnt = 0
    while ( queue ):
        cur = queue.popleft()
        a, b = cur[0], cur[1]
        cnt += 1
        if a+1<N and arr[a+1][b] != 0:
            queue.append((a+1, b))
            arr[a+1][b] = 0
        if a-1>=0 and arr[a-1][b] != 0:
            queue.append((a-1, b))
            arr[a-1][b] = 0
        if b+1<N and arr[a][b+1] != 0:
            queue.append((a, b+1))
            arr[a][b+1] = 0
        if b-1>=0 and arr[a][b-1] != 0:
            queue.append((a, b-1))
            arr[a][b-1] = 0
    return cnt

res = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:     
            res.append(bfs(i, j))

print(len(res))
res.sort()

for _ in res: print(_)
