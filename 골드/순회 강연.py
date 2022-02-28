from sys import stdin
import heapq
input = stdin.readline

n = int(input())
q = []
days = {}
last_day = 0
profit = 0

for i in range(n):
    a, b = map(int, input().split())
    last_day = max(last_day, b)
    if b in days: days[b].append(a)
    else: days[b] = [a]

for i in range(last_day, 0, -1):
    if i in days.keys():
        for j in days[i]:
            heapq.heappush(q, -j)

    if len(q) != 0:
        profit -= heapq.heappop(q)

print(profit)
