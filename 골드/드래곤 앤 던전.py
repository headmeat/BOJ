from sys import stdin
input = stdin.readline

n, h_atk = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(n)]
tmp = [0]

for i in range(len(rooms)):
    t, a, h = rooms[i]
    temp = tmp[-1]
    
    if t == 1:
        temp -= a*(h//h_atk-1) + (a if h%h_atk else 0)
    else:
        h_atk += a
        temp += h

    tmp.append(temp if temp<0 else 0)

print(abs(min(tmp))+1)
