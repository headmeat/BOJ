from itertools import combinations

T = int(input())

for i in range(T):
    N = int(input())
    mn = 10 ** 15

    arr = [tuple((map(int, input().split()))) for _ in range(N)]

    for combs in list(combinations([i for i in range(N)], N//2)):
        x, y = 0, 0
        for j in range(N):
            if j in combs:
                x += arr[j][0]
                y += arr[j][1]
            else:
                x -= arr[j][0]
                y -= arr[j][1]
        tmp = (x ** 2 + y ** 2) ** 0.5

        mn = min(mn, tmp)
    print(mn)
