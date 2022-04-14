from sys import stdin
input = stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
x = y = n//2
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
d = 0
blow_x = [-1, 1, 1, -1, -1, 1, -2, 2, 0, 0]
blow_y = [1, 1, -1, -1, 0, 0, 0, 0, -2, -1]
percent = [1, 1, 10, 10, 7, 7, 2, 2, 5]
total = 0

for i in range(n):
    for j in range(n):
        total += arr[i][j]

def blow(a, b):
    sm = 0

    if d==0:
        for i in range(9):
            if 0<=a+blow_x[i]<n and 0<=b+blow_y[i]<n:
                arr[a+blow_x[i]][b+blow_y[i]] += (arr[a][b]*percent[i])//100
            sm += (arr[a][b]*percent[i])//100
        if 0<=a+blow_x[-1]<n and 0<=b+blow_y[-1]<n: arr[a+blow_x[-1]][b+blow_y[-1]] += arr[a][b] - sm
    elif d==2:
        for i in range(9):
            if 0<=a-blow_x[i]<n and 0<=b-blow_y[i]<n:
                arr[a-blow_x[i]][b-blow_y[i]] += (arr[a][b]*percent[i])//100
            sm += (arr[a][b]*percent[i])//100
        if 0<=a-blow_x[-1]<n and 0<=b-blow_y[-1]<n: arr[a-blow_x[-1]][b-blow_y[-1]] += arr[a][b] - sm
    elif d==1:
        for i in range(9):
            if 0<=a-blow_y[i]<n and 0<=b-blow_x[i]<n:
                arr[a-blow_y[i]][b-blow_x[i]] += (arr[a][b]*percent[i])//100
            sm += (arr[a][b]*percent[i])//100
        if 0<=a-blow_y[-1]<n and 0<=b-blow_x[-1]<n: arr[a-blow_y[-1]][b-blow_x[-1]] += arr[a][b] - sm
    else:
        for i in range(9):
            if 0<=a+blow_y[i]<n and 0<=b+blow_x[i]<n:
                arr[a+blow_y[i]][b+blow_x[i]] += (arr[a][b]*percent[i])//100
            sm += (arr[a][b]*percent[i])//100
        if 0<=a+blow_y[-1]<n and 0<=b+blow_x[-1]<n: arr[a+blow_y[-1]][b+blow_x[-1]] += arr[a][b] - sm

    arr[a][b] = 0

for k in range(1, n):
    for i in range(2):
        for j in range(k):
            x += dx[d]
            y += dy[d]
            blow(x, y)
        d = (d+1)%4

for j in range(n-1):
    x += dx[d]
    y += dy[d]
    blow(x, y)

for i in range(n):
    for j in range(n):
        total -= arr[i][j]

print(total)
