from sys import stdin
from collections import deque
input = stdin.readline

q = deque()

n, k = map(int, input().split())
idx = k

for i in range(1, n+1):
    q.append(i)

print("<", end="")
while(q):
    v = q.popleft()
    idx -= 1
    if idx==0:
        idx = k
        if len(q)>0: print(v, end=", ")
        else: print(v, end="")
    else:
        q.append(v)

print(">")
