N = int(input())

arr = sorted(list(set([input() for _ in range(N)])), key = lambda x: len(x))
#그냥 sorted()하면 알아서 ord 순으로 정렬됨.
for i in range(len(arr)-1):
    tmp = arr[i]
    idx = i
    for j in range(i+1, len(arr)):
        if len(arr[i]) < len(arr[j]): break

        if len(tmp) == len(arr[j]):
            for k in range(len(tmp)):
                if(ord(tmp[k]) > ord(arr[j][k])):
                    tmp = arr[j]
                    idx = j
                    break
                elif(ord(tmp[k]) < ord(arr[j][k])): break
        
    x = arr[i]
    arr[i] = tmp
    arr[idx] = x

for i in arr: print(i)
