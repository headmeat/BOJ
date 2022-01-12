N = int(input())

arr = list(map(int, input().split()))
sm = 0
mx = max(arr)

for i in arr:
    sm += i/mx*100

print(sm/len(arr))
