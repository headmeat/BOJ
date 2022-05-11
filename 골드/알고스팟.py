import heapq
from sys import stdin
input = stdin.readline

m, n = map(int, input().split())
INF = 10**9
arr = [[int(x) for x in input().rstrip()] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

distance = [[INF for _ in range(m)] for _ in range(n)]

def dijkstra():
    global distance

    q = []
    distance[0][0] = 0
    heapq.heappush(q, (0, 0, 0))

    while(q):
        dist, x, y = heapq.heappop(q)

        if dist>distance[x][y]: continue

        for i in range(4):
            if 0<=x+dx[i]<n and 0<=y+dy[i]<m:
                if arr[x+dx[i]][y+dy[i]] == 0 and dist<distance[x+dx[i]][y+dy[i]]:
                    heapq.heappush(q, (dist, x+dx[i], y+dy[i]))
                    distance[x+dx[i]][y+dy[i]] = dist
                elif arr[x+dx[i]][y+dy[i]] == 1 and dist+1<distance[x+dx[i]][y+dy[i]]:
                    heapq.heappush(q, (dist+1, x+dx[i], y+dy[i]))
                    distance[x+dx[i]][y+dy[i]] = dist + 1

    return

dijkstra()
print(distance[n-1][m-1])
