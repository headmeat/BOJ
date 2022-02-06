string = input()
dictionary = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
dic = dict()
cnt = 0
l = h = 0

for i in dictionary: dic[i] = 0

while ( l < len(string) ):
    if string[l:h] in dictionary:
        cnt += 1
        l = h
        h += 1
    else:
        if h - l >= 3: 
            l += 1
            cnt += 1
        else: 
            if h < len(string): h += 1
            else: 
                l += 1
                cnt += 1

print(cnt)
