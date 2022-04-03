from sys import stdin
input = stdin.readline

def cd(x):
    if x>=0:
        x%=n
    elif x<-n:
        while(x<-n):
            x += n
    
    return x

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

points = [x for x in range(n)]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
visited = [[0 for _ in range(n)] for _ in range(n)]
clouds = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n-2, n, 1):
    for j in range(0, 2, 1):
        clouds[i][j] = 1

for i in range(m):
    d, s = map(int, input().split())

    for j in range(n):
        for k in range(n):
            if clouds[j][k]==1:
                clouds[j][k] = 0
                arr[cd(j+dx[d-1]*s)][cd(k+dy[d-1]*s)] += 1
                visited[cd(j+dx[d-1]*s)][cd(k+dy[d-1]*s)] = 1

    for j in range(n):
        for k in range(n):
            if visited[j][k]==0: continue

            for z in range(1,8,2):
                if 0<=j+dx[z]<n and 0<=k+dy[z]<n and arr[j+dx[z]][k+dy[z]]>0:
                    arr[j][k] += 1

    for j in range(n):
        for k in range(n):
            if visited[j][k]==1 or arr[j][k]<2:
                visited[j][k] = 0
                continue
            arr[j][k] -= 2
            clouds[j][k] = 1

print(sum([sum(x) for x in arr]))
