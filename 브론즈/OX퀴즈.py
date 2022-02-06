T = int(input())

for i in range(T):
    sm = 0
    cnt = 0
    tmp = 1
    for j in input():
        if j == "O":
            sm += tmp
            tmp += 1
            continue
        tmp = 1
        
    print(sm)
