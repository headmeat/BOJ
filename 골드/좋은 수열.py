from sys import stdin
input = stdin.readline

n = int(input())

def dfs(arr):
    if len(arr)==n:
        print("".join(map(str, arr)))
        exit(0)

    for i in range(1, 4):
        if arr and arr[-1] == i: continue

        arr = arr + [i]
        sw = True

        for j in range(3, len(arr), 2):
            s = len(arr) - j - 1
            e = j//2+1

            if arr[s:s+e] == arr[s+e:]:
                sw = False
                break
        
        if sw: dfs(arr)
        del arr[-1]

dfs([])
