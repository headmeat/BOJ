from sys import stdin
input = stdin.readline

t = int(input())

def dfs(string):
    f = l = 0 

    if len(string)==0: return 1

    for i in range(1, len(string)):
        if string[l]==string[i]: l += 1
        else:
            if l-f and dfs(string[:f]+(string[l+1:])) == 1: return 1
            f = l = i
    
    if l-f>0 and dfs(string[:f]+string[l+1:]) == 1: return 1

    return 0

for _ in range(t):
    string = input().rstrip()
    print(dfs(string))
