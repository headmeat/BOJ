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
        days = v[2]

        if v[1]+1 < M and arr[v[0]][v[1]+1] == 0:
            cnt += 1
            arr[v[0]][v[1]+1] = 1
            queue.append((v[0], v[1]+1, days+1))
        if v[0]+1 < N and arr[v[0]+1][v[1]] == 0: 
            cnt += 1
            arr[v[0]+1][v[1]] = 1
            queue.append((v[0]+1, v[1], days+1))
        if v[0]-1 >= 0 and arr[v[0]-1][v[1]] == 0: 
            cnt += 1
            arr[v[0]-1][v[1]] = 1
            queue.append((v[0]-1, v[1], days+1))
        if v[1]-1 >= 0 and arr[v[0]][v[1]-1] == 0: 
            cnt += 1
            arr[v[0]][v[1]-1] = 1
            queue.append((v[0], v[1]-1, days+1))

    print(days if cnt == K else -1)

        

#N:가로, M:세로
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
K = 0
start = []

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == 0: K += 1
        elif arr[i][j] == 1: start.append((i, j, 0))

if K == 0:
    print(0)
    exit(0)

bfs(start)
