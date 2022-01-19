N = int(input())
A = list(map(int, input().split()))
M, S = map(int, input().split())
sm = len(A)

for i in A:
    tmp = i - M
    if i - M > 0:
        sm += (i - M)//S
        if (i - M)%S != 0: sm += 1

print(sm)
