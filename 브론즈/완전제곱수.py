M = int(input())
N = int(input())
mn = -1
sm = 0
mx = N

for i in range(M, N+1):
    if i**0.5 == int(i**0.5):
        mn = int(i**0.5)
        break

if mn == -1:print("-1")
else: 
    mx = int(N**0.5)

    for i in range(mn, mx+1):
        sm += int(i ** 2)
    print(sm)
    print(mn**2)
