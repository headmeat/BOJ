from sys import stdin
from collections import deque
input = stdin.readline

t = int(input())

for _ in range(t):
    string = input().rstrip()
    k = int(input())
    short = [10001 for _ in range(26)]
    long = [0 for _ in range(26)]
    arr = [deque() for _ in range(26)]

    for i in range(len(string)):
        order = ord(string[i]) - 97
        arr[order].append(i)

        if len(arr[order]) == k:
            short[order] = min(short[order], arr[order][-1] - arr[order][0] + 1)
            long[order] = max(long[order], arr[order][-1] - arr[order][0] + 1)
            arr[order].popleft()

    if min(short)<10001: print(min(short), max(long))
    else: print(-1)
