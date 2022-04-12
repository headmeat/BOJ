from sys import stdin
from collections import deque
input = stdin.readline

t = int(input())

for i in range(t):
    n, o = map(int, input().split())
    q = deque()
    arr = list(map(int, input().split()))

    for j in range(len(arr)):
        q.append((arr[j], j))
    
    mx = max(q, key=lambda x: x[0])[0]
    order = 1

    while(q):
        a, b = q.popleft()
        if a==mx: 
            if b==o:
                print(order)
                break
            order += 1
            mx = max(q, key=lambda x: x[0])[0]
        else: q.append((a, b))
