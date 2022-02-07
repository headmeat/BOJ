N = int(input())
arr = list(map(int, input().split()))
sm = 0
streak = 1

for i in range(len(arr)):
    if arr[i] == 1: 
        sm += streak
        streak += 1
    else:
        streak = 1

print(sm)
