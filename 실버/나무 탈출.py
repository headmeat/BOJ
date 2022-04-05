import sys
sys.setrecursionlimit(5*(10**5))
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

depths = 0

def dfs(v, d):
    global visited, depths
    c = 0

    for i in adj[v]:
        if visited[i]==0:
            c += 1
            visited[i] = 1
            dfs(i, d+1)

    if c == 0: depths += d

visited[1] = 1
dfs(1, 0)

print("Yes" if depths%2==1 else "No")
