from sys import stdin
import heapq
input = stdin.readline

n = int(input())
mx = []
mn = []

first = int(input())
heapq.heappush(mx, -first)
print(first)

for _ in range(n-1):
    x = int(input())

    if len(mx)==len(mn): heapq.heappush(mx, -x)
    else: heapq.heappush(mn, x)

    if -mx[0]>mn[0]:
        a = -heapq.heappop(mx)
        b = heapq.heappop(mn)
        heapq.heappush(mx, -b)
        heapq.heappush(mn, a)

    print(-mx[0])
