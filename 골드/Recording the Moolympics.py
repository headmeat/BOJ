from sys import stdin
input = stdin.readline

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort(key = lambda x: (x[1], x[0]))
a, b = [(0, 0)], [(0, 0)]

for i in range(n):
    sw1 = a[-1][1]<=arr[i][0]
    sw2 = b[-1][1]<=arr[i][0]

    if sw1 and sw2:
        if arr[i][1] - a[-1][1] < arr[i][1] - b[-1][1]: a.append(arr[i])
        else: b.append(arr[i])
    elif sw1: a.append(arr[i])
    elif sw2: b.append(arr[i])

print(len(a)+len(b) - 2)
