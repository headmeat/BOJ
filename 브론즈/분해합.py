#분해합

N = int(input())
sw = False

for i in range(1, N):
    sm = i
    tmp = i
    while (tmp > 0):
        sm += tmp % 10
        tmp //= 10
    if sm == N:
        print(i)
        sw = True
        break

if sw == False: print(0)
