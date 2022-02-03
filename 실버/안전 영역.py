import sys
from copy import deepcopy
sys.setrecursionlimit(100000)

input = sys.stdin.readline

N = int(input())

arr = []
rain = -1
mn = 10 ** 15
dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]
mx = -1

def dfs(tmp, start, h):
    i, j = start[0], start[1]
    tmp[i][j] = -1

    for k in range(len(dx)):
        if i + dx[k] < N and i + dx[k] >= 0 and j + dy[k] < N and j + dy[k] >= 0:
            if tmp[i + dx[k]][j + dy[k]] > h:
                dfs(tmp, (i + dx[k], j + dy[k]), h)

    return

for _ in range(N):
    arr.append(list(map(int, input().split())))
    rain = max(max(arr[-1]), rain)
    mn = min(min(arr[-1]), mn)

for h in range(rain):
    cnt = 0
    tmp = deepcopy(arr)
    for i in range(N):
        for j in range(N):
            if tmp[i][j] > h:
                dfs(tmp, (i, j), h)
                cnt += 1
    mx = max(mx, cnt)

print(mx)
