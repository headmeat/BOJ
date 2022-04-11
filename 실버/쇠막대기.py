from sys import stdin
from collections import deque
input = stdin.readline

string = input()
n = 0
stack = []
ans = 0

for i in range(len(string)):
    if string[i]==")":
        if string[i-1]!="(":
            n += 1

for i in range(len(string)):
    if string[i] == "(":
        stack.append(string[i])
    else:
        if string[i] == ")":
            if string[i-1] == "(":
                stack.pop()
                ans += len(stack)
            else:
                stack.pop()

print(ans+n)
