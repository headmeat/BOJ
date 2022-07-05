from sys import stdin
input = stdin.readline

n = int(input())
stack = []
ans = 0

for _ in range(n):
    x, h = map(int, input().split())

    while(stack and stack[-1]>h): stack.pop()

    if h>0 and (len(stack)==0 or stack[-1]<h): 
        stack.append(h)
        ans += 1

print(ans)
