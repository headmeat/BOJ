S = input().upper()
ch = dict()

for i in set(S): ch[i] = S.count(i)

mx = max(ch.values())

ans = [x for x in ch if ch[x] == mx]

if len(ans) > 1: print("?")
else: print(ans[0])
