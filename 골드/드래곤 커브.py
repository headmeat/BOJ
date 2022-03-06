from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
dragon = [list(map(int, input().split())) for _ in range(n)]
arr = [[False for _ in range(101)] for _ in range(101)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def dragonize(start, dir, gen):
    movements = []
    cur = start

    arr[cur[0]][cur[1]] = True
    arr[cur[0]+dx[dir]][cur[1]+dy[dir]] = True
    cur[0], cur[1] = cur[0]+dx[dir], cur[1]+dy[dir]

    movements.append(dir)

    for i in range(gen):
        next = []

        for j in movements:
            next.append((((j+3)%4)+2)%4)
        
        next.reverse()

        for j in next:
            cur[0], cur[1] = cur[0]+dx[j], cur[1]+dy[j]

            arr[cur[0]][cur[1]] = True
            movements.append(j)

    return

for x, y, d, g in dragon:
    dragonize([y, x], d, g)

count = 0

for i in range(101):
    for j in range(101):
        if arr[i][j] == True:
            if j+1<=100 and arr[i][j+1] == True:
                if i+1<=100 and arr[i+1][j] == True:
                    if arr[i+1][j+1] == True:
                        count += 1

print(count)
