K = int(input())
N = int(input())
passed = 0

times = []
ans = []

for i in range(N):
    tmp = input().split()
    times.append(tmp[0])
    ans.append(tmp[1])

for i in range(N):
    passed += int(times[i])

    if passed >= 230:
        print(K)
        break

    if ans[i] == "T": 
        if K<8: K += 1
        else: K = 1
