from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
noo = [0]
cand = {0:1}
ans = 0

for i in range(n): noo.append(noo[-1]+arr[i])

for i in range(1, n+1):
    num = noo[i]
    
    ans += cand[num-k] if num-k in cand.keys() else 0
    if num not in cand.keys(): cand[num] = 1
    else: cand[num] += 1

print(ans)
