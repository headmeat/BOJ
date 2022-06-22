from sys import stdin
input = stdin.readline

t = int(input())
nn = 10**7
primes = [1 for _ in range(nn)]
p = []

for i in range(2, int(len(primes)**0.5)+1):
    if primes[i] == 0: continue
    for j in range(i*2, len(primes), i):
        primes[j] = 0

sieve = [*range(1, nn, 2)]

for p in range(3, int(nn**0.5)+1, 2):
    if sieve[p//2]:
        sieve[p*p//2::p] = [0] * ((nn - p * p)//(2 * p) + 1)
p = [2] + [p for p in sieve if p]

for pp in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    tmp = [set() for _ in range(n)]
    
    for window in range(n):
        l, h = 0, arr[window]-1
        sm = sum(p[l:h])

        while(h<len(p)):
            sm += p[h]
            
            if sm>10**7: break
            if primes[sm] == 1: tmp[window].add(sm)
            sm -= p[l]
            h += 1
            l += 1

    ans = tmp[0]

    for i in range(1, n):
        ans = ans & tmp[i]

    if ans:
        print("Scenario {0}:\n{1}".format(pp+1, min(list(ans))))
        print()연속하는 소수의 합
