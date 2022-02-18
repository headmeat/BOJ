from sys import stdin
import heapq
input = stdin.readline

INF = 10 ** 15
n, m, x = map(int, input().split())

adj = [[] for _ in range(n+1)]
rev = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    adj[a].append((b, w))
    rev[b].append((a, w))

dist = [INF for _ in range(n+1)]
rev_dist = [INF for _ in range(n+1)]
dist[x] = 0
queue = []

heapq.heappush(queue, (dist[x], x))

while(queue):
    distance, vertex = heapq.heappop(queue)

    if dist[vertex] < distance: continue

    for t, w in adj[vertex]:
        if distance + w < dist[t]:
            dist[t] = distance + w
            heapq.heappush(queue, (dist[t], t))

heapq.heappush(queue, (dist[x], x))

while(queue):
    distance, vertex = heapq.heappop(queue)

    if rev_dist[vertex] < distance: continue

    for t, w in rev[vertex]:
        if distance + w < rev_dist[t]:
            rev_dist[t] = distance + w
            heapq.heappush(queue, (rev_dist[t], t))

mx = -1
for i in range(1, n+1):
    mx = max(mx, dist[i] + rev_dist[i])

print(mx)
