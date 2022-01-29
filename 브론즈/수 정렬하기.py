N = int(input())
arr = [0 for i in range(2002)]

for i in range(N):
    arr[int(input())] = 1
cnt = 0

for i in range(-1000, 1001):
    if cnt == N: break
    if arr[i] == 1: 
        print(i)
        cnt += 1
