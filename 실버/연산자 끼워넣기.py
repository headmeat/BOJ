def solve(i, arr, sm):
    if i == n:
        global mx, mn
        mx = max(sm, mx)
        mn = min(sm, mn)
        return

    if arr[0] > 0:
        arr[0] -= 1
        solve(i+1, arr, sm + nums[i])
        arr[0] += 1
    if arr[1] > 0:
        arr[1] -= 1
        solve(i+1, arr, sm - nums[i])
        arr[1] += 1
    if arr[2] > 0:
        arr[2] -= 1
        solve(i+1, arr, sm * nums[i])
        arr[2] += 1
    if arr[3] > 0:
        arr[3] -= 1
        if sm < 0: solve(i+1, arr, -(abs(sm)//nums[i]))
        else: solve(i+1, arr, sm // nums[i])
        arr[3] += 1

T = int(input())

for k in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    ops = ["+", "-", "*", "//"]
    combs = []
    tmp = list(map(int, input().split()))
    mx = -10 ** 15
    mn = 10 ** 15

    for i in range(4):
        for j in range(tmp[i]): combs.append(ops[i])

    solve(1, tmp, nums[0])

    print(f"#{k+1} {mx} {mn}")

"""
#기존
from itertools import permutations

N = int(input())
lst = list(map(int, input().split()))
comp = list(map(int, input().split()))
res = []
st = set()

def calculate(comp):
    sm = lst[0]

    for i in range(len(comp)):
        if comp[i] == "+": sm = sm + lst[i+1]
        elif comp[i] == "-": sm = sm - lst[i+1]
        elif comp[i] == "*": sm = sm * lst[i+1]
        elif comp[i] == "/": sm = int(sm / lst[i+1])
    res.append(sm)

calcs = []

for i in range(len(comp)):
    for j in range(comp[i]):
        if i == 0: calcs.append("+")
        elif i == 1: calcs.append("-")
        elif i == 2: calcs.append("*")
        else: calcs.append("/")
c = 0
for i in set(permutations(calcs, len(calcs))):
    calculate(i)
print(max(res))
print(min(res))
"""
