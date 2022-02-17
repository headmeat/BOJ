from collections import deque
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
do = deque()
su = deque()
sw = True

for i in range(n):
    a, b = map(int, input().split())
    do.append(a)
    su.append(b)

pan_do = deque()
pan_su = deque()

for i in range(m):
    if sw == True: pan_do.append(do.pop())
    else: pan_su.append(su.pop())

    la, lb = len(do), len(su)

    if la == 0 and lb != 0:
        print("su")
        exit(0)
    elif la != 0 and lb == 0:
        print("do")
        exit(0)

    if len(pan_do) > 0 and len(pan_su) > 0 and pan_do[-1] + pan_su[-1] == 5:
        for i in range(len(pan_do)):
            su.appendleft(pan_do.popleft())

        for i in range(len(pan_su)):
            su.appendleft(pan_su.popleft())
    else:
        if (len(pan_do) > 0 and pan_do[-1] == 5) or (len(pan_su) > 0 and pan_su[-1] == 5):
            for i in range(len(pan_su)):
                do.appendleft(pan_su.popleft())

            for i in range(len(pan_do)):
                do.appendleft(pan_do.popleft())

    sw = not sw

if len(do) > len(su): print("do")
elif len(do) < len(su): print("su")
else: print("dosu")
