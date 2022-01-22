N = int(input())

nums = list((map(int, input().split())))
total = sum(nums)
sm = 0

for i in range(len(nums)):
    total -= nums[i]
    sm += nums[i] * total

print(sm)
