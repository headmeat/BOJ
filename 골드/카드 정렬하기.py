from sys import stdin
import heapq
input = stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
heapq.heapify(arr)
ans = 0

while(len(arr)>1):
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)

    ans += a + b
    heapq.heappush(arr, a + b)

print(ans)
