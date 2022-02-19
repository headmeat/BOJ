from sys import stdin
input = stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
nums = list(map(int, input().split()))

for num in nums:
    left, right = 0, len(a)-1
    mid = (left + right) // 2
    sw = False

    while(left <= right):
        if a[mid] == num: 
            sw = True
            break
        elif a[mid] < num: left = mid + 1
        else: right = mid - 1

        mid = (left + right) // 2

    if sw == True: print(1)
    else: print(0)
