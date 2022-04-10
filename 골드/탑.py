from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
stack = []
ans = [0 for _ in range(n)]

for i in range(n):
    if len(stack)==0:
        stack.append(i+1)
        continue

    while(stack):
        if arr[stack[-1]-1] >= arr[i]:
            ans[i] = stack[-1]
            break
        else:
            stack.pop()

    stack.append(i+1)

print(" ".join(map(str, ans)))
