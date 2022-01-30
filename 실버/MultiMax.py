import sys

N = int(input())
input = sys.stdin.readline

lst = list(map(int, input().split()))
tmp = list(lst)

sec = sec2 = 1

for i in range(2):
    mx = max(lst)
    sec *= mx
    lst.remove(mx)

for i in range(2):
    mn = min(tmp)
    sec2 *= mn
    tmp.remove(mn)

thd = max(sec * max(lst), sec2 * max(tmp))

print(max(max(thd, sec2), sec))
