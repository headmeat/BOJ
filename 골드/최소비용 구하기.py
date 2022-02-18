from sys import stdin
import heapq
input = stdin.readline

INF = 10 ** 15
n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    adj[a].append((b, w))

start, end = map(int, input().split())

dist = [INF for _ in range(n+1)]
dist[start] = 0
queue = []

heapq.heappush(queue, (dist[start], start))

while(queue):
    distance, vertex = heapq.heappop(queue)

    if dist[vertex] < distance: continue

    for n, w in adj[vertex]:
        if distance + w < dist[n]:
            dist[n] = distance + w
            heapq.heappush(queue, (dist[n], n))

print(dist[end])
