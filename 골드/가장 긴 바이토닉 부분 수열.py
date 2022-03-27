from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
lis = [1 for _ in range(n)]
lds = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i]>arr[j]:
            lis[i] = max(lis[i], lis[j] + 1)

for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if arr[i]>arr[j]:
            lds[i] = max(lds[i], lds[j]+1)

print(max([lds[i]+lis[i]-1 for i in range(n)]))
