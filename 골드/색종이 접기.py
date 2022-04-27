from copy import deepcopy
from sys import stdin
input = stdin.readline

arr = [list(map(int, input().split())) for _ in range(10)]
dp = [[0 for _ in range(10)] for _ in range(10)]
papers = [5 for _ in range(5)]

ans = 101
total = 0

for i in range(10):
    for j in range(10):
        total += arr[i][j]

def solve(x, paper, whole):
    global ans, papers

    if whole==total: 
        ans = min(ans, paper)
        return
    if paper>=ans: 
        return

    for i in range(x, 10):
        for j in range(10):
            if arr[i][j] == 1:
                for k in range(4, -1, -1):#색종이 크기
                    if papers[k]==0: continue
                    if i+k>=10 or j+k>=10: continue
                    sw = True

                    for l in range(k+1):
                        for m in range(k+1):
                            if arr[i+l][j+m]==0:
                                sw = False
                                break
                        if sw==False: break
                    if sw==False: continue

                    papers[k] -= 1
                    for l in range(k+1):
                        for m in range(k+1):
                            arr[i+l][j+m] = 0

                    solve(i, paper+1, whole+(k+1)**2)

                    papers[k] += 1
                    for l in range(k+1):
                        for m in range(k+1):
                            arr[i+l][j+m] = 1

solve(0, 0, 0)
if ans==101: print(-1)
else: print(ans)
