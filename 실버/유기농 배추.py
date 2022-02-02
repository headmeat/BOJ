from collections import deque
from sys import stdin

input = stdin.readline

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while(queue):
        tmp = queue.popleft()
        a, b = tmp[0], tmp[1]

        if b+1 < N and arr[a][b+1] != 0: 
            queue.append((a, b+1))
            arr[a][b+1] = 0
        if a+1 < M and arr[a+1][b] != 0: 
            queue.append((a+1, b))
            arr[a+1][b] = 0
        if a-1 >= 0 and arr[a-1][b] != 0: 
            queue.append((a-1, b))
            arr[a-1][b] = 0
        if b-1 >= 0 and arr[a][b-1] != 0: 
            queue.append((a, b-1))
            arr[a][b-1] = 0

T = int(input())

for _ in range(T):
    #M:가로, N:세로, K:배추개수
    M, N, K = map(int, input().split())

    arr = [[0 for _ in range(N)] for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input().split())
        arr[x][y] = 1

    cnt = 0

    for i in range(M):
        for j in range(N):
            if arr[i][j] == 1:
                bfs(i, j)
                cnt += 1

    print(cnt)
