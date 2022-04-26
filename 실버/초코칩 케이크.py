from sys import stdin
from collections import deque
input = stdin.readline

n, q = map(int, input().split())
max_r = 0
max_c = 0
row = [0 for _ in range(n)]
col = [0 for _ in range(n)]
dp_r = [0 for _ in range(100001)]
dp_c = [0 for _ in range(100001)]
dp_r[0] = dp_c[0] = n

for _ in range(q):
    t, a = map(int, input().split())

    if t==1:
        row[a-1] += 1
        dp_r[row[a-1]] += 1
        max_r = max(max_r, row[a-1])
    else:
        col[a-1] += 1
        dp_c[col[a-1]] += 1
        max_c = max(max_c, col[a-1])

    print(dp_r[max_r]*dp_c[max_c])
