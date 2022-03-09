from sys import stdin
from collections import deque
from copy import deepcopy
input = stdin.readline

directions = [0 for _ in range(17)]
fish_locations = [0 for _ in range(17)]
best_eat = 0
lifeordeath = [1 for _ in range(17)]

#반시계 방향
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
    tmp = list(map(int, input().split()))
    
    for j in range(0, 8, 2):
        directions[tmp[j]] = tmp[j+1]-1
        fish_locations[tmp[j]] = [i, j//2]

def fish_move(fish_locations, shark, directions):
    for i in range(1, len(fish_locations)):
        fish = i
        x, y = fish_locations[i][0], fish_locations[i][1]

        if lifeordeath[i] == 0: continue

        for _ in range(8):
            move_x, move_y = x+dx[directions[fish]], y+dy[directions[fish]]

            if move_x<0 or move_x>=4 or move_y<0 or move_y>=4 or (shark[0] == move_x and shark[1] == move_y):
                directions[fish] = (directions[fish] + 1) % 8
                continue

            sw = 0

            #물고기가 있는 경우, 없는 경우
            for j in range(1, len(fish_locations)):
                if fish_locations[j][0] == move_x and fish_locations[j][1] == move_y and lifeordeath[j] == 1:
                    sw = j
                    break

            fish_locations[fish] = [move_x, move_y]

            if sw:#물고기가 있는 경우(스왑)
                fish_locations[sw] = [x, y]
            
            break

def shark_move(shark, shark_head, eat, fish_locations, direct, d):
    global lifeordeath
    fl = deepcopy(fish_locations)
    dr = deepcopy(direct)
    fish_move(fl, shark, dr)

    for i in range(1,4):
        x, y = shark[0]+dx[shark_head]*i, shark[1]+dy[shark_head]*i

        if x<0 or x>3 or y<0 or y>3: break

        for j in range(1, len(fl)):
            if fl[j][0] == x and fl[j][1] == y and lifeordeath[j] == 1:
                lifeordeath[j] = 0
                
                shark_move([x, y], dr[j], eat + j, fl, dr, d+1)

                lifeordeath[j] = 1

                break

    global best_eat
    best_eat = max(best_eat, eat)

shark = [0, 0]
shark_head = -1
eat = 0

for i in range(1, len(fish_locations)):
    if fish_locations[i][0] == 0 and fish_locations[i][1] == 0:
        shark_head = directions[i]
        eat += i
        lifeordeath[i] = 0

best_eat = eat
shark_move(shark, shark_head, eat, fish_locations, directions, 0)
print(best_eat)
