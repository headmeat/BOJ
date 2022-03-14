from sys import stdin
input = stdin.readline

n = int(input())
prev = [0]

for i in range(n):
    curr = list(map(int, input().split()))

    for j in range(len(curr)):
        cand1 = cand2 = -1

        if j-1>=0:
            cand1 = prev[j-1]
        if 0<=j<len(prev):
            cand2 = prev[j]
        
        curr[j] += max(cand1, cand2)
    
    prev = curr

print(max(prev))
