import random

total, correct = map(int, input().split())
ans = list(map(int, input().split()))
sheet = [0] * total

for i in list(map(int, input().split())):
    sheet[i-1] = ans[i-1]

choices = [x for x in range(1, 6)]

if sheet[0] == 0:
    st = set()
    if 1<total and sheet[1]!=0: st.add(sheet[1])
    st.add(ans[0])

    for j in st: choices.remove(j)
    sheet[0] = random.choice(choices)
    for j in st: choices.append(j)

for i in range(1, len(sheet)):
    if sheet[i]!=0: continue
    
    st = set()
    st.add(sheet[i-1]) #
    st.add(ans[i])
    if i+1 < len(sheet): 
        if sheet[i+1] != 0: st.add(sheet[i+1])

    for j in st: choices.remove(j) #

    sheet[i] = random.choice(choices)

    for j in st: choices.append(j)

print(" ".join(map(str, sheet)))
