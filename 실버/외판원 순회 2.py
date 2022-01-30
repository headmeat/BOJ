import sys

N = int(input())
input = sys.stdin.readline

lst = [list(map(int, input().split())) for _ in range(N)]
mn = 10 ** 15

def solve(N, arr, hap):
    if len(arr) == N:
        if lst[arr[-1]][arr[0]] == 0: return
        
        global mn
        mn = min(mn, hap + lst[arr[-1]][arr[0]])
        return

    for i in range(N):
        if i not in arr:
            tmp = lst[arr[-1]][i]
            if tmp == 0: continue
            
            if hap + tmp > mn: continue

            hap += tmp
            arr.append(i)

            solve(N, arr, hap)

            del arr[-1]
            hap -= tmp

for i in range(N):
    solve(N, [i], 0)
if mn != 10 ** 15: print(mn)
else: print(0)
