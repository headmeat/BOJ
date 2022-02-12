from sys import stdin
from collections import deque

input = stdin.readline
n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
res = [[0 for _ in range(len(arr[0]))] for _ in range(n)]

def solve(start):
    queue = deque()
    queue.append(start)
    visited = [0 for _ in range(n)]

    while(queue):
        v = queue.popleft()

        for j in range(n):
            if arr[v][j] == 1 and visited[j] == 0:
                queue.append(j)
                res[start][j] = 1
                visited[j] = 1

    return

for i in range(n):
    solve(i)

for i in range(len(res)):
    print(" ".join(map(str, res[i])))
