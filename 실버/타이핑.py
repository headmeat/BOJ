from sys import stdin
input = stdin.readline

string = input().rstrip()
sw = 0
combs = []
c = 0

for letter in string:
    if 65<=ord(letter)<=90:
        if sw: c += 1
        else:
            if c>0: combs.append((0, c))
            sw = 1
            c = 1
    else:
        if sw==0: c += 1
        else:
            if c>0: combs.append((1, c))
            sw = 0
            c = 1

if c>0: combs.append((sw, c))

sw = 0
ans = 0

for i in range(len(combs)):
    cap_e_rago_burugee, count = combs[i]

    if sw == cap_e_rago_burugee: ans += count
    elif count==1: ans += 2
    else:
        ans += count+1
        sw = 0 if sw else 1

print(ans)
