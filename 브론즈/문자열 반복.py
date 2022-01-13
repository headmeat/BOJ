N = int(input())

def iter(N, M, arr):
    if len(arr) == M:
        print(" ".join(map(str, arr)))
        return

    for i in range(1, N+1):
        if i not in arr:
            arr.append(i)
            iter(N, M, arr)
            arr.remove(i)

for i in range(N):
    L, S = input().split()
    L = int(L)

    for j in range(len(S)):
        print(S[j] * L, end = "")
    print()
