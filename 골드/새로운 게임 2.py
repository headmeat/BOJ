from sys import stdin
from collections import deque
input = stdin.readline

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
real_map = [[[] for _ in range(n)] for _ in range(n)]
horse = [list(map(int, input().split())) for _ in range(k)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
count = 0

for i in range(k):
    for j in range(3):
        horse[i][j] -= 1
    real_map[horse[i][0]][horse[i][1]].append(i)

def move():
    for i in range(k):
        x, y, d = horse[i]
        idx = real_map[x][y].index(i)
        q = deque()

        if 0<=x+dx[d]<n and 0<=y+dy[d]<n and arr[x+dx[d]][y+dy[d]] != 2:
            for _ in range(idx, len(real_map[x][y])):
                h = real_map[x][y].pop()
                q.append(h)
                horse[h][0] += dx[d]
                horse[h][1] += dy[d]
            
            if arr[x+dx[d]][y+dy[d]] != 1: q.reverse()

            while(q):
                h = q.popleft()
                real_map[x+dx[d]][y+dy[d]].append(h)
            if len(real_map[x+dx[d]][y+dy[d]])>=4:
                print(count)
                exit(0)
        else:
            #방향 전환
            if d==0 or d==2: 
                horse[i][2] += 1
                d += 1
            else: 
                horse[i][2] -= 1
                d -= 1

            #이동(못할 경우 턴 패스)
            if 0<=x+dx[d]<n and 0<=y+dy[d]<n and arr[x+dx[d]][y+dy[d]] != 2:
                for _ in range(idx, len(real_map[x][y])):
                    h = real_map[x][y].pop()
                    q.append(h)
                    horse[h][0] += dx[d]
                    horse[h][1] += dy[d]

                if arr[x+dx[d]][y+dy[d]] != 1: q.reverse()

                while(q):
                    h = q.popleft()
                    real_map[x+dx[d]][y+dy[d]].append(h)

                if len(real_map[x+dx[d]][y+dy[d]])>=4:
                    print(count)
                    exit(0)

    return

for _ in range(1000):
    count += 1
    move()

print(-1)
