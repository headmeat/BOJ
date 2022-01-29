import sys

N = int(input())
arr = [0 for i in range(10001)]

for i in range(N):
    arr[int(sys.stdin.readline())] += 1
cnt = 0

for i in range(1, 10001):
    if arr[i] >= 1: 
        for j in range(arr[i]): sys.stdout.write("%d\n" % (i))
        cnt += 1
    if cnt == N: break
