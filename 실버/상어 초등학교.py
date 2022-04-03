from sys import stdin
input = stdin.readline

n = int(input())
arr = [[0 for _ in range(n**2+1)] for _ in range(n**2+1)]
room = [[0 for _ in range(n)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n**2):
    tmp = list(map(int, input().split()))
    i = tmp[0]
    for j in range(1, len(tmp)):
        arr[tmp[0]][tmp[j]] = 1

    lst = [[[0, 0] for _ in range(n)] for _ in range(n)]

    for j in range(n-1, -1, -1):
        for k in range(n-1, -1, -1):
            if room[j][k]>0: continue
            l = c = 0

            for d in range(4):
                if 0<=j+dx[d]<n and 0<=k+dy[d]<n:
                    if arr[i][room[j+dx[d]][k+dy[d]]] == 1: l += 1
                    elif room[j+dx[d]][k+dy[d]]==0: c += 1

            lst[j][k][0], lst[j][k][1] = l, c

    x = y = n-1

    for j in range(n-1, -1, -1):
        for k in range(n-1, -1, -1):
            if room[j][k]>0: continue
            if lst[j][k][0]==lst[x][y][0]:
                if lst[j][k][1]>=lst[x][y][1]:
                        x, y = j, k
            elif lst[j][k][0]>lst[x][y][0]:
                x, y = j, k

    room[x][y] = i

sm = 0

for i in range(n):
    for j in range(n):
        if room[i][j]==0: continue
        u = room[i][j]
        c = 0

        for d in range(4):
            if 0<=i+dx[d]<n and 0<=j+dy[d]<n:
                if arr[u][room[i+dx[d]][j+dy[d]]] == 1: c+=1

        sm += 10**(c-1) if c>0 else 0

print(sm)
