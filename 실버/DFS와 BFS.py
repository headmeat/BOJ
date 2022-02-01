#효율적인 코드
from collections import deque
import sys

input = sys.stdin.readline

N, M, V = map(int, input().split())
res = []
board = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = list(map(int, input().split()))
    board[a].append(b)
    board[b].append(a)

def bfs(start, edges, visited):
    res2 = []
    queue = deque()
    queue.append(start)
    visited[start] = 1

    while(len(queue)!=0):
        start = queue.popleft()
        res2.append(start)
        for neighbor in edges[start]:
            if visited[neighbor] != 1:
                queue.append(neighbor)
                visited[neighbor] = 1
    return res2

def dfs(start, edges, visited):
    global res
    res.append(start)
    visited[start] = 1
    for neighbor in edges[start]:
        if visited[neighbor] != 1:
            dfs(neighbor, edges, visited)

    return res

visited = [0 for i in range(N+1)]

for i in range(len(board)):
    board[i].sort()

print(" ".join(map(str, dfs(V, board, list(visited)))))

print(" ".join(map(str, bfs(V, board, list(visited)))))

#내가 풀었던 코드
"""
from collections import deque

N, M, V = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(M)]
def sorting(arr):
    for i in arr:
        if i[0] > i[1]:
            tmp = i[0]
            i[0] = i[1]
            i[1] = tmp

def bfs(start, edges, visited):
    queue = deque()
    queue.append(start)

    while(len(queue)!=0):
        start = queue.popleft()
        print(start, end = " ")
        for edge in edges:
            if start in edge:
                neighbor = sum(edge) - start
                if visited[neighbor] != 1:
                    queue.append(neighbor)
                    visited[neighbor] = 1

def dfs(start, edges, visited): 
    print(start, end=" ")
    for edge in edges:
        if start in edge:
            neighbor = sum(edge) - start
            if visited[neighbor] != 1:
                visited[neighbor] = 1
                dfs(neighbor, edges, visited)

visited = [0 for i in range(N+1)]
sorting(arr)
arr.sort(key = lambda x: (x[0], x[1]))
visited[V] = 1
dfs(V, arr, visited)

print()

visited = [0 for i in range(N+1)]
sorting(arr)
arr.sort(key = lambda x: (x[0], x[1]))
visited[V] = 1
bfs(V, arr, visited)
"""
