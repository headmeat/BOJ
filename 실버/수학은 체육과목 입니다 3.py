S = input()

first = -1

try:
    sw = True
    t = 0
    if len(S) != 1:
        while(True):
            for i in range(1, len(S)):
                if t > len(S) or i > len(S): raise Exception()
                sw = True

                for j in range(i, 3*i+1, i):
                    cnt = 0
                    if int(S[:i]) + 1 != int(S[i:2*i+t]):
                        sw = False
                        break
                    cnt += 1
                    if cnt >= 3:
                        sw = True
                        raise Exception()
                if sw == True: first = int(S[:i])
            if first != -1: break
            else: t += 1
except Exception as e:
    pass

if first != -1:
    i = 0
    digits = -1
    L = len(str(first))

    while i < len(S):
        tmp = int("9"*L)
        i += (tmp - first + 1) * L
        digits = L
        L += 1

    print(first, S[-digits:])
else: print(S, S)
