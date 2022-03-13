from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
length = [0 for _ in range(n)]

for i in range(n):
    length[i] = 1
    for j in range(i):
        if arr[j]<arr[i]:
            length[i] = max(length[i], length[j]+1)

print(max(length))
