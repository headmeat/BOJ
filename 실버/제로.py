from sys import stdin
from collections import deque
input = stdin.readline

k = int(input())
stack = []

for i in range(k):
    n = int(input())
    if n == 0: stack.pop()
    else: stack.append(n)

print(sum(stack))
