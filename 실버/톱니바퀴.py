from sys import stdin
from collections import deque
input = stdin.readline

status = [[int(x) for x in input().rstrip()] for _ in range(4)]
k = int(input())
rotation = [list(map(int, input().split())) for _ in range(k)]
#[right, left]
side = [[2, 6], [2, 6], [2, 6], [2, 6]]

for i in range(k):
    visited = [0 for _ in range(4)]
    visited[rotation[i][0]-1] = 1
    queue = deque()
    order = deque()
    queue.append(rotation[i][0]-1)

    while(queue):
        v = queue.popleft()
        order.append(v)

        if 0<=v-1 and visited[v-1] == 0:
            visited[v-1] = 1
            queue.append(v-1)
        if v+1<4 and visited[v+1] == 0:
            visited[v+1] = 1
            queue.append(v+1)
    
    visited = [0 for _ in range(4)]
    visited[rotation[i][0]-1] = 1

    #방향
    rotate = [0 for _ in range(4)]
    rotate[rotation[i][0]-1] = rotation[i][1]

    while(order):
        v = order.popleft()

        if rotate[v] != 0:
            if 0<=v-1 and visited[v-1]==0:
                visited[v-1] = 1
                if status[v-1][side[v-1][0]] != status[v][side[v][1]]:
                    rotate[v-1] = -rotate[v]

            if v+1<4 and visited[v+1]==0:
                visited[v+1] = 1
                if status[v+1][side[v+1][1]]!=status[v][side[v][0]]:
                    rotate[v+1] = -rotate[v]

    for i in range(4):
        side[i][0] = (side[i][0]-rotate[i])%8
        side[i][1] = (side[i][1]-rotate[i])%8
    
score = 0

for i in range(4):
    if status[i][(side[i][1]+2)%8] == 1:
        score += 2**(i)

print(score)
