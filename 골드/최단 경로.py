from sys import stdin
import heapq

INF = 10 ** 15
N, M = map(int, input().split())
start = int(input())
adj = [[] for _ in range(N+1)]
dp = [INF for _ in range(N+1)]
dp[start] = 0

for _ in range(M):
    a, b, w = map(int, input().split())
    adj[a].append((b, w))

def djikstra(start):
    q = []
    heapq.heappush(q, (0, start))

    while( q ):
        w, n = heapq.heappop(q)
        if dp[n] < w: continue
        
        for i in adj[n]:
            cost = dp[n] +  i[1]
            if cost < dp[i[0]]:
                dp[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

djikstra(start)

for i in range(1, len(dp)):
    if dp[i] == INF: print("INF")
    else: print(dp[i])
