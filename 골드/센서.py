from sys import stdin
input = stdin.readline

n = int(input())
k = int(input())

arr = list(map(int, input().split()))
d = []

arr.sort()

for i in range(n-1):
    d += [arr[i+1] - arr[i]]

d.sort()

for _ in range(k-1): 
    if d: d.pop()

print(sum(d))
