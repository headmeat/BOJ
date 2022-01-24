N, M, K = map(int, input().split())

while(N/2 < M):
    M -= 1
    K -= 1

while(N > 2*M):
    N -= 1
    K -= 1

if K <= 0: print(int(M))
else: 
    while(True):
        if (K % 3) == 0: break
        K += 1
    print(int(M) - int(K/3))

"""
#새로운 풀이
N, M, K = map(int, input().split())
tmp = K

if N % 2 != 0: 
    N -= 1
    K -= 1

if N < 2 * M:
    K -= M - int(N / 2)
    M = int(N / 2)
elif N > 2 * M:
    K -= N - (2 * M)
    N = 2 * M

if K > 0:
    M -= K // 3
    if K % 3 != 0: M -=1

print(M)
"""
