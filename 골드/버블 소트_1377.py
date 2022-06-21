from sys import stdin
input = stdin.readline

n, ans = int(input()), 1
arr = [(int(input()), i) for i in range(n)]
arr.sort(key=lambda x: (x[0], x[1]))

print(max([arr[i][1]-i+1 for i in range(n)]))
