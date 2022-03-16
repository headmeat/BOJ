from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    dp[i][i]=1

    if i<n-1 and arr[i]==arr[i+1]:
        dp[i][i+1]=1
    
for gap in range(2, n):
    for i in range(n):
        if i+gap<n:
            if dp[i+1][i+gap-1]==1:
                if arr[i]==arr[i+gap]:
                    dp[i][i+gap]=1
        else: break

m=int(input())

for i in range(m):
    a, b=map(int,input().split())

    print(dp[a-1][b-1])
