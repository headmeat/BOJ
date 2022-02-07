a, b, v = map(int, input().split())
tmp = (v - a)

if tmp % ( a - b ) != 0:
    tmp = (tmp // (a - b) + 1) * (a-b)

val = tmp // (a-b)

print(val if val==v else (val + 1))
