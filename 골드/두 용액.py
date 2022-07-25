from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
com = 2*(10**9) + 1
answer = [-1, -1]

a, b = 0, len(arr)-1

while(a<b):
    value = arr[b] + arr[a]
    
    if abs(value) < com:
        com = abs(value)
        answer[0], answer[1] = arr[a], arr[b]

    if value>0: b -= 1
    elif value<0: a += 1
    else: break

print(" ".join(map(str, answer)))
