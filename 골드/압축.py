from sys import stdin
input = stdin.readline

string = input().rstrip()
i, times = 0, [1]
stack = 0
ans = 0

while(i < len(string)):
    if string[i] == "(": 
        times.append(times[-1] * int(string[i-1]))
        stack += 1
    elif string[i] == ")":
        stack -= 1
        times.pop()
    elif 48<=ord(string[i])<=57: 
        if i+1 < len(string) and string[i+1] == "(": pass
        else: ans += times[-1]

    i += 1

print(ans)
