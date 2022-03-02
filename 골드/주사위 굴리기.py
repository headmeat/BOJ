from sys import stdin
from collections import deque
input = stdin.readline

n, m, x, y, k = map(int, input().split())
dice = [0 for _ in range(6)]

#위북동서남아
rotate = [[4, 2, 1, 6, 5, 3], [3, 2, 6, 1, 5, 4], [2, 6, 3, 4, 1, 5], [5, 1, 3, 4, 6, 2]]

arr = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for move in order:
    if 0<=x + dx[move-1]<n and 0<=y+dy[move-1]<m:
        x += dx[move-1]
        y += dy[move-1]
    else: continue

    tmp = list(dice)

    for i in range(6):
        dice[i] = tmp[rotate[move-1][i]-1]

    if arr[x][y] == 0:
        arr[x][y] = dice[-1]
    else:
        dice[-1] = arr[x][y]
        arr[x][y] = 0
    
    print(dice[0])
