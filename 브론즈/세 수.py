from sys import stdin
input = stdin.readline

nums = list(map(int, input().split()))

#(i,j) == (0, 2) or (2, 0)
def solve(i, j):
    if i == 1:
        print("뭐하는데 시발")
        exit(0)

    if nums[i] + nums[1] == nums[j]:
        return "+"
    if nums[i] * nums[1] == nums[j]:
        return "*"
    if i < j:
        if nums[i]/nums[1] == nums[j]:
            return "/"
        if nums[i] - nums[1] == nums[j]:
            return "-"
    else:
        if nums[1]/nums[i] == nums[j]:
            return "/"
        if nums[1] - nums[i] == nums[j]:
            return "-"

    return "꼬추"

first = solve(0, 2)
second = solve(2, 0)
if first != "꼬추": print(f"{nums[0]}{first}{nums[1]}={nums[2]}")
else: print(f"{nums[0]}={nums[1]}{second}{nums[2]}")
