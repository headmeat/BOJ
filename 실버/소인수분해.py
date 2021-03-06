N = int(input())

lst = [0 for i in range(N+1)]
lst[0] = lst[1] = -1 #0과 1은 소수에서 제외
primes = []

i = 2
mx = int(N ** 0.5) + 1

while N != 1:
    if N % i == 0:
        print(i)
        N = int(N / i)
        i = 2
    else:
        if i < mx: i += 1
        else: 
            print(N)
            break

"""
#초기 풀이
N = int(input())

lst = [0 for i in range(N+1)]
lst[0] = lst[1] = -1 #0과 1은 소수에서 제외
primes = []

for i in range(2, int(N ** 0.5) + 1):
    for j in range(2*i, N+1, i):
        lst[j] = -1

for i in range(len(lst)):
    if lst[i] != -1: primes.append(i)

idx = 0

while(N != 1):
    if N % primes[idx] == 0:
        print(primes[idx])
        N /= primes[idx]
        idx = 0
    else: idx += 1
"""
