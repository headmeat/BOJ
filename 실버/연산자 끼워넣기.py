N = int(input())
lst = list(map(int, input().split()))
comp = list(map(int, input().split()))
res = []

def iter(N, arr):
    if len(arr) == N:
        sm = lst[0]
        print(arr)
        for i in range(len(arr)):
            if calcs[arr[i]] == "+": sm = sm + lst[i+1]
            elif calcs[arr[i]] == "-": sm = sm - lst[i+1]
            elif calcs[arr[i]] == "*": sm = sm * lst[i+1]
            elif calcs[arr[i]] == "/": sm = int(sm / lst[i+1])
        res.append(sm)

        return

    for i in range(N):
        if i not in arr:
            arr.append(i)
            iter(N, arr)
            arr.remove(i)

calcs = []

for i in range(len(comp)):
    for j in range(comp[i]):
        if i == 0: calcs.append("+")
        elif i == 1: calcs.append("-")
        elif i == 2: calcs.append("*")
        else: calcs.append("/")

iter(N-1, [])
#print(res)
print(max(res))
print(min(res))
