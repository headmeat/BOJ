from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
size = [0 for _ in range(n)]

for i in range(n):
    size[i] = arr[i]

    if i>0 and size[i-1]+arr[i] > arr[i]:
        size[i] = arr[i] + size[i-1]

print(max(size))
