from sys import stdin
from collections import deque
input = stdin.readline

def poss(key, k, w, d, l, arr):
    if w+d+l == 0:
        candidates[key].append([x for x in arr])
        return
    
    if key==k:
        arr.append(-1)
        poss(key, k+1, w, d, l, arr)
        del arr[-1]
        return

    if w>0:
        arr += ["W"]
        poss(key, k+1, w-1, d, l, arr)
        del arr[-1]
    if d>0:
        arr += ["D"]
        poss(key, k+1, w, d-1, l, arr)
        del arr[-1]
    if l>0:
        arr += ["L"]
        poss(key, k+1, w, d, l-1, arr)
        del arr[-1]

def compare(a, b):
    if a=="D" and b=="D": return True
    elif a=="W" and b=="L": return True
    elif a=="L" and b=="W": return True
    else: return False

def solve(n):
    global ans

    if n == 6:
        ans = 1
        return

    for cand in candidates[n]:
        sw = True

        for prev in range(n):
            if compare(sel[prev][n], cand[prev])==False: 
                sw = False
                break
            
        if sw:
            sel[n] = cand
            solve(n+1)
            if ans: return
            sel[n] = []

answer = []

for _ in range(4):#테케
    sel = [[] for _ in range(6)]
    case = deque(map(int, input().rstrip().split()))
    dic = {}
    ans = 0
    candidates = [[] for _ in range(6)]
    tel = True

    if sum(case)>30:
        answer.append(0)
        continue

    for i in range(6):
        tmp = []
        cnt = 0
        for j in range(3): tmp.append(case.popleft())
        dic[i] = tmp
        if sum(dic[i])!=5: tel = False
    
    if tel==False:
        answer.append(0)
        continue

    for i in range(6):
        w, d, l = dic[i]
        poss(i, 0, w, d, l, [])

    solve(0)

    answer.append(ans)

print(" ".join(map(str, answer)))
