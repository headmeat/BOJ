from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
s = deque([input().rstrip() for _ in range(n)])
t = ""

def faster(a, b):
    tmp_a, tmp_b = a, b

    while(tmp_a<tmp_b):
        if ord(s[tmp_a])<ord(s[tmp_b]): return a
        elif ord(s[tmp_a])>ord(s[tmp_b]): return b
        
        tmp_a += 1
        tmp_b -= 1

    return a

for i in range(n):
    if ord(s[0])<ord(s[-1]): t += s.popleft()
    elif ord(s[0])==ord(s[-1]):
        idx = faster(0, len(s)-1)
        if idx==0: t += s.popleft()
        else: t += s.pop()
    else: t += s.pop()

for i in range(len(t)):
    if i!=0 and i%80==0: print()
    print(t[i], end="")
