from sys import stdin
input = stdin.readline

n = int(input())
formula = input().rstrip()
max_result = -2**32

def solve(i, arr):
    if i == c:
        idx = 0
        res = []
        res.append(int(formula[0]))

        for x in range(1, len(formula)):
            if formula[x] in ["+", "-", "/", "*"]:
                if arr[idx] == 0:
                    res.append(formula[x])
                    if x+1<n: res.append(int(formula[x+1]))
                else:
                    del res[-1]
                    sm = int(formula[x-1]) if 0<=x-1 else 0

                    if formula[x] == "+":
                        sm += int(formula[x+1])
                    elif formula[x] == "-":
                        sm -= int(formula[x+1])
                    elif formula[x] == "/":
                        sm /= int(formula[x+1])
                    else:
                        sm *= int(formula[x+1])

                    res.append(sm)

                idx += 1

        total = res[0]

        for i in range(1, len(res)-1):
            if res[i] == "+":
                total += res[i+1]
            elif res[i] == "-":
                total -= res[i+1]
            elif res[i] == "/":
                total /= res[i+1]
            elif res[i] == "*":
                total *= res[i+1]

        global max_result
        max_result = max(max_result, total)

        return

    arr[i] = 0
    solve(i+1, arr)

    if i == 0 or arr[i-1]==0:
        arr[i] = 1
        solve(i+1, arr)

c = 0

for x in formula:
    if x in ["+", "-", "/", "*"]:
        c += 1

solve(0, [0 for _ in range(c)])

print(max_result)
