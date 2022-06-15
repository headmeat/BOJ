from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
m = int(input())
adj = []
tour = [[0 for _ in range(n)] for _ in range(n)]

def bfs(start):
    q = deque()
    visited = [0 for _ in range(n)]
    visited[start] = 1
    tour[start][start] = 1
    q.append(start)

    while(q):
        v = q.popleft()

        for neighbor in adj[v]:
            if visited[neighbor]==0:
                q.append(neighbor)
                tour[start][neighbor] = 1
                visited[neighbor] = 1

for i in range(n):
    neighbors = list(map(int, input().split()))

    adj.append([x for x in range(len(neighbors)) if neighbors[x]])

route = list(map(int, input().split()))

for i in range(n):
    bfs(i)

for i in range(1, len(route)):
    if tour[route[i-1]-1][route[i]-1]==0:
        print("NO")
        exit(0)

print("YES")
