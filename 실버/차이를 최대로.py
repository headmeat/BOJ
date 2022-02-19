from sys import stdin
input = stdin.readline

n = int(input())
lst = list(map(int, input().split()))
mx = -10 ** 15

def solve(arr, sm):
    if len(arr) == n:
        global mx
        mx = max(mx, sm)
        return

    for i in range(n):
        if i not in arr:
            if len(arr) > 0:
                tmp = lst[arr[-1]]
                arr.append(i)
                solve(arr, sm + abs(tmp - lst[arr[-1]]))
                del arr[-1]
            else:
                arr.append(i)
                solve(arr, sm)
                del arr[-1]

solve([], 0)

print(mx)
