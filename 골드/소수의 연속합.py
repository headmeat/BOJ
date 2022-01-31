import sys
input = sys.stdin.readline

N = int(input())
l = h = sm = cnt = 0

primes = [0 for _ in range(N+1)]

primes[0] = primes[1] = -1

for i in range(2, int((N) ** 0.5) + 1):
    if primes[i] == -1: continue
    for j in range(i*2, N + 1, i):
        primes[j] = -1

tmp = primes
primes = []

for i in range(len(tmp)):
    if tmp[i] != -1: primes.append(i)

while ( True ):
    if sm < N and h < len(primes):
        sm += primes[h]
        h += 1
    elif l == len(primes): break
    else:
        sm -= primes[l]
        l += 1
    
    if sm == N: cnt += 1

print(cnt)
