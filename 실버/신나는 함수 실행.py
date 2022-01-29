dp = [[[-1 for _ in range(21)] for _ in range(21)] for _ in range(21)]

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0: return 1

    if a > 20 or b > 20 or c > 20: return w(20, 20, 20)

    if a < b and b < c: 
        return w(a, b, c-1) if dp[a][b][c-1] == -1 else dp[a][b][c-1] + w(a, b-1, c-1) if dp[a][b-1][c-1] == -1 else dp[a][b-1][c-1] - w(a, b-1, c) if dp[a][b-1][c] == -1 else dp[a][b-1][c]

    return (w(a-1, b, c) if dp[a-1][b][c] == -1 else dp[a-1][b][c]) + (w(a-1, b-1, c) if dp[a-1][b-1][c] == -1 else dp[a-1][b-1][c]) + (w(a-1, b, c-1) if dp[a-1][b][c-1] == -1 else dp[a-1][b][c-1]) - (w(a-1, b-1, c-1) if dp[a-1][b-1][c-1] == -1 else dp[a-1][b-1][c-1])

for i in range(1, 21):
    for j in range(1, 21):
        for k in range(1, 21):
            dp[i][j][k] = w(i, j, k)

while(True):
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1: break
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")
