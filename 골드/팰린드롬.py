from sys import stdin
input = stdin.readline

arr = [x for x in input().rstrip()]
n = len(arr)
dp = [[0 for _ in range(n)] for _ in range(n)]
pal = [10**15 for _ in range(n)]

for i in range(n):
    dp[i][i] = 1
    if i+1<n and arr[i] == arr[i+1]: dp[i][i+1] = 1

for i in range(2, n):
    for j in range(n):
        if j+i<n:
            if dp[j+1][j+i-1] == 1 and arr[j] == arr[j+i]:
                dp[j][j+i] = 1
        else: break

for k in range(n):
    for i in range(k+1):
        if dp[i][k]==1:
            if i-1>=0: pal[k]=min(pal[k], min(pal[i-1]+1, pal[k-1]+1))
            else: pal[k] = 1

print(pal[-1])
