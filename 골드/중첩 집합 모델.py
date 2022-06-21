import sys
sys.setrecursionlimit(10**6)
from sys import stdin
input = stdin.readline

n = int(input())
adj = [[] for _ in range(n)]
ans = [[] for _ in range(n)]

def dfs(x, l):
    left = l
    tmp = left + 1
    visited[x] = 1
    
    for neighbor in adj[x]:
        if visited[neighbor]==0: 
            tmp = dfs(neighbor, tmp)

    right = tmp

    ans[x].append(left)
    ans[x].append(right)

    return right + 1
    
for _ in range(n):
    tmp = list(map(int, input().split()))

    adj[tmp[0]-1] = [int(x)-1 for x in tmp[1:] if x!=-1]
    adj[tmp[0]-1].sort()

root = int(input())-1

visited = [0 for _ in range(n)]

dfs(root, 1)

for i in range(n): print(str(i+1)+" "+" ".join(map(str, ans[i])))
