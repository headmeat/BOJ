from sys import stdin
from collections import deque
input = stdin.readline

arr = [[x for x in input().rstrip()] for _ in range(12)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def gravity():
    for i in range(10, -1, -1):#행
        for j in range(6):#열
            if arr[i][j]!="." and arr[i+1][j]==".":
                row = i+1

                for k in range(row+1, 12):
                    if arr[k][j] != ".": break
                    else: row = k

                arr[row][j] = arr[i][j]
                arr[i][j] = "."

def bfs(x, y):
    global visited

    q = deque()
    q.append((x, y))
    color = arr[x][y]
    visited[x][y] = 1
    stack = [(x, y)]

    while(q):
        a, b = q.popleft()

        for k in range(4):
            if 0<=a+dx[k]<12 and 0<=b+dy[k]<6 and visited[a+dx[k]][b+dy[k]]==0 and arr[a+dx[k]][b+dy[k]]==color:
                q.append((a+dx[k], b+dy[k]))
                visited[a+dx[k]][b+dy[k]] = 1
                stack.append((a+dx[k], b+dy[k]))

    if len(stack)>=4:
        while(stack):
            a, b = stack.pop()
            arr[a][b] = "."
        return True
    else: return False

cnt = 1
ans = 0

while(cnt):
    visited = [[0 for _ in range(6)] for _ in range(12)]
    cnt = 0

    for i in range(12):
        for j in range(6):
            if arr[i][j]!="." and visited[i][j]==0: 
                if bfs(i, j): cnt += 1

    gravity()

    if cnt>0: ans += 1

print(ans)
