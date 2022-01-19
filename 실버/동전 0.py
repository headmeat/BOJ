N, K = map(int, input().split())

coins = [int(input()) for i in range(N)]
cnt = 0

for i in range(N-1, -1, -1):
    if K <= 0: break
    cnt += K // coins[i]
    K -= (K // coins[i]) * coins[i]

print(cnt)
