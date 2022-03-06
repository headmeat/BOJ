from sys import stdin
input = stdin.readline

n, m, h = map(int, input().split())
pipes = [[0 for _ in range(n)] for _ in range(h+1)]
minimum = 4
location = []

for i in range(m):
    a, b = map(int, input().split())
    pipes[a][b] = 1

for i in range(1, h+1):
    for j in range(1, n):
        if pipes[i][j-1] == 0 and pipes[i][j] == 0 and (pipes[i][j+1] == 0 if j+1<n else True):
            location.append((i, j))

def solve(c, maximal, last):
    if c==maximal:
        if goDown():
            print(maximal)
            exit(0)
        return

    for i in range(last+1, len(location)):
        pipes[location[i][0]][location[i][1]] = 1
        solve(c+1, maximal, i)
        pipes[location[i][0]][location[i][1]] = 0

def goDown():
    for l in range(1, n+1):
        start = l

        for i in range(1, h+1):
            if start<n and pipes[i][start] == 1:
                start += 1
            elif start>1 and pipes[i][start-1] == 1:
                start -= 1
    
        if start != l: return False

    return True

for i in range(0, 4):
    maximal = i
    solve(0, maximal, -1)

print(-1)
