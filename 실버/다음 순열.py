from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))

for i in range(n-1, 0, -1):
    if arr[i] > arr[i-1]:
        tmp = i
        for j in range(i+1, n):
            if arr[j] < arr[tmp] and arr[j] > arr[i-1]: tmp = j
        temp = arr[i-1]
        arr[i-1] = arr[tmp]
        arr[tmp] = temp
        print(" ".join(map(str, arr[:i] + sorted(arr[i:]))))
        exit(0)

print(-1)
