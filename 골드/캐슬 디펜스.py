from sys import stdin
from collections import deque
input = stdin.readline

n, m, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)] + [[-1 for _ in range(m)]]
dx = [0, -1, 0]
dy = [-1, 0, 1]
dp = [[] for _ in range(m)]
ans = 0

def bfs(x, y, v):
    global d

    q = deque()
    visited = [[0 for _ in range(m)] for _ in range(n+1)]

    visited[x][y] = 1
    q.append((x, y))

    while(q):
        a, b = q.popleft()

        for i in range(3):
            if 0<=a+dx[i]<x and 0<=b+dy[i]<m and visited[a+dx[i]][b+dy[i]]==0:
                tmp_d = abs(x-(a+dx[i])) + abs(y-(b+dy[i]))
                if tmp_d>d: continue

                visited[a+dx[i]][b+dy[i]] = 1
                q.append((a+dx[i], b+dy[i]))

                if arr[a+dx[i]][b+dy[i]] == 1 and v[a+dx[i]][b+dy[i]] == 0: 
                    return (a+dx[i], b+dy[i])

    return -1

def solve(lst):
    global ans

    if len(lst)==3:
        v = [[0 for _ in range(m)] for _ in range(n)]
        kill = 0

        for k in range(n):
            stack = []

            for i in range(3):
                res = bfs(n-k, lst[i], v)
                if res==-1: continue
                stack.append(res)

            stack = list(set(stack))

            while(stack):
                a, b = stack.pop()
                v[a][b] = 1
                kill += 1

        ans = max(ans, kill)

        return

    for i in range(m):
        if i not in lst:
            lst.append(i)
            solve(lst)
            del lst[-1]

solve([])
print(ans)
