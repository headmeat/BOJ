from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
k = int(input())
#-1:사과, 0:없음, 1:뱀몸있음
arr = [[0 for _ in range(n)] for _ in range(n)]
apple = []

for i in range(k):
    x, y = map(int, input().split())
    arr[x-1][y-1] = -1

l = int(input())
move = []

for i in range(l):
    t, m = input().split()
    move.append((int(t), m))
move.reverse()

snake = deque()
snake.append((0, 0))
arr[0][0] = 1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
index = 0
time = 0
shift = move.pop()

while(True):
    if time == shift[0]:
        if shift[1] == "L":
            if index == 0: index = 3
            else: index -= 1
        else:
            if index == 3: index = 0
            else: index += 1
        
        if len(move) != 0:
            shift = move.pop()

    time += 1
    
    if len(snake) > 0 and 0<=snake[-1][0] + dx[index]<n and 0<=snake[-1][1] + dy[index]<n and arr[snake[-1][0]+dx[index]][snake[-1][1]+dy[index]] <= 0:
        x_tmp, y_tmp = snake[-1][0] + dx[index], snake[-1][1] + dy[index]

        if arr[snake[-1][0]+dx[index]][snake[-1][1]+dy[index]] != -1:
            tail = snake.popleft()
            arr[tail[0]][tail[1]] = 0

        snake.append((x_tmp, y_tmp))
        arr[x_tmp][y_tmp] = 1
    else: 
        break

print(time)
