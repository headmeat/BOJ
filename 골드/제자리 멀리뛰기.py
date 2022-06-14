from sys import stdin
input = stdin.readline

d, n, m = map(int, input().split())
rocks = []

for i in range(n): rocks.append(int(input()))
rocks.sort()
rocks = [0] + rocks + [d]
distance = []
ans = 0

for i in range(1, len(rocks)):
    distance.append(rocks[i]-rocks[i-1])

def check(mid):
    global ans

    mn = d+1
    sm = 0
    tmp_m = m

    for i in range(len(distance)):
        if sm + distance[i]<mid:
            sm += distance[i]
            tmp_m -= 1
        else:
            mn = min(sm + distance[i], mn)
            sm = 0

    if sm>0: mn = min(sm, mn)
    if mn==mid and tmp_m>=0: ans = max(ans, mid)

    return tmp_m>=0

l, r = 0, d

while(l<=r):
    mid = (l+r)//2

    if check(mid): 
        l = mid + 1
    else: r = mid - 1

print(ans)
