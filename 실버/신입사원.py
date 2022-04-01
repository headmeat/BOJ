from sys import stdin
input = stdin.readline

t = int(input())

#최적화된 풀이
for i in range(t):
    n = int(input())
    arr = [0 for _ in range(n+1)]

    for j in range(n):
        a, b = map(int, input().split())
        arr[a] = b

    c = 0
    stand = 10**6

    for j in range(1, n+1):
        if arr[j] < stand:
            c += 1
            stand = min(stand, arr[j])

    print(c)

#내 첫 풀이
'''
for i in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    c = 0
    stand = [10**6, 10**6]
    arr.sort(key=lambda x: x[0])

    for j in arr:
        if j[0]<stand[0] or j[1]<stand[1]:
            c += 1
            stand = j

    print(c)
'''
