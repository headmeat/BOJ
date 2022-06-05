from sys import stdin
input = stdin.readline

r, c = map(int, input().split())
useable = int(input().strip())
wrong = int(input().strip())
papers = [0 for _ in range(c)]
ans = 10**7
height = 0

for _ in range(wrong):
    a, b = map(int, input().strip().split())
    papers[b-1] += 1
    height = max(height, a)

def place(size):
    idx, use = 0, useable

    while(idx<len(papers)):
        if papers[idx]>0: 
            if use>0: 
                use -= 1
                idx += size
            else: return False
        else: idx += 1

    return True

def bisec(x, y):
    if x>y: return

    global ans
    mid = (x+y)//2

    if place(mid): 
        ans = min(ans, mid)
        bisec(x, mid-1)
    else: bisec(mid+1, y)

bisec(height, len(papers))
print(ans)
