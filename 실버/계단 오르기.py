from sys import stdin
input = stdin.readline

n = int(input())
one = []
two = []

one.append((int(input()), 1))

for i in range(1, n):
    i_score = int(input())
    m1=m2=0
    cands=[]

    if two:
        cands.append((max(two)[0]+i_score, 1))
    else:
        cands.append((i_score, 1))
    
    two = []
    steps = 0

    while(one):
        score, step = one.pop()

        if step==1:
            m1=max(score+i_score, m1)
        
        if score>m2:
            m2=score
            steps=step

    if m1: cands.append((m1, 2))
    if m2: two.append((m2, steps))

    one = cands

print(max(one)[0])
