from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
binlist = []
ans = 0

def binary(x):
    if len(binlist)==0 or binlist[-1]<x:
        binlist.append(x)
        return

    l, r = 0, len(binlist)-1
    mid = (l+r)//2

    while(l<=r and mid<len(binlist)):
        if binlist[mid]==x: break
        elif binlist[mid]<x: l = mid + 1
        else: r = mid - 1

        mid = (l+r)//2

    if l == mid: binlist[l] = x
    elif r == mid: binlist[r + 1] = x

for i in range(n):
    binary(arr[i])
    ans = max(ans, len(binlist))

print(ans)
