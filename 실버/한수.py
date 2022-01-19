N = int(input())
cnt = 0

for i in range(1, N+1):
    st = set()
    num = str(i)
    for j in range(len(num)-1):
        st.add(int(num[j])-int(num[j+1]))
    if len(st) <= 1: cnt += 1

print(cnt)
