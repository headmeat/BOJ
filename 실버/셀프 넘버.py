st = set()

for i in range(1, 10001):
    st.add(sum([int(x) for x in str(i)]) + i)

for i in range(1, 10001):
    if i not in st: print(i)
