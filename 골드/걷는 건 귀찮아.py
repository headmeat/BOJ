from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
p = list(map(int, input().split()))
x = list(map(int, input().split()))
px = []

for i in range(len(p)):
    px.append(p[i] + x[i])

idx = cnt = 0
mx_length = px[idx]

while ( True ):
    length = px[idx]
    tmp = 0

    if length >= m:
        print(cnt)
        exit(0)

    for i in range(idx+1, len(p)):
        if p[i] <= length:
            if mx_length < p[i] + x[i]:
                mx_length = p[i] + x[i]
                idx = i
                tmp += 1
        else: break
    
    if tmp == 0:
        print(-1)
        exit(0)
    else: cnt += 1
