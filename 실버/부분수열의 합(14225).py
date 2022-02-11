from sys import stdin

input = stdin.readline

n = int(input())
lst = list(map(int, input().split()))
res = set()

def solve(i, sm):
    if i == n:
        res.add(sm)
        return

    solve(i+1, sm)
    solve(i+1, sm + lst[i])

solve(0, 0)
mx = max(res)
res = sorted(list(res))

for i in range(1, mx):
    if res[i] != i:
        print(i)
        exit(0)

print(mx + 1)

"""
#부분수열의 합

N = int(input())

tmp = []

def solve(i, arr):
    if i == N:
        sm = 0
        for j in range(N):
            sm += lst[j] * arr[j]
        try:
            tmp[sm] = 1
        except Exception as e:
            print("SEX",sm)
        return

    arr[i] = 0
    solve(i+1, arr)
    arr[i] = 1
    solve(i+1, arr)

lst = list(map(int, input().split()))
mx = sum(lst)

tmp = [0 for i in range(20 * 100000)]
solve(0, [0 for i in range(N)])

for i in range(1, 20 * 100000):
    if tmp[i] == 0: 
        print(i)
        break
"""
