from sys import stdin
input = stdin.readline

n, m, K = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
trees = [list(map(int, input().split())) for _ in range(m)]
arr = [[5 for _ in range(n)] for _ in range(n)]
containers = [[[] for _ in range(n)] for _ in range(n)]

dx = [-1, 0, 1, 0, -1, 1, -1, 1]
dy = [0, -1, 0, 1, -1, 1, 1, -1]

trees.sort(key=lambda x:-x[2])

for i in range(len(trees)):
    containers[trees[i][0]-1][trees[i][1]-1].append(trees[i][2])

for i in range(K):
    for j in range(n):
        for k in range(n):
            dead = -1

            for h in range(len(containers[j][k])-1, -1, -1):
                if arr[j][k] >= containers[j][k][h]:
                    arr[j][k] -= containers[j][k][h]
                    containers[j][k][h] += 1
                else:
                    dead = h
                    break

            for h in range(dead, -1, -1):
                arr[j][k] += containers[j][k][h]//2
                del containers[j][k][h]

    for j in range(n):
        for k in range(n):
            arr[j][k] += a[j][k]

            for h in range(len(containers[j][k])-1, -1, -1):
                if containers[j][k][h] % 5 == 0:
                    for tt in range(8):
                        if 0<=j+dx[tt]<n and 0<=k+dy[tt]<n:
                            containers[j+dx[tt]][k+dy[tt]].append(1)

count = 0

for i in range(n):
    for j in range(n):
        for k in containers[i][j]:
            if k > 0: count += 1

print(count)
