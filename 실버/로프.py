from sys import stdin
input = stdin.readline

n = int(input())
ropes = []
mx = 0

for i in range(n):
    ropes.append(int(input()))

ropes.sort(reverse=True)

for i in range(1, n+1):
    mx = max(mx, ropes[i-1]*i)

print(mx)
