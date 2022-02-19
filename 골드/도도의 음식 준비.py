from sys import stdin
input = stdin.readline

n, k, c = map(int, input().split())
a = list(map(int, input().split()))
therighttime = 10 ** 13

def findTime():
    left, right = 1, 10 ** 12
    mid = (left + right) // 2

    while(left <= right):
        sm = 0

        for i in a:
            sm += mid // i

        if sm >= k: 
            global therighttime
            therighttime = min(therighttime, mid)
            right = mid - 1
        else: left = mid + 1

        mid = (left + right) // 2

    return

def solve(t, count):
    findTime()

    if count == c: return

    for i in range(t, n):
        if a[i] > 1:
            a[i] -= 1
            solve(i, count + 1)
            a[i] += 1

solve(0, 0)
print(therighttime)
