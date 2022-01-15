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
