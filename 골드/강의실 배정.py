from sys import stdin
import heapq
input = stdin.readline

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: (x[0], x[1]))
q = []
heapq.heappush(q, arr[0][1])

for i in range(1, n):
    s, t = arr[i]
    v = heapq.heappop(q)
    if s>=v: heapq.heappush(q, t)
    else: 
        heapq.heappush(q, v)
        heapq.heappush(q, t)

print(len(q))
