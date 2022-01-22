N = int(input())

nums = list(map(int, input().split()))
sm = 0
k = 0
for i in nums:
    if i == 1:
        k += 1
        sm += k
    else: k = 0

print(sm)
