from sys import stdin
from collections import deque
input = stdin.readline

for _ in range(int(input())):
    x, y = map(int, input().split())
    if x==y: 
        print(0)
        continue

    distance = y - x
    ans = distance + 1
    n = 0

    while(n*(n+1)//2<=distance):
        tmp = distance - n*(n+1)//2

        if n*(n+1)//2<=tmp:
            add = tmp - n*(n+1)//2
            if 0<add<n: add = 1
            elif add==0: add = 0
            ans = min(ans, 2*n + add)

        if n-1>=0 and n*(n-1)//2<=tmp: 
            add = tmp - n*(n-1)//2
            if 0<add<n-1: add = 1
            elif add==0: add = 0
            ans = min(ans, 2*n - 1 + add)

        n += 1

    print(ans)
