from sys import stdin
from collections import deque
input = stdin.readline

n, m, t = map(int, input().split())
circle = [list(map(int, input().split())) for _ in range(n)]
test = [list(map(int, input().split())) for _ in range(t)]

def spin(meter, d, k):
    #d==0 시계, 1 반시계
    tmp = [0 for _ in range(len(circle[meter]))]

    if d==0:
        for j in range(len(circle[meter])):
            tmp[j] = circle[meter][j-k]
    else:
        for j in range(len(circle[meter])):
            tmp[j] = circle[meter][(j+k)%len(circle[meter])]
    
    circle[meter] = tmp

def check():
    global circle

    c = 0
    tmp = [x[:] for x in circle]

    for i in range(len(circle)):
        for j in range(len(circle[i])):
            if circle[i][j]=='x': continue

            if circle[i][(j+1)%len(circle[i])]==circle[i][j]:
                tmp[i][(j+1)%len(circle[i])] = tmp[i][j] = 'x'
                c += 1
            if i+1<len(circle) and circle[i+1][j]==circle[i][j]:
                tmp[i+1][j] = tmp[i][j] = 'x'
                c += 1
            if i-1>=0 and circle[i-1][j]==circle[i][j]:
                tmp[i-1][j] = tmp[i][j] = 'x'
                c += 1
    
    circle = tmp

    if c==0:
        avg = 0
        count = 0

        for i in range(len(circle)):
            for j in range(len(circle[i])):
                if circle[i][j]=='x': continue
                avg += circle[i][j]
                count += 1

        if count>0:
            avg /= count
            for i in range(len(circle)):
                for j in range(len(circle[i])):
                    if circle[i][j]=='x': continue
                    if circle[i][j]>avg: circle[i][j] -= 1
                    elif circle[i][j]<avg: circle[i][j] += 1

for i in range(t):
    x, d, k = test[i]
    for j in range(1, n+1):
        if j%x==0: spin(j-1, d, k)
    check()

sm = 0

for i in range(len(circle)):
    for j in range(len(circle[i])):
        if circle[i][j] == 'x': continue
        sm += circle[i][j]

print(sm)
