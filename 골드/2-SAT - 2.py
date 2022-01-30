N, M = map(int, input().split())

def solve(i, arr):
    if i==N:
        tmp_pre = arr[lst[0][0]-1] if lst[0][0]>0 else int(not arr[abs(lst[0][0])-1])
        tmp_post = arr[lst[0][1]-1] if lst[0][1]>0 else int(not arr[abs(lst[0][1])-1])

        prev = tmp_pre or tmp_post
        if prev == 0: return

        for j in range(1, M):
            pre_x = arr[lst[j][0]-1] if lst[j][0]>0 else int(not arr[abs(lst[j][0])-1])
            post_x  = arr[lst[j][1]-1] if lst[j][1]>0 else int(not arr[abs(lst[j][1])-1])
            
            prev = prev and (pre_x or post_x)
            if prev == 0: return

        print("1")
        print(" ".join(map(str, arr)))
        exit(0)

    arr[i] = 0
    solve(i+1, arr)
    arr[i] = 1
    solve(i+1, arr)

lst = [tuple(map(int, input().split())) for i in range(M)]

solve(0, [0 for _ in range(N)])

print("0")
