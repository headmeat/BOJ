from sys import stdin

input = stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

first = [[0, 0, 0, 0],[0, 1, 2, 3]]
second = [[0, 1, 0, 1], [0, 0, 1, 1]]
third = [[0, 1, 2, 2], [0, 0, 0, 1]]
fourth = [[0, 1, 1, 2], [0, 0, 1, 1]]
fifth = [[0, 0, 0, 1], [0, -1, 1, 0]]
coords = [first, second, third, fourth, fifth]
mx = -1

def solve(x, y):
    global mx
    poss = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
    
    for coord in coords:
        a, b = 0, 1
        for i in range(2):
            for k in range(len(poss)):
                sw = True
                sm = 0

                for i in range(len(coord[0])):
                    dx, dy = coord[a][i], coord[b][i]
                    if (x + dx*poss[k][0] < N) and (x + dx*poss[k][0] >= 0) and (y + dy*poss[k][1] < M) and (y + dy*poss[k][1] >= 0):
                        sm += arr[x+dx*poss[k][0]][y+dy*poss[k][1]]
                    else:
                        sw = False
                        break
                if sw == True: mx = max(mx, sm)

            a, b = 1, 0

for i in range(len(arr)):
    for j in range(len(arr[0])):
        solve(i, j)

print(mx)
