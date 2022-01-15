line = int(input())

for i in range(2*line-1):
    tmp = abs((i+1) - line)
    for j in range(tmp): print(" ", end="")
    for j in range(line-tmp): print("*", end="")
    print()
