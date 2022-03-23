from sys import stdin
input = stdin.readline

n = int(input())
prev = [0]

for i in range(n):
    curr = list(map(int, input().split()))

    for j in range(len(curr)):
        cand1 = cand2 = -1

        if j-1>=0:
            cand1 = prev[j-1]
        if 0<=j<len(prev):
            cand2 = prev[j]
        
        curr[j] += max(cand1, cand2)
    
    prev = curr

print(max(prev))

'''
#DFS 풀이 방식

from sys import stdin
input = stdin.readline

n = int(input())
arr = []
dp = []

for _ in range(n):
    arr.append(list(map(int, input().split())))
    dp.append([0]*len(arr[_]))

def solve(i, j):
    if i>=n or j>i:
        return 0

    if dp[i][j] != 0:
        return dp[i][j]

    dp[i][j] = arr[i][j] + max(solve(i+1, j), solve(i+1, j+1))

    return dp[i][j]

print(solve(0, 0))
'''
