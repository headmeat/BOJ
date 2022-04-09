from sys import stdin
input = stdin.readline

def solve(l, r):
    global preorder, inorder
    
    mn = arr.index(min(arr[l:r]))

    if l<mn: solve(l,mn)
    if mn+1<r: solve(mn+1, r)
    print(inorder[mn], end=" ")

t = int(input())

for _ in range(t):
    n = int(input())
    preorder=list(map(int,input().split()))
    inorder=list(map(int,input().split()))
    arr = [0 for _ in range(n)]

    for i in range(n):
        arr[i] = preorder.index(inorder[i])

    solve(0,n)
    print()
