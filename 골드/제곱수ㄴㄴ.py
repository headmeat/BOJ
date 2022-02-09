from math import log
from sys import stdin

input = stdin.readline
mn, mx = map(int, input().split())
real_max = 1000001000000
arr = [0 for _ in range(int(mx ** 0.5) + 1)]
arr[0] = -1
arr[1] = -1
cnt = 0
primes = []
arr2 = [0 for _ in range(mx - mn + 2)]

for i in range(2, int(len(arr) ** 0.5) + 1):
    if arr[i] == -1: continue

    for j in range(2*i, len(arr), i):
        arr[j] = -1

for i in range(len(arr)):
    if arr[i] == -1: continue
    primes.append(i)

for i in range(len(primes)):
    tmp = primes[i] ** 2
    rem = mn // tmp
    tmp = (rem if mn % tmp == 0 else (rem + 1)) * tmp

    for j in range(tmp, mx + 1, primes[i] ** 2):
        arr2[j-mn] = 1
        cnt += 1

print(mx - mn - sum(arr2) + 1)
