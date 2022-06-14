from sys import stdin
input = stdin.readline

n = int(input())
sm = 0
colors = []
substract_color = [0 for _ in range(200001)]
substract_size = [0 for _ in range(2001)]
ans = [0 for _ in range(n)]

for i in range(n):
    color, size = map(int, input().split())
    colors.append((i, color, size))

colors.sort(key = lambda x: (x[2], x[1]))

for i in range(len(colors)):
    idx, color, size = colors[i]
    if i>0 and colors[i-1][1]==color and colors[i-1][2]==size: ans[idx] = ans[colors[i-1][0]]
    else: ans[idx] = sm - substract_color[color] - substract_size[size]
    sm += size
    substract_color[color] += size
    substract_size[size] += size

print("\n".join(map(str, ans)))
