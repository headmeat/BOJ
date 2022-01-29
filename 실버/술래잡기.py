soobin, bro = map(int, input().split())
cnt = 0

while(soobin!=bro):
    if abs(bro - soobin * 2) < abs(bro - soobin - 1):
        if abs(bro - soobin * 2) <= abs(bro - (soobin - 1) * 2):
            soobin = soobin * 2
        else: soobin -= 1
    else:
        if soobin < bro: soobin += 1
        else: soobin -= 1
    #print(soobin, bro)
    cnt += 1

print(cnt)

13 12 11 10 20 40 39
