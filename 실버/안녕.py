ppl = int(input())
health = list(map(int, input().split()))
happy = list(map(int, input().split()))
mx = -1
dp = [0 for i in range(ppl)]

def solve(i, arr):
    if i == ppl:
        sm = 0
        hp = 0
        for i in range(len(arr)):
            hp += arr[i] * health[i]
            sm += arr[i] * happy[i]
        if hp < 100:
            global mx
            mx = max(mx, sm)
        return
    
    arr[i] = 0
    solve(i+1, arr)
    arr[i] = 1
    solve(i+1, arr)

solve(0, [0 for i in range(ppl)])

print(mx)
