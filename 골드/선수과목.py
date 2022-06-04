from sys import stdin
from collections import deque
from copy import deepcopy
input = stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
neighbors = [0 for _ in range(n)]
sem = [0 for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a-1].append(b-1)
    neighbors[b-1] += 1

q = deque([x for x in range(n)])

c = 1

while(q):
    updated_neighbors = [x for x in neighbors]
    tmp = deque()

    while(q):
        v = q.popleft()

        if neighbors[v] == 0: 
            sem[v] = c

            for k in adj[v]:
                updated_neighbors[k] -= 1
        else: tmp.append(v)

    q = tmp
    neighbors = [x for x in updated_neighbors]
    c += 1

print(" ".join(map(str, sem)))
