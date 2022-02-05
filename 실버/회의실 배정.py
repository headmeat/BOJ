from sys import stdin
input = stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

arr.sort(key=lambda x: (x[1], x[0], x[1]-x[0]))
prev = arr[0]

for i in range(1, len(arr)):
    if arr[i][0] >= prev[1]:
        cnt += 1
        prev = arr[i]

print(cnt+1)
