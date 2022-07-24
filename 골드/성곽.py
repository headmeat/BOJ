from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
visited = [[0 for _ in range(n)] for _ in range(m)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cands = []

room = [0]
room_no = 1
ans = 0

def bfs(x, y):
    global room, room_no, ans, cands

    q = deque()
    q.append((x, y))
    visited[x][y] = room_no
    set_ = set()

    size = 0

    while(q):
        a, b = q.popleft()
        size += 1

        binary = ("0"*3 + bin(arr[a][b])[2:])[-4:]

        for k in range(4):
            if binary[k] == "1":
                if 0<=a+dx[k]<m and 0<=b+dy[k]<n and visited[a+dx[k]][b+dy[k]] != room_no and visited[a+dx[k]][b+dy[k]]!=0: set_.add(visited[a+dx[k]][b+dy[k]])
            elif 0<=a+dx[k]<m and 0<=b+dy[k]<n and visited[a+dx[k]][b+dy[k]] == 0:
                q.append((a+dx[k], b+dy[k]))
                visited[a+dx[k]][b+dy[k]] = room_no

    set_ = list(set_)

    for k in range(len(set_)):
        cands.append((room_no, set_[k]))

    room += [size]
    room_no += 1

for i in range(m):
    for j in range(n):
        if visited[i][j] == 0: bfs(i, j)

for i in range(len(cands)):
    a, b = cands[i]
    ans = max(ans, room[a]+room[b])

print(len(room)-1)
print(max(room))
print(ans)
