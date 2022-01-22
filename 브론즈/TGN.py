N = int(input())

ads = [list(map(int, input().split())) for i in range(N)]

for i in ads:
    r, e, c = map(lambda x: x, i)

    if r < e - c: print("advertise")
    elif r == e - c: print("does not matter")
    else: print("do not advertise")
