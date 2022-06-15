from sys import stdin
input = stdin.readline

n = int(input())
coders = list(map(int, input().split()))
coders.sort()

offset = 10000
count = [0 for _ in range(20001)]
order = [0 for _ in range(len(coders))]
ans = 0

for i in range(len(coders)):
    count[offset+coders[i]] += 1
    order[i] = count[offset+coders[i]]

for i in range(len(coders)):
    if count[offset+coders[i]]==0: continue

    for j in range(i+1, len(coders)):
        if coders[i]+coders[j]>10000 or coders[i]+coders[j]<-10000: continue

        if coders[j] == -(coders[j]+coders[i]) and count[offset+coders[j]] - order[j]: ans += count[offset+coders[j]] - order[j]
        elif count[offset-(coders[j]+coders[i])]>0 and -(coders[j]+coders[i])>coders[j]: ans += count[offset-(coders[i]+coders[j])]

print(ans)
