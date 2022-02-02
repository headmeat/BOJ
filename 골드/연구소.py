from collections import deque
from sys import stdin
from copy import deepcopy

input = stdin.readline


def solve(N, lst):
    if len(lst) == 3:
        first, second, third = res[lst[0]], res[lst[1]], res[lst[2]]

        if arr[first[0]][first[1]] == 0:
            arr[first[0]][first[1]] = 1
        else: return

        if arr[second[0]][second[1]] == 0:
            arr[second[0]][second[1]] = 1
        else: return

        if arr[third[0]][third[1]] == 0:
            arr[third[0]][third[1]] = 1
        else: return

        tmp = deepcopy(arr)
        bfs(tmp)
        
        arr[first[0]][first[1]] = 0
        arr[second[0]][second[1]] = 0
        arr[third[0]][third[1]] = 0

        return

    for i in range(N):
        tmp = -1
        if len(lst) >= 1: tmp = lst[-1]
        if i < tmp: continue

        if i not in lst:
            lst.append(i)
            solve(N, lst)
            del lst[-1]

def bfs(arr):
    queue = deque()
    for _ in range(len(virus)): queue.append(virus[_])
    cnt = 0

    while(queue):
        v = queue.popleft()

        if v[0] + 1 < N and arr[v[0] + 1][v[1]] == 0:
            queue.append((v[0] + 1, v[1]))
            arr[v[0] + 1][v[1]] = 2
            cnt += 1
        if v[0] - 1 >= 0 and arr[v[0] - 1][v[1]] == 0:
            queue.append((v[0] - 1, v[1]))
            arr[v[0] - 1][v[1]] = 2
            cnt += 1
        if v[1] + 1 < M and arr[v[0]][v[1] + 1] == 0:
            queue.append((v[0], v[1] + 1))
            arr[v[0]][v[1] + 1] = 2
            cnt += 1
        if v[1] - 1 >= 0 and arr[v[0]][v[1] - 1] == 0:
            queue.append((v[0], v[1] - 1))
            arr[v[0]][v[1] - 1] = 2
            cnt += 1

    global mx
    mx = max(mx, K - cnt - 3)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
virus = []
K = 0
res = []

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == 0: 
            res.append((i, j))
            K += 1
        if arr[i][j] == 2: virus.append((i, j))

mx = -1

solve(len(res), [])

print(mx)
