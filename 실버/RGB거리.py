from sys import stdin
input = stdin.readline

t = int(input())

add = [0,0,0]

for _ in range(t):
    r,g,b=map(int,input().split())
    
    z = min(add[1]+r,add[2]+r)
    x = min(add[0]+g,add[2]+g)
    c = min(add[0]+b,add[1]+b)

    add[0] = z
    add[1] = x
    add[2] = c

print(min(add))
