N = int(input())

def solve(N, arr):
    if len(arr) == 2:
        if arr[0] ** 2 - arr[1] ** 2 == N:
            global cnt
            cnt += 1
        return

    for i in range(1, 501):
        if i not in arr:
            arr.append(i)
            solve(N, arr)
            del arr[-1]

cnt = 0
solve(N, [])
print(cnt)
