from sys import stdin
input = stdin.readline

ans = 0

def mergeSort(arr):
    global ans
    if len(arr)<=1: return arr

    a_lst = mergeSort(arr[:len(arr)//2])
    b_lst = mergeSort(arr[len(arr)//2:])

    a_idx = b_idx = 0
    tmp_lst = []

    while(a_idx<len(a_lst) and b_idx<len(b_lst)):
        if a_lst[a_idx]<=b_lst[b_idx]:
            tmp_lst.append(a_lst[a_idx])
            a_idx += 1
        else:
            tmp_lst.append(b_lst[b_idx])
            b_idx += 1
            ans += len(a_lst) - a_idx

    while(a_idx<len(a_lst)):
        tmp_lst.append(a_lst[a_idx])
        a_idx += 1
    while(b_idx<len(b_lst)):
        tmp_lst.append(b_lst[b_idx])
        b_idx += 1

    return tmp_lst

n = int(input())
arr = list(map(int, input().split()))
mergeSort(arr)

print(ans)
