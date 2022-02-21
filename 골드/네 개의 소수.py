from sys import stdin
input = stdin.readline

n = int(input())
primes = [0 for _ in range(n+1)]
primes[0] = primes[1] = 1
real_primes = []

def goldman(number):
    for i in real_primes:
        if number - i >= 2 and primes[number - i] == 0: return i, number-i

    return -1, -1

for i in range(2, int(n ** 0.5) + 1):
    if primes[i] == 1: continue
    for j in range(2*i, n+1, i):
        primes[j] = 1

for i in range(len(primes)):
    if primes[i] == 0: real_primes.append(i)

if n % 2 == 0:
    a, b = goldman(n-4)
    if a == -1 and b == -1: print(-1)
    else: print(2, 2, a, b)
else:
    a, b = goldman(n-5)
    if a == -1 and b == -1: print(-1)
    else: print(2, 3, a, b)
