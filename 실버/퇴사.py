from itertools import combinations

N = int(input())
lst = []
earns = []
costs = []
good = 0

for i in range(N):
    T, P = map(int, input().split())

    if i + T <= N: 
        lst.append(i)
        costs.append(T)
        earns.append(P)

for i in range(len(lst), 0, -1):
    tmp = list(combinations(lst, i))

    for j in tmp:
        k = j[0]
        sm = 0
        while(k<=N):
            if k in j:
                sm += earns[k]
                k += costs[k]
            else: k += 1
        good = max(good, sm)
        if sm == 270:
            print("tmp:",tmp)
            print("j:",j)

print(good)
