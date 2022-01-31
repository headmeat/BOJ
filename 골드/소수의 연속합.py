import sys
input = sys.stdin.readline

N = int(input())
l = h = sm = cnt = 0

primes = [1 for _ in range(N+1)]

primes[0] = primes[1] = 0

for i in range(2, int((N) ** 0.5) + 1):
    if primes[i] == 0: continue
    for j in range(i*2, N + 1, i):
        primes[j] = 0

tmp = primes
primes = []

for i in range(2, len(tmp)):
    if tmp[i] != 0: primes.append(i)

length = len(primes)

while ( True ):
    if sm < N and h < length:
        sm += primes[h]
        h += 1
    elif l == length: break
    else:
        sm -= primes[l]
        l += 1
    
    if sm == N: cnt += 1

print(cnt)
