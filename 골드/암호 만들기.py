from sys import stdin
input = stdin.readline

L, C = map(int, input().split())
nouns = ['a', 'e', 'i', 'o', 'u']

string = [x for x in input().split()]
string.sort()

def solve(i, arr):
    if i == C:
        if sum(arr) == L:
            cnt = 0
            tmp = ""

            for i in range(len(arr)):
                    if arr[i] == 1: 
                        tmp += string[i]
                        if string[i] in nouns: cnt += 1

            if cnt >= 1 and len(tmp) - cnt >= 2:
                print(tmp)

        return

    arr[i] = 1
    solve(i+1, arr)
    arr[i] = 0
    solve(i+1, arr)

solve(0, [0 for _ in range(len(string))])

"""0610-개선
from sys import stdin
input = stdin.readline

l, c = map(int, input().split())
keys = input().rstrip().split()
keys.sort()
nouns = ['a', 'e', 'i', 'o', 'u']

def solve(l, arr, idx):
    global keys, nouns
    if len(arr)==l:
        n = 0

        for k in nouns:
            if k in arr: n += 1

        if len(arr) - n>=2 and n>0: print("".join(arr))
        return

    for i in range(idx, len(keys)):
        arr.append(keys[i])
        solve(l, arr, i+1)
        del arr[-1]

solve(l, [], 0)
"""
