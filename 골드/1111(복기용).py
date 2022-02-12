from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))

if len(arr) > 2:
    sw = False

    if len(set(arr)) == 1:
        print(arr[0])
        exit(0)

    if len(arr) > 3:
        for i in range(len(arr)-3):
            if arr[i+1] - arr[i] != 0 and arr[i+2] - arr[i+1] != 0:
                if (arr[i+2] - arr[i+1]) / (arr[i+1] - arr[i]) == (arr[i+3] - arr[i+2]) / (arr[i+2] - arr[i+1]):
                    sw = True
                else:
                    sw = False
                    break
            else:
                if arr[i+1] - arr[i] == 0: 
                    print("B")
                elif sum(arr[1:]) == 0: 
                    print(0)
                else: print("B")
                exit(0)

        a = (arr[2] - arr[1]) / (arr[1] - arr[0])

        if sw and a == int(a): sw = True
        else: sw = False
    else:
        a = (arr[2] - arr[1]) / (arr[1] - arr[0])
        if a == int(a): sw = True

    if sw != True:
        print("B")
        exit(0)

    a = int((arr[2] - arr[1]) / (arr[1] - arr[0]))
    b = arr[1] - a*arr[0]
    print(arr[-1]*a + b)
elif len(arr) == 2:
    if arr[0] == arr[1]: print(arr[0])
    else: print("A")
else: print("A")
