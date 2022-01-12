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
