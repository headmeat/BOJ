from sys import stdin
input = stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
stack = []
cnt = {}
ans = 0

for h in arr:
    while(stack and h>stack[-1]):
        ans += 1
        item = stack.pop()
        cnt[item] -= 1

    if h not in cnt.keys(): cnt[h] = 0
    else: ans += cnt[h]

    if len(stack)>cnt[h]: ans += 1
    stack.append(h)

    cnt[h] += 1

print(ans)
