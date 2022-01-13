N = int(input())
mn = N

for i in range(int(N / 5), -1, -1):
    fives = i
    tmp = N - (fives*5)
    threes = int(tmp / 3)
    
    if ( N == (fives * 5 + threes * 3) ): mn = min(mn, fives+threes)

if mn == N: print("-1")
else: print(mn)
