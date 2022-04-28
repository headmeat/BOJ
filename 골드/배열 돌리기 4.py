from sys import stdin
from collections import deque
from copy import deepcopy
input = stdin.readline

n,m,k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
rotation = []

def solve(lst):
    global ans

    if len(lst)==k:
        tmp = deepcopy(arr)

        for i in range(k):
            visited = [[0 for _ in range(m)] for _ in range(n)]
            r, c, s = rotation[lst[i]]
            spin(r-s-1, c-s-1, r+s, c+s, tmp, visited, 1)
            
        for i in range(n):
            ans = min(ans, sum(tmp[i]))

        return

    for i in range(k):
        if i not in lst:
            lst.append(i)
            solve(lst)
            del lst[-1]

def spin(x1, y1, x2, y2, tmp, visited, c):
    if x1 == x2-1 and y1 == y2-1:
        return

    q = deque()
    k = 0

    visited[x1][y1] = 1
    q.append((x1, y1, tmp[x1][y1]))

    while(q):
        i, j, v = q.popleft()

        while(k<4):
            if x1<=i+dx[k]<x2 and y1<=j+dy[k]<y2 and visited[i+dx[k]][j+dy[k]]==0:
                c += 1
                q.append((i+dx[k], j+dy[k], tmp[i+dx[k]][j+dy[k]]))
                visited[i+dx[k]][j+dy[k]]=c
                tmp[i+dx[k]][j+dy[k]] = v
                break
            k += 1
        
        if k==4: tmp[i+dx[3]][j+dy[3]] = v

    spin(x1+1, y1+1, x2-1, y2-1, tmp, visited, c)

    return

for _ in range(k):
    r, c, s = map(int, input().split())
    rotation.append((r, c, s))

ans = 5001

solve([])

print(ans)
