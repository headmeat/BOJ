from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
population = list(map(int, input().split()))
adj = [[] for _ in range(n)]
ans = 1001

for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(1, len(arr)):
        adj[i].append(arr[j]-1)

def check(flag, arr):
    start = -1

    for i in range(n):
        if arr[i]==flag:
            start = i
            break

    q = deque()
    q.append(start)
    visited = [0 for _ in range(n)]
    visited[start] = 1

    while(q):
        v = q.popleft()

        for k in adj[v]:
            if arr[k]==flag and visited[k]==0:
                q.append(k)
                visited[k] = 1

    for i in range(n):
        if arr[i]==flag and visited[i]==0:#플래그는 같지만 연결돼 있지 않다?
            return False
    
    return True

def solve(s, arr, c):
    if s==n:
        global ans
        if c==0 or c==n: return
        

        if check(0, arr) and check(1, arr):
            first = second = 0

            for i in range(n):
                if arr[i]==0: first+=population[i]
                else: second+= population[i]

            ans = min(ans, abs(first-second))

        return

    solve(s+1, arr, c)
    arr[s] = 1
    solve(s+1, arr, c+1)
    arr[s] = 0

solve(0, [0 for _ in range(n)], 0)

if ans==1001: print(-1)
else: print(ans)
