from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
s = {}
ans = 0

for _ in range(n):
    s[input().rstrip()] = 0

for _ in range(m):
    if input().rstrip() in s.keys(): ans += 1

print(ans)
