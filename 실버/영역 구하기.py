from sys import stdin
from collections import deque
input = stdin.readline

m, n, k = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
arr = [[0 for _ in range(n)] for _ in range(m)]

def bfs(start, arr):
    queue = deque()
    queue.append(start)
    arr[start[0]][start[1]] = 1
    cnt = 0

    while(queue):
        v = queue.popleft()

        cnt += 1

        for i in range(4):
            if 0<=v[0]+dx[i]<m and 0<=v[1]+dy[i]<n and arr[v[0]+dx[i]][v[1]+dy[i]] == 0:
                arr[v[0]+dx[i]][v[1]+dy[i]] = 1
                queue.append((v[0]+dx[i], v[1]+dy[i]))

    return cnt

for i in range(k):
    y1, x1, y2, x2 = map(int, input().split())

    for j in range(x1, x2):
        for k in range(y1, y2):
            arr[j][k] = 1

count = 0
ans = []

for j in range(m):
    for k in range(n):
        if arr[j][k] == 0:
            ans.append(bfs((j, k), arr))
            count += 1

print(count)
ans.sort()
print(" ".join(map(str, ans)))
