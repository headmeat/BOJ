from sys import stdin
input = stdin.readline

string = input().rstrip()
all = []
tmp = ""

for s in string:
    if s == "+" or s == "-": 
        all.append(int(tmp))
        all.append(s)
        tmp = ""
    else:
        tmp += s
        continue

all.append(int(tmp))

visited = [0 for _ in range(len(all))]

while(sum(visited) + 1 != len(visited)):
    if "+" in all:
        idx = all.index("+")
        all[idx] = "X"
        visited[idx] = 1
        prev = idx - 1
        next = idx + 1

        while(prev >= 0):
            if visited[prev] == 0:
                break
            else: prev -= 1

        while(next < len(all)):
            if visited[next] == 0:
                all[prev] += all[next]
                visited[next] = 1
                break
            else: next += 1
    elif "-" in all:
        idx = all.index("-")
        all[idx] = "X"
        visited[idx] = 1
        prev = idx - 1
        next = idx + 1

        while(prev >= 0):
            if visited[prev] == 0:
                break
            else: prev -= 1

        while(next < len(all)):
            if visited[next] == 0:
                all[prev] -= all[next]
                visited[next] = 1
                break
            else: next += 1

print(all[0])
