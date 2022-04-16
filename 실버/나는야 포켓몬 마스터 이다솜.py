from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
poke = {}
num = {}

for i in range(1, n+1):
    x = input().rstrip()
    poke[x] = i
    num[i] = x

for _ in range(m):
    x = input().rstrip()
    if x.isnumeric():
        x = int(x)
        print(num[x])
    else:
        print(poke[x])
