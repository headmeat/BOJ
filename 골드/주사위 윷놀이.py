from sys import stdin
input = stdin.readline

dice = list(map(int, input().split()))
board = [[x for x in range(0, 42, 2)], [10, 13, 16, 19, 25, 30, 35, 40], [20, 22, 24, 25, 30, 35, 40], [30, 28, 27, 26, 25, 30, 35, 40]]
best_score = 0

def run(arr):
    global best_score

    horse = [[0 for _ in range(4)] for _ in range(4)]
    flag = [0 for _ in range(4)]
    score = 0

    for i in range(len(arr)):
        h = arr[i]
        if horse[h][flag[h]]>=len(board[flag[h]]): return
        horse[h][flag[h]] += dice[i]
        
        if horse[h][flag[h]]>=len(board[flag[h]]): continue
        
        if flag[h] == 0 and horse[h][flag[h]]%5 == 0 and 5<=horse[h][flag[h]]<=15:
            flag[h] = horse[h][flag[h]] // 5
            horse[h][flag[h]] = 0

        for k in range(4):
            if k==h or horse[k][flag[k]]>=len(board[flag[k]]): continue
            if flag[h]==flag[k] and horse[h][flag[h]]==horse[k][flag[k]]: return
            if flag[h]>0 and flag[k]>0 and horse[h][flag[h]]>0 and horse[k][flag[k]]>0 and board[flag[h]][horse[h][flag[h]]]==board[flag[k]][horse[k][flag[k]]]: return
            if board[flag[h]][horse[h][flag[h]]]==board[flag[k]][horse[k][flag[k]]] and board[flag[k]][horse[k][flag[k]]]==40: return

        score += board[flag[h]][horse[h][flag[h]]]

    best_score = max(best_score, score)

def solve(arr):
    if len(arr)==10:
        run(arr)
        return
    
    for i in range(4):
        arr.append(i)
        solve(arr)
        del arr[-1]

solve([])

print(best_score)
