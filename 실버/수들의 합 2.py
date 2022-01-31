import sys
input = sys.stdin.readline

N, S = map(int, input().split())
l = h = sm = cnt = 0
arr = list(map(int, input().split()))
sm += arr[0]

while ( l < N ):
    tmp = 0
    if sm < S:
        tmp = 1
        if h < N-1: 
            h += 1
            sm += arr[h]
        else: #l += 1
            break
    else:
        tmp = 2
        if sm == S: cnt += 1
        if l < h: 
            sm -= arr[l]
            l += 1
        else: 
            if h < N-1:
                h += 1
                sm += arr[h]
            else: break

print(cnt)

#좀 더 정리된 답안
"""
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
l = h = sm = cnt = 0
arr = list(map(int, input().split()))

while ( True ):
    if sm < S and h < N:
        sm += arr[h]
        h += 1
    elif l == N: break
    else:
        sm -= arr[l]
        l += 1
    
    if sm == S: cnt += 1

print(cnt)
"""
