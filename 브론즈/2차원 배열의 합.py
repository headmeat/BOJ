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
#
