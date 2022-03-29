from sys import stdin
input = stdin.readline

s = [x for x in input().rstrip()]
n = len(s)

a = b = c = 0

for i in range(n):
    if s[i]=='a':
        a = 2*a + 1
        a %= 1000000007
    elif s[i]=='b':
        b = 2*b + a
        b %= 1000000007
    else:
        c = 2*c + b
        c %= 1000000007

print(c%1000000007)
