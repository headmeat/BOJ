from collections import deque
from sys import stdin

input = stdin.readline

def bfs(start):
    days = 0
    queue = deque()
    for x in start: queue.append(x)
    cnt = 0

    while(queue):
        v = queue.popleft()
        days = v[3]

        if v[0]+1 < H and arr[v[0]+1][v[1]][v[2]] == 0:
            cnt += 1
            arr[v[0]+1][v[1]][v[2]] = 1
            queue.append((v[0]+1, v[1], v[2], days+1))
        if v[0]-1 >= 0 and arr[v[0]-1][v[1]][v[2]] == 0: 
            cnt += 1
            arr[v[0]-1][v[1]][v[2]] = 1
            queue.append((v[0]-1, v[1], v[2], days+1))
        if v[1]+1 < N and arr[v[0]][v[1]+1][v[2]] == 0: 
            cnt += 1
            arr[v[0]][v[1]+1][v[2]] = 1
            queue.append((v[0], v[1]+1, v[2], days+1))
        if v[1]-1 >= 0 and arr[v[0]][v[1]-1][v[2]] == 0: 
            cnt += 1
            arr[v[0]][v[1]-1][v[2]] = 1
            queue.append((v[0], v[1]-1, v[2], days+1))
        if v[2]+1 < M and arr[v[0]][v[1]][v[2]+1] == 0:
            cnt += 1
            arr[v[0]][v[1]][v[2]+1] = 1
            queue.append((v[0], v[1], v[2]+1, days+1))
        if v[2]-1 >= 0 and arr[v[0]][v[1]][v[2]-1] == 0:
            cnt += 1
            arr[v[0]][v[1]][v[2]-1] = 1
            queue.append((v[0], v[1], v[2]-1, days+1))

    print(days if cnt == K else -1)

#N:가로, M:세로
M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
K = 0

start = []
#i: Height, j: Row, k: Col
for i in range(len(arr)):
    for j in range(len(arr[0])):
        for k in range(len(arr[0][0])):
            if arr[i][j][k] == 0: K += 1
            elif arr[i][j][k] == 1: start.append((i, j, k, 0))
            
if K == 0:
    print(0)
    exit(0)

bfs(start)
