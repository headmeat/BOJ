#Sudoku
arr = [[int(x) for x in input()] for _ in range(9)]

def solve(N, k, lst):#N은 보고있는 로우 #, k는 열 번호(0~8)
    if N == 9:
        for i in range(9): print("".join(map(str, arr[i])))
        exit(0)

    if k == 9:
        arr[N] = lst
        solve(N+1, 0, list(arr[N+1]) if N+1 <=8 else [])
        return

    if lst[k] != 0: solve(N, k+1, lst)
    else:
        rec_x, rec_y = N // 3, k // 3
        tmp = [arr[x][y] for x in range(9) if x//3 == rec_x for y in range(9) if y//3 == rec_y]
        tmp2 = [arr[x][k] for x in range(9) if x != N]
        
        for i in range(1, 10):
            if len(tmp) != 9: print("?")
            if i not in lst and i not in tmp2 and i not in tmp:
                lst[k] = i
                solve(N, k+1, lst)
                lst[k] = 0

    return lst

idx = 0

solve(0, 0, list(arr[0]))
