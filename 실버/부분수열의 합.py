N, S = map(int, input().split())
lst = list(map(int, input().split()))
rts = 0

def solution(i, arr):
    if (i == N):
        sm = 0
        for j in range(len(arr)):
            sm += arr[j] * lst[j]
        if sm == S:
            global rts
            rts += 1
        return
    
    arr[i] = 0
    solution(i+1, arr)
    arr[i] = 1
    solution(i+1, arr)

solution(0, [0] * len(lst))

if S == 0: rts -= 1

print(rts)
