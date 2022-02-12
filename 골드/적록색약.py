from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
colors = [[x for x in input().rstrip()] for _ in range(n)]

def bfs(point, sekmeng):
    color = [colors[point[0]][point[1]]]
    queue = deque()
    queue.append(point)

    if sekmeng == 1 and color[0] == "R": 
        color.append("G")
    elif sekmeng == 1 and color[0] == "G":
        color.append("R")

    while(queue):
        v = queue.popleft()

        if v[0] + 1 < n and arr[v[0] + 1][v[1]] != -1 and colors[v[0] + 1][v[1]] in color:
            queue.append((v[0]+1, v[1]))
            arr[v[0]+1][v[1]] = -1
        if v[0] - 1 >= 0 and arr[v[0] - 1][v[1]] != -1 and colors[v[0] - 1][v[1]] in color:
            queue.append((v[0]-1, v[1]))
            arr[v[0]-1][v[1]] = -1
        if v[1] + 1 < n and arr[v[0]][v[1] + 1] != -1 and colors[v[0]][v[1] + 1] in color:
            queue.append((v[0], v[1]+1))
            arr[v[0]][v[1]+1] = -1
        if v[1] - 1 >= 0 and arr[v[0]][v[1] - 1] != -1 and colors[v[0]][v[1] - 1] in color:
            queue.append((v[0], v[1]-1))
            arr[v[0]][v[1]-1] = -1

    return

cnt = 0

arr = [[0 for _ in range(len(colors[0]))] for _ in range(n)]
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == 0:
            bfs((i, j), 0)
            cnt += 1

print(cnt, end = " ")
cnt = 0

arr = [[0 for _ in range(len(colors[0]))] for _ in range(n)]
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == 0:
            bfs((i, j), 1)
            cnt += 1

print(cnt)
