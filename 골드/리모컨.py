from sys import stdin

input = stdin.readline

n = int(input())
m = int(input())

first = n
second = n
start = 100

if m > 0: wrong = list(map(int, input().split()))
else:
    print(min(len(str(n)), abs(n - start)))
    exit(0)

sw = sw2 = True

while(sw and sw2):
    if abs(n - start) <= abs(first-n): break

    if sw == True:
        k  = 1
        c = 0

        for i in range(len(str(first))):
            if (((first % 10 ** k) - ((first % 10 ** (k-1)) if k > 1 else 0))) // (10 ** (k-1)) in wrong:
                first += 1
                c += 1
                break
            k += 1

    if second >= 0 and sw2 == True:
        k = 1
        c1 = 0

        for i in range(len(str(second))):
            if (((second % 10 ** k) - ((second % 10 ** (k-1)) if k > 1 else 0))) // (10 ** (k-1)) in wrong:
                second -= 1
                c1 += 1
                break
            k += 1

    if c == 0: 
        start = first
        sw = False
    if c1 == 0 and second >= 0:
        start = second
        sw2 = False

if len(str(start)) + abs(start-n) > abs(n - 100): print(abs(n - 100))
else: print(len(str(start)) + abs(start-n))
