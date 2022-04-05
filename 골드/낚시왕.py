from sys import stdin
input = stdin.readline

r, c, m = map(int, input().split())
sharks = [list(map(int, input().split())) for _ in range(m)]
arr = [[0 for _ in range(c)] for _ in range(r)]
death = [0 for _ in range(m)]
ans = 0

for i in range(m):
    sharks[i][0] -= 1
    sharks[i][1] -= 1
    sharks[i][3] -= 1

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def fisher(stand):
    global ans

    for i in range(r):
        if arr[i][stand]>0:
            no = arr[i][stand] - 1
            ans += sharks[no][4]
            death[no] = 1
            arr[i][stand] = 0
            return

def shark_moves():
    for i in range(m):
        if death[i]==1: continue
        x, y = sharks[i][0], sharks[i][1]
        if arr[x][y]==i+1: arr[x][y] = 0
        speed = sharks[i][2]
        d = sharks[i][3]

        if d == 0 or d == 1:
            speed %= ((r-1)*2)
        elif d == 2 or d == 3:
            speed %= ((c-1)*2)

        for _ in range(speed):
            if 0<=x+dx[d]<r and 0<=y+dy[d]<c:
                x += dx[d]
                y += dy[d]
            elif d == 0 or d == 2:
                d += 1
                x += dx[d]
                y += dy[d]
            else:
                d -= 1
                x += dx[d]
                y += dy[d]
        
        sharks[i][3] = d
        
        if arr[x][y]>0 and arr[x][y]<i+1:
            if sharks[i][4]>sharks[arr[x][y]-1][4]:
                death[arr[x][y]-1] = 1
                sharks[i][0] = x
                sharks[i][1] = y
                arr[x][y] = i+1
            else:
                death[i] = 1
        else:
            arr[x][y] = i+1
            sharks[i][0] = x
            sharks[i][1] = y

    return

for i in range(m):
    a, b = sharks[i][0], sharks[i][1]
    arr[a][b] = i+1

for i in range(c):
    fisher(i)
    shark_moves()

print(ans)
