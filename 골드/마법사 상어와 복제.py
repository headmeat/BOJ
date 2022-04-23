from sys import stdin
from collections import deque
from copy import deepcopy
input = stdin.readline

'''
전역 변수
m, s, dx, dy, arr, tmp
'''

m, s = map(int, input().split())
fish = [list(map(int, input().split())) for _ in range(m)]
shark = list(map(int, input().split()))
shark[0] -= 1
shark[1] -= 1
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
shark_x = [-1, 0, 1, 0]
shark_y = [0, -1, 0, 1]
number = [0, 1, 2, 3, 4, 5, 6, 7]
arr = [[[] for _ in range(4)] for _ in range(4)]
smell = [[0 for _ in range(4)] for _ in range(4)]

for i in range(m):
    x, y, d = fish[i]
    arr[x-1][y-1].append(d-1)

def fish_move():
    global arr
    res = [[[] for _ in range(4)] for _ in range(4)]

    for i in range(4):
        for j in range(4):
            while(arr[i][j]):
                direction_of_fish = arr[i][j].pop()
                sw = True

                for k in range(8):
                    tmp_x, tmp_y = i+dx[direction_of_fish-k], j+dy[direction_of_fish-k]

                    if 0<=tmp_x<4 and 0<=tmp_y<4 and smell[tmp_x][tmp_y]==0 and (shark[0]!=tmp_x or shark[1]!=tmp_y):
                        res[tmp_x][tmp_y].append(number[direction_of_fish-k])
                        sw = False
                        break
                
                if sw: res[i][j].append(direction_of_fish)

    arr = res

    return

def shark_move(x, y, depth):#DFS
    global max_move_of_shark, eat_fishes, shark
    
    if len(depth)==3:

        test = 0
        visited = [[0 for _ in range(4)] for _ in range(4)]
        a, b = shark

        for i in depth:
            move = int(i)

            a += shark_x[move]
            b += shark_y[move]

            if visited[a][b] == 0:
                test += len(arr[a][b])
                visited[a][b] = 1

        if test>eat_fishes:
            max_move_of_shark = depth
            eat_fishes = test

        return

    for i in range(4):
        if 0<=x+shark_x[i]<4 and 0<=y+shark_y[i]<4:
            shark_move(x+shark_x[i], y+shark_y[i], depth + str(i))

    return

for _ in range(s):
    tmp = deepcopy(arr)

    fish_move()#2) 물고기 이동

    max_move_of_shark = "1000"
    eat_fishes = -1
    shark_move(shark[0], shark[1], "")
    
    for j in max_move_of_shark:
        move = int(j)
        shark[0] += shark_x[move]
        shark[1] += shark_y[move]

        if arr[shark[0]][shark[1]]:#에러
            smell[shark[0]][shark[1]] = 3
            arr[shark[0]][shark[1]] = []

    for i in range(4):
        for j in range(4):
            if smell[i][j]: smell[i][j] -= 1

    for i in range(4):
        for j in range(4):
            while(tmp[i][j]):
                arr[i][j].append(tmp[i][j].pop())

sm = 0

for i in range(4):
    for j in range(4):
        sm += len(arr[i][j])

print(sm)
