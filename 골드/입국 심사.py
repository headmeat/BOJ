from sys import stdin
input = stdin.readline

n, m = map(int, input().split())

arr = [int(input().rstrip()) for _ in range(n)]

ans = 10**18

def solve(low, high):
    global ans
    if low>high: return

    tmp = m
    limit = (low+high)//2

    for i in range(len(arr)):
        tmp -= limit // arr[i]

    if tmp>0: solve(limit+1, high)
    elif tmp<=0: 
        ans = limit
        solve(low, limit-1)

    return

solve(0, 10**18)

print(ans)
