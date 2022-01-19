M, N = map(int, input().split())

lst = [x for x in range(N+1)]
lst[0] = -1
lst[1] = -1

for i in range(2, int(N**0.5)+1):
    for j in range(i*2, N+1, i):
        lst[j] = -1

for i in range(M, N+1):
    if lst[i] != -1: print(i)
