from sys import stdin
input = stdin.readline

r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
machine = -1
upper_dir = [3, 0, 2, 1]
lower_dir = [3, 1, 2, 0]

for i in range(r):
    if arr[i][0]==-1:
        machine = i
        break

def munji():
    global r, c, arr

    spread = [x[:] for x in arr]
    for i in range(r):
        for j in range(c):
            if arr[i][j]>4:
                count = 0

                for k in range(4):
                    a, b = i+dx[k], j+dy[k]
                    if 0<=a<r and 0<=b<c and arr[a][b]!=-1:
                        count += 1

                for k in range(4):
                    a, b = i+dx[k], j+dy[k]
                    if 0<=a<r and 0<=b<c and arr[a][b]!=-1:
                        spread[a][b] += arr[i][j]//5

                spread[i][j] -= (arr[i][j]//5)*count

    arr = spread

def filter():
    upper = [machine, 0]
    lower = [machine+1, 0]
    idx = 0
    prev = 0

    while(idx<4):
        upper[0] += dx[upper_dir[idx]]
        upper[1] += dy[upper_dir[idx]]

        while(0<=upper[0]<r and 0<=upper[1]<c and arr[upper[0]][upper[1]]!=-1):
            curr = arr[upper[0]][upper[1]]
            arr[upper[0]][upper[1]] = prev
            prev = curr
            upper[0] += dx[upper_dir[idx]]
            upper[1] += dy[upper_dir[idx]]

        upper[0] -= dx[upper_dir[idx]]
        upper[1] -= dy[upper_dir[idx]]
        idx += 1

    idx = 0
    prev = 0

    while(idx<4):
        lower[0] += dx[lower_dir[idx]]
        lower[1] += dy[lower_dir[idx]]

        while(0<=lower[0]<r and 0<=lower[1]<c and arr[lower[0]][lower[1]]!=-1):
            curr = arr[lower[0]][lower[1]]
            arr[lower[0]][lower[1]] = prev
            prev = curr
            lower[0] += dx[lower_dir[idx]]
            lower[1] += dy[lower_dir[idx]]
        
        lower[0] -= dx[lower_dir[idx]]
        lower[1] -= dy[lower_dir[idx]]
        idx += 1

for i in range(t):
    munji()
    filter()

print(sum([sum(arr[i]) for i in range(r)])+2)
