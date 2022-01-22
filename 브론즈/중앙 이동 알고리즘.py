N = int(input())

sqrs = int(4 ** N)
lines = int(2 ** N)

ans = (int(sqrs/lines) + 1) * (lines + 1)

print(ans)
