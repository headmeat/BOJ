from sys import stdin
from collections import deque
input = stdin.readline

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
score = 0
dice = [2, 4, 1, 3, 5, 6]
location = [0, 0]
dice_dir = 1
#북동남서 = 0123
direction = [[2, 1, 4, 3, 5, 0], [0, 5, 1, 2, 4, 3], [5, 1, 0, 3, 2, 4], [0, 2, 3, 5, 4, 1]]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def roll(to):
    global dice
    tmp = [0 for _ in range(6)]

    for i in range(len(direction[to])):
        tmp[i] = dice[direction[to][i]]

    dice = tmp

def bfs(x, y):
    q = deque()
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[x][y] = 1
    c = 0
    q.append((x, y))

    while(q):
        a, b = q.popleft()
        c += 1
        for p in range(4): 
            if 0<=a+dx[p]<n and 0<=b+dy[p]<m and arr[a+dx[p]][b+dy[p]]==arr[x][y] and visited[a+dx[p]][b+dy[p]]==0:
                visited[a+dx[p]][b+dy[p]] = 1
                q.append((a+dx[p], b+dy[p]))

    return c

def move():
    global score, dice_dir

    x, y = location

    if x+dx[dice_dir]<0 or x+dx[dice_dir]>=n or y+dy[dice_dir]<0 or y+dy[dice_dir]>=m:
        if dice_dir<=1: dice_dir += 2
        else: dice_dir -= 2

    x += dx[dice_dir]
    y += dy[dice_dir]
    
    roll(dice_dir)

    if dice[-1]>arr[x][y]:
        dice_dir = (dice_dir+1)%4
    elif dice[-1]<arr[x][y]:
        dice_dir -= 1
        if dice_dir<0: dice_dir = 3

    score += arr[x][y] * bfs(x, y)

    location[0], location[1] = x, y

for i in range(k):
    move()

print(score)
