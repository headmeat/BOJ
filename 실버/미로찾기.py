from collections import deque
from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
arr = [[int(_) for _ in input().rstrip()] for _ in range(N)]
queue = deque()
cur = (0, 0, 1)
queue.append(cur)

while ( cur[0] != N-1 or cur[1] != M-1 ):
    cur = queue.popleft()
    x, y, step = cur[0], cur[1], cur[2]

    #우
    if y + 1 < M and arr[x][y+1] != 0:
        arr[x][y+1] = 0
        queue.append((x, y + 1, step + 1))
    #하
    if x + 1 < N and arr[x+1][y] != 0:
        arr[x+1][y] = 0
        queue.append((x + 1, y, step + 1))
    #좌
    if y - 1 >= 0 and arr[x][y-1] != 0:
        arr[x][y-1] = 0
        queue.append((x, y-1, step + 1))
    #상
    if x - 1 >= 0 and arr[x-1][y] != 0:
        arr[x-1][y] = 0
        queue.append((x - 1, y, step + 1))

print(cur[2])
