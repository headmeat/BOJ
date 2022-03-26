from sys import stdin
input = stdin.readline

durumari = [x for x in input().rstrip()]
akma = [x for x in input().rstrip()]
chunsa = [x for x in input().rstrip()]
n = len(akma)
dp = [[[0 for _ in range(n)] for _ in range(len(durumari))] for _ in range(2)]
c = 0

def solve(idx, acc, sw):
    if acc>=len(durumari):
        return 1
    if idx>=n:
        return 0

    if dp[sw][acc][idx]:
        return dp[sw][acc][idx]

    for i in range(idx, n):
        if sw==1 and akma[i]==durumari[acc]:
            dp[sw][acc][idx] += solve(i+1, acc+1, 0)
        if sw==0 and chunsa[i]==durumari[acc]:
            dp[sw][acc][idx] += solve(i+1, acc+1, 1)

    return dp[sw][acc][idx]

for i in range(n):
    if akma[i] == durumari[0]:
        dp[0][0][i] += solve(i+1, 1, 0)
    if chunsa[i] == durumari[0]:
        dp[1][0][i] += solve(i+1, 1, 1)

print(sum(dp[0][0])+sum(dp[1][0]))
