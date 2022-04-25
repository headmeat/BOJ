from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
sm = total = 0

for i in range(n-1):
    arr[i] %= (10**9+7)
    sm = sm*arr[i] + arr[i]
    sm %= (10**9+7)
    total += sm
    total %= (10**9+7)

print(total%(10**9+7))
