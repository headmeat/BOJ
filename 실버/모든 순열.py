from sys import stdin
input = stdin.readline

n = int(input())

def solve(arr):
    if len(arr) == n:
        print(" ".join(map(str, arr)))
        return

    for i in range(1, n+1):
        if i not in arr:
            arr.append(i)
            solve(arr)
            del arr[-1]

solve([])
