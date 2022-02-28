from sys import stdin
input = stdin.readline

n = int(input())
arr = []

for i in range(n):
    a, b = map(int, input().split())
    arr.append((i+1, a, b))

arr.sort(key = lambda x: -x[2]/x[1])

for i in range(n):
    print(arr[i][0], end = " ")
