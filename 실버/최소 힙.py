from sys import stdin
import heapq
input = stdin.readline

n = int(input())
q = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if len(q)==0: print(0)
        else: print(heapq.heappop(q))
    else:
        heapq.heappush(q, x)
