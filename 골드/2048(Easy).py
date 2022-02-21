from sys import stdin
input = stdin.readline
from copy import deepcopy

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
score_max = -1

for i in range(n):
    for j in range(n):
        score_max = max(score_max, arr[i][j])

def moves(lst):
    if len(lst) == 5:
        moveit(lst, deepcopy(arr))
        return

    for i in range(1, 5):
        lst.append(i)
        moves(lst)
        del lst[-1]

def moveit(move, tmp):
    global score_max

    for mov in move:
        if mov == 1 or mov == 3:
            for i in range(n):
                if mov == 1: x, y, z, idx = 0, n, 1, 0
                else: x, y, z, idx = n-1, -1, -1, n-1
                visited = [[0 for _ in range(n)] for _ in range(n)]

                for j in range(x, y, z):
                    if mov == 1:
                        if tmp[i][j] != 0:
                            if idx < j:
                                tmp[i][idx] = tmp[i][j]
                                tmp[i][j] = 0

                            if idx > 0 and tmp[i][idx - 1] == tmp[i][idx] and visited[i][idx-1] == 0:
                                tmp[i][idx - 1] += tmp[i][idx]
                                tmp[i][idx] = 0
                                visited[i][idx-1] = 1
                            else: idx += 1
                    else:
                        if tmp[i][j] != 0:
                            if idx > j:
                                tmp[i][idx] = tmp[i][j]
                                tmp[i][j] = 0
                        
                            if idx < n-1 and tmp[i][idx] == tmp[i][idx+1] and visited[i][idx+1] == 0:
                                tmp[i][idx + 1] += tmp[i][idx]
                                tmp[i][idx] = 0
                                visited[i][idx+1] = 1
                            else: idx -= 1
        else:
            for i in range(n):
                if mov == 2: x, y, z, idx = 0, n, 1, 0
                else: x, y, z, idx = n-1, -1, -1, n-1
                visited = [[0 for _ in range(n)] for _ in range(n)]

                for j in range(x, y, z):
                    if mov == 2:
                        if tmp[j][i] != 0:
                            if idx < j:
                                tmp[idx][i] = tmp[j][i]
                                tmp[j][i] = 0

                            if idx > 0 and tmp[idx-1][i] == tmp[idx][i] and visited[idx-1][i] == 0:
                                tmp[idx-1][i] += tmp[idx][i]
                                tmp[idx][i] = 0
                                visited[idx-1][i] = 1
                            else: idx += 1
                    else:
                        if tmp[j][i] != 0:
                            if idx > j:
                                tmp[idx][i] = tmp[j][i]
                                tmp[j][i] = 0
                        
                            if idx < n-1 and tmp[idx][i] == tmp[idx+1][i] and visited[idx+1][i] == 0:
                                tmp[idx+1][i] += tmp[idx][i]
                                tmp[idx][i] = 0
                                visited[idx + 1][i] = 1
                            else: idx -= 1

    for a in range(n):
        score_max = max(score_max, max(tmp[a]))

moves([])

print(score_max)
