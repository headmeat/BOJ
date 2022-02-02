N = int(input())

arr = list(map(int, input().split()))
tmp = sorted(arr)

for i in range(len(arr)):
    idx = tmp.index(arr[i])
    print(idx, end = " ")
    tmp[idx] = 10 * 4
