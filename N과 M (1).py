N, M = map(int, input().split())

def solution(N, M, arr):
    if len(arr) == M:
        print(" ".join(map(str, arr)))

    for i in range(1, N+1):
        if i not in arr:
            arr.append(i)
            solution(N, M, arr)
            arr.remove(i)


solution(N, M, [])
