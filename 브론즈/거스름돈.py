from sys import stdin
input = stdin.readline

n = 1000 - int(input())
c = 0
coins = [500, 100, 50, 10, 5, 1]

for i in coins:
    c+=n//i
    n%=i
    if n==0: break

print(c)
