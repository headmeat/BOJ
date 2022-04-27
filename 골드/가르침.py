from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
alphabet = [0 for _ in range(26)]
words = [input().rstrip() for _ in range(n)]
ans = 0

if k<5:
    print(0)
    exit(0)

def solve(c, x):
    if c==k:
        global ans
        count = 0
        for word in words:
            sw = True
            for w in word[4:-4]:
                if alphabet[ord(w)-97]==0: 
                    sw = False
                    break
            if sw: count += 1
        ans = max(ans, count)
        return

    for i in range(x+1, 26):
        if alphabet[i]: continue

        alphabet[i]=1
        solve(c+1, i)
        alphabet[i]=0

for i in [0, 13, 19, 8, 2]:
    alphabet[i] = 1

solve(5, -1)

print(ans)
