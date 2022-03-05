from sys import stdin
from collections import deque
from copy import deepcopy
input = stdin.readline

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
directions = [ [[0], [1], [2], [3]], [[0, 2], [1,3]], [[0,1], [1,2], [2,3], [0,3]], [[0, 1, 3], [0, 1, 2], [1, 2, 3], [0, 2, 3]], [[0, 1, 2, 3]]]
square_spots = 10 ** 15

#북동남서
#0 1 2 3 (0는 방향 무관함을 의미.)

def solve(i, cam, arr):
    if len(arr) == len(cam):
        global square_spots
        s = set()

        for a in range(len(cam)):
            x, y = cam[a][0], cam[a][1]

            for c in directions[lst[x][y]-1][arr[a]]:
                if c == 0:
                    for d in range(x-1, -1, -1):
                        if lst[d][y] == 6: break
                        if lst[d][y] == 0: s.add((d, y))
                elif c == 1:
                    for d in range(y+1, m):
                        if lst[x][d] == 6: break
                        if lst[x][d] == 0: s.add((x, d))
                elif c == 2:
                    for d in range(x+1, n):
                        if lst[d][y] == 6: break
                        if lst[d][y] == 0: s.add((d, y))
                else:
                    for d in range(y-1, -1, -1):
                        if lst[x][d] == 6: break
                        if lst[x][d] == 0: s.add((x, d))

        square_spots = min(square_spots, spots - len(s))
        return
    
    camera = lst[cam[i][0]][cam[i][1]]

    for r in range(len(directions[camera-1])):
        arr.append(r)
        solve(i+1, cam, arr)
        del arr[-1]

spots = 0
cam = []

for i in range(n):
    for j in range(m):
        if 1<=lst[i][j]<=5: 
            cam.append((i, j))
        elif lst[i][j] == 0: spots += 1

solve(0, cam, [])

print(square_spots)
