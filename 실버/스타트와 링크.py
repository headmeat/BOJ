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

"""
#재귀 호출 버전
def iter(T, start):
    if len(start) == T:
        global players, st, mn

        if tuple(start) in st: return
        link = []
        start_s = link_s = 0
        for i in players:
            if i not in start: link.append(i)
        st.add(tuple(link))
        for j in start:
            for k in [x for x in start if x!=j and x > j]: 
                start_s += scores[j][k]
                start_s += scores[k][j]
        for j in link:
            for k in [x for x in link if x!=j and x > j]:
                link_s += scores[j][k]
                link_s += scores[k][j]
        mn = min(mn, abs(start_s-link_s))  
        return

    for i in range(N):
        if i not in start:
            if len(start) == 0:
                start.append(i)
                iter(T, start)
                start.remove(i)
            elif i>start[-1]:
                start.append(i)
                iter(T, start)
                start.remove(i)

iter(int(N/2), [])
"""
