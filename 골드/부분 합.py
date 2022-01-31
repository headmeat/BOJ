import sys
input = sys.stdin.readline

N, S = map(int, input().split())
l = h = sm = cnt = 0
arr = list(map(int, input().split()))
mn = 10 ** 15

while ( True ):
    if sm < S and h < N:
        sm += arr[h]
        h += 1
    elif l == N: break
    else:
        sm -= arr[l]
        l += 1
    
    if sm >= S: mn = min(mn, h - l)

if mn != 10 ** 15: print(mn)
else: print(0)
