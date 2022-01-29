N = int(input())
arr = [0 for i in range(2000002)]

for i in range(N):
    arr[int(input())] = 1
cnt = 0

for i in range(-1000000, 1000001):
    if cnt == N: break
    if arr[i] == 1: 
        print(i)
        cnt += 1
