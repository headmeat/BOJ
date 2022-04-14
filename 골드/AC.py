from sys import stdin
from collections import deque
input = stdin.readline

t = int(input())

for _ in range(t):
    command = input().rstrip()
    n = int(input())
    lst = input().rstrip().strip("[").strip("]").split(",")
    arr = deque()

    odd = 0

    for i in range(len(lst)):
        if lst[i]!='': arr.append(int(lst[i]))

    error = False
    rev = False
    
    for i in range(len(command)):
        if command[i] == "R": 
            rev = not rev
            continue
        else:
            if len(arr)==0:
                error = True
                break
            if rev: arr.pop()
            else: arr.popleft()

    if rev==True: arr.reverse()

    if error: print("error")
    else: 
        print("[", end = "")
        print(",".join(map(str, arr)), end="")
        print("]")
