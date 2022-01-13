N = int(input())

#재귀(2^n)
arr = [0] * (N+1)
arr[0] = 0
if N>0: arr[1] = 1

#N은 원소 번호: #1~#N
def fibonacci(N, arr):
    if N == 0 or N == 1: return arr[N]
    if arr[N] != 0: return arr[N]

    return fibonacci(N-2, arr) + fibonacci(N-1, arr)

print(fibonacci(N, arr))

#dp(n)
"""
fibo = [0] * (N+1)

#N은 원소 번호: #1~#N
def fibonacci(N):
    if N <= 1: return N
    
    fibo[0] = 0
    fibo[1] = 1

    for i in range(2, N+1):
        fibo[i] = fibo[i-1] + fibo[i-2]
    
    return fibo[N]

print(fibonacci(N))
"""
