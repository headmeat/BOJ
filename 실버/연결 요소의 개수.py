from collections import deque
from sys import stdin

input = stdin.readline

def bfs(visited):
    queue = deque()
    cnt = 0

    while(sum(visited) != N):
        for i in range(1, len(visited)):
            if visited[i] == 0:
                cnt += 1
                visited[i] = 1
                queue.append(i)
                break
            
        while(queue):
            v = queue.popleft()
            
            for n in matrix[v]:
                if visited[n] == 0:
                    visited[n] = 1
                    queue.append(n)

    print(cnt)

N, M = map(int, input().split())
matrix = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())

    matrix[a].append(b)
    matrix[b].append(a)

bfs(visited)
