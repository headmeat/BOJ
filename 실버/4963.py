from sys import stdin
from collections import deque
input = stdin.readline

def bfs(start):
    dx = [-1,-1,0,1,1,1,0,-1]
    dy = [0,1,1,1,0,-1,-1,-1]
    queue = deque()
    queue.append(start)

    while( queue ):
        v = queue.popleft()

        for i in range(8):
            if v[0] + dx[i] >= 0 and v[0] + dx[i] < h and v[1] + dy[i] >= 0 and v[1] + dy[i] < w:
                if mp[v[0] + dx[i]][v[1]+dy[i]] == 1:
                    mp[v[0] + dx[i]][v[1]+dy[i]] = 0
                    queue.append((v[0]+dx[i], v[1]+dy[i]))

while(True):
    w, h = map(int, input().split())
    if w == 0 and h == 0: break
    mp = []
    cnt = 0

    for _ in range(h):
        mp.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if mp[i][j] == 1:
                bfs((i, j))
                cnt += 1
    print(cnt)
