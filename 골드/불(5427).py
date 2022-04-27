from sys import stdin
from collections import deque
input = stdin.readline

t = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = []

def bfs(f):
    global location

    q = deque()
    q.append((location[0], location[1]))
    step = 0
    visited = [[0 for _ in range(w)] for _ in range(h)]
    visited[location[0]][location[1]] = 1

    for x, y in f:
        visited[x][y] = 1

    while(q):
        step += 1
        qs = len(q)
        fs = len(f)

        while(fs):
            a, b = f.popleft()

            for k in range(4):
                if 0<=a+dx[k]<len(arr) and 0<=b+dy[k]<len(arr[0]) and visited[a+dx[k]][b+dy[k]] == 0 and arr[a+dx[k]][b+dy[k]]!="#":
                    visited[a+dx[k]][b+dy[k]] = 1
                    f.append((a+dx[k], b+dy[k]))

            fs -= 1

        while(qs):
            a, b = q.popleft()
            
            for k in range(4):
                if a+dx[k]<0 or a+dx[k]>=h or b+dy[k]<0 or b+dy[k]>=w:
                    print(step)
                    return

                if 0<=a+dx[k]<h and 0<=b+dy[k]<w and visited[a+dx[k]][b+dy[k]]==0 and arr[a+dx[k]][b+dy[k]]!="*" and arr[a+dx[k]][b+dy[k]]!="#":
                    q.append((a+dx[k], b+dy[k]))
                    visited[a+dx[k]][b+dy[k]] = 1
            
            qs -= 1

    print("IMPOSSIBLE")

for _ in range(t):
    w, h = map(int, input().split())
    arr = [[x for x in input().rstrip()] for _ in range(h)]
    location = [-1, -1]
    fire = deque()

    for i in range(h):
        for j in range(w):
            if arr[i][j]=="@": location[0], location[1] = i, j
            elif arr[i][j]=="*": fire.append((i, j))

    bfs(fire)
