from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
truth_list = list(map(int, input().split()))
truth = [0 for _ in range(n+1)]
party = [list(map(int, input().split()))[1:] for _ in range(m)]
yes_or_no = [1 for _ in range(m)]
ans = 0

for i in range(1, len(truth_list)): truth[truth_list[i]] = 1

for _ in range(50):
    for i in range(m):#50
        if yes_or_no[i] == 0: continue

        for j in party[i]:#50
            if truth[j]:
                yes_or_no[i] = 0
                break

        if yes_or_no[i]==0:
            for j in party[i]: truth[j] = 1

print(sum(yes_or_no))

#무한 반복해도 끝이 없을 수 있음
