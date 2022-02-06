N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
house = []
chicken = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1: house.append((i, j))
        elif arr[i][j] == 2: chicken.append((i, j))

total_min = 10 ** 15

def solve(i, arr):
    if i == len(arr):
        if sum(arr) == M:
            distance = 0

            for h in house:
                mn = 10 ** 15
                for c in range(len(arr)):
                    if arr[c] == 0: continue

                    mn = min(mn, abs(h[0] - chicken[c][0]) + abs(h[1] - chicken[c][1]))

                distance += mn
            global total_min
            total_min = min(total_min, distance)

        return

    arr[i] = 0
    solve(i+1, arr)
    arr[i] = 1
    solve(i+1, arr)

solve(0, [0 for _ in range(len(chicken))])

print(total_min)
