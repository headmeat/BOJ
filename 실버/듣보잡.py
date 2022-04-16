from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
count = 0
ppl = {}
guys = []

for _ in range(n):
    ppl[input().rstrip()] = 0

for _ in range(m):
    who = input().rstrip()
    try:
        ppl[who]
        guys.append(who)
        count += 1
    except Exception as e:
        pass

print(count)
guys.sort()
if len(guys): print("\n".join(map(str, guys)))
