from collections import deque

N = int(input())
E = int(input())
edges = [[] for _ in range(N+1)]
visited = [0 for i in range(N+1)]

for _ in range(E):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

def bfs(start, edges):
    visited[start] = 1
    queue = deque()
    queue.append(start)
    cnt = 0

    while(queue):
        start = queue.popleft()
        for neighbor in edges[start]:
            if visited[neighbor] != 1:
                visited[neighbor] = 1
                queue.append(neighbor)
                cnt += 1

    print(cnt)

for e in edges:
    e.sort()

bfs(1, edges)
