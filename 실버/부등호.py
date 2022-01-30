import sys
input = sys.stdin.readline
N = int(input())
lst = list(input().split())
mn = 99999999999
mx = -1

def solve(arr, k):
    if len(arr) == k:
        cnt = 0
        for j in range(len(lst)):
            if lst[j] == '<':
                if arr[j] > arr[j+1]: 
                    cnt += 1
                    break
            else:
                if arr[j] < arr[j+1]: 
                    cnt += 1
                    break
        
        if cnt == 0:
            global mx, mn
            num = int("".join(map(str, arr)))
            mx = max(mx, num)
            mn = min(mn, num)
        return

    x, y = 0, 10
    if len(arr) >= 1:
        if lst[len(arr)-1] == '>':
            x, y = 0, arr[-1]
        else:
            x, y = arr[-1]+1, 10
    for i in range(x, y):
        if i not in arr:
            arr.append(i)
            solve(arr, k)
            del arr[-1]

solve([], N+1)
print(mx)
zero = "0"*(len(str(mx)) - len(str(mn)))
print(f"{zero}{str(mn)}")
