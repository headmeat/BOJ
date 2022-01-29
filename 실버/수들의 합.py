N = int(input())
i = 1
cnt = 0

while (N >= 0):
    N -= i
    i += 1
    cnt += 1

if N == 0: print(cnt)
elif N < 0: print(cnt - 1)
