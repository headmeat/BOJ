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
        idx = 0

        for a in range(n):
            for b in range(m):
                if lst[a][b] == "#": continue

                if 1<=lst[a][b]<=5:
                    for c in directions[cam[idx]][arr[idx]]:
                        if c == 0:
                            for d in range(a-1, -1, -1):
                                if lst[d][b] == 6: break
                                if lst[d][b] == 0: s.add((d, b))
                        elif c == 1:
                            for d in range(b+1, m):
                                if lst[a][d] == 6: break
                                if lst[a][d] == 0: s.add((a, d))
                        elif c == 2:
                            for d in range(a+1, n):
                                if lst[d][b] == 6: break
                                if lst[d][b] == 0: s.add((d, b))
                        else:
                            for d in range(b-1, -1, -1):
                                if lst[a][d] == 6: break
                                if lst[a][d] == 0: s.add((a, d))

                    idx += 1

        square_spots = min(square_spots, spots - len(s))
        return

    for r in range(4):
        if (cam[i] == 1 and r > 1) or (cam[i]==4 and r>0): break
        arr.append(r)
        solve(i+1, cam, arr)
        del arr[-1]

k = 0
spots = 0
cam = []

for i in range(n):
    for j in range(m):
        if 1<=lst[i][j]<=5: 
            k += 1
            cam.append(lst[i][j]-1)
        elif lst[i][j] == 0: spots += 1

solve(0, cam, [])

print(square_spots)
