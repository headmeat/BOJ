from sys import stdin
input = stdin.readline

h, w = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

for i in range(1, w-1):
    curr = arr[i]
    l = r = 0
    for j in range(i):
        l = max(arr[j], l)
    for j in range(i+1, w):
        r = max(arr[j], r)

    tmp = min(l, r) - curr
    if tmp>0: ans += tmp

print(ans)
