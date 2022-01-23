N = int(input())
i, j = 0, 1

while(j <= N):
    j += i
    i += 1

i -= 1
j -= i

print(i - (N - j), N - j + 1)
