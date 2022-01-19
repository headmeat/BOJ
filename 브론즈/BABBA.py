K = int(input())

fibo = [0 for i in range(46)]

fibo[0] = 0
fibo[1] = 1

for i in range(2, K+1):
    fibo[i] = fibo[i-1] + fibo[i-2]

print(fibo[K-1], end = " ")

fibo[0] = 1
fibo[1] = 1

for i in range(2, K+1):
    fibo[i] = fibo[i-1] + fibo[i-2]

print(fibo[K-1])
