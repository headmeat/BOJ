from sys import stdin
input = stdin.readline

r, c = map(int, input().split())
arr = [[x for x in input()] for _ in range(r)]
alphabets = [0 for _ in range(26)]
mx = -1

def dfs(v, alphabets, depth):
    if alphabets[ord(arr[v[0]][v[1]])-65] == 1: return
    global mx
    mx = max(mx, depth)
    alphabets[ord(arr[v[0]][v[1]])-65] = 1

    if v[0]-1 >= 0 and alphabets[ord(arr[v[0]-1][v[1]])-65] == 0:
        dfs((v[0]-1, v[1]), alphabets, depth + 1)
    if v[0]+1 < r and alphabets[ord(arr[v[0]+1][v[1]])-65] == 0:
        dfs((v[0]+1, v[1]), alphabets, depth + 1)
    if v[1]-1 >= 0 and alphabets[ord(arr[v[0]][v[1]-1])-65] == 0:
        dfs((v[0], v[1]-1), alphabets, depth + 1)
    if v[1]+1 < c and alphabets[ord(arr[v[0]][v[1]+1])-65] == 0:
        dfs((v[0], v[1]+1), alphabets, depth + 1)
    
    alphabets[ord(arr[v[0]][v[1]])-65] = 0

dfs((0, 0), alphabets, 1)

print(mx)
