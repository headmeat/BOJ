from itertools import combinations
N = int(input())
players = []
scores = []
mn = 9999
st = set()

for i in range(N): 
    scores.append(list(map(int, input().split())))
    players.append(i)
cnt = 0

for i in list(combinations(players, int(N/2))):
    start = list(i)
    link = []

    if tuple(start) in st: continue
    cnt +=1 
    start_s = 0
    link_s = 0
    for j in players:
        if j not in start: link.append(j)

    st.add(tuple(link))

    for j in start:
        for k in [x for x in start if x!=j]: 
            if j > k: continue
            start_s += scores[j][k]
            start_s += scores[k][j]
    for j in link:
        for k in [x for x in link if x!=j]: 
            if j > k: continue
            link_s += scores[j][k]
            link_s += scores[k][j]
    mn = min(mn, abs(start_s-link_s))

print(mn)
