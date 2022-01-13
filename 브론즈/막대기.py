import sys

N = int(input())
lst = []
prev = -1
cnt = 0

for i in range(N):
    lst.append(int(sys.stdin.readline().rstrip()))

for i in range(N-1, -1, -1):
    if prev < lst[i]:
        cnt += 1
        prev = lst[i]
