from sys import stdin
input = stdin.readline

n = int(input())

def compare(arr):
    for i in range(3, len(arr), 2):
        s = len(arr) - i - 1
        e = i//2+1

        if "".join(map(str, arr[s:s+e])) == "".join(map(str, arr[s+e:])): return False

    return True

def dfs(arr):
    if len(arr)==n:
        print("".join(map(str, arr)))
        exit(0)

    for i in range(1, 4):
        if arr and arr[-1] == i: continue
        
        if compare(arr + [i]): dfs(arr + [i])

dfs([])
