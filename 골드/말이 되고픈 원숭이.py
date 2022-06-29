from sys import stdin
from collections import deque
input = stdin.readline

k = int(input())
w, h = map(int, input().split())
INF = 10**5
dx = [-1, 1, 0, 0, -2, -2, -1, -1, 1, 1, 2, 2]
dy = [0, 0, -1, 1, -1, 1, -2, 2, -2, 2, -1, 1]

arr = [list(map(int, input().split())) for _ in range(h)]

def bfs():
    global visited

    q = deque()
    visited[0][0][k] = 1
    q.append((0, 0, k, 0))
    ans = INF

    while(q):
        a, b, c, d = q.popleft()

        if a==h-1 and b==w-1:
            ans = min(ans, d)

        for i in range(12):
            if i>3 and c==0: break
            tmp = c-1 if i>3 else c

            if 0<=a+dx[i]<h and 0<=b+dy[i]<w and visited[a+dx[i]][b+dy[i]][tmp]==0 and arr[a+dx[i]][b+dy[i]]==0:
                visited[a+dx[i]][b+dy[i]][tmp] = 1
                q.append((a+dx[i], b+dy[i], tmp, d+1))

    return ans

visited = [[[0 for _ in range(k+1)] for _ in range(w)] for _ in range(h)]
ans = bfs()
print(ans if ans<INF else -1)
