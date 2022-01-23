N, M = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
T = int(input())
idxs = [list(map(int, input().split())) for i in range(T)]
noo = [[0 for i in range(M + 1)] for i in range(N + 1)]

for i in range(1, len(noo)):
    noo[i][1] = arr[i-1][0]
    for j in range(2, len(noo[0])):
        noo[i][j] = noo[i][j-1] + arr[i-1][j-1]

for i in range(1, len(noo)):
    for j in range(len(noo[0])):
        noo[i][j] += noo[i-1][j]

for idx in idxs:
    i, j, x, y = map(int, idx)
    print(noo[x][y] - noo[i-1][y] - noo[x][j-1] + noo[i-1][j-1])

#아래는 첫 풀이. 복기용으로 남김.    
"""
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]

sm = 0
noo = []

for i in range(len(arr[0])):
    for j in range(len(arr)):
        sm += arr[j][i]
        noo.append(sm)

T = int(input())

idxs = [list(map(lambda x: x-1, map(int, input().split()))) for i in range(T)]

for idx in idxs:
    i, j, x, y = map(int, idx)

    print("I,J", (i*len(arr[0])) + (j))
    print("X,Y", (x*len(arr[0])) + (y))
    print("SQR1,2", noo[(x*len(arr[0])) + y], noo[(i*len(arr[0])) + j])
    print(noo[(x*len(arr[0])) + y] - noo[(i*len(arr[0])) + j])
"""
