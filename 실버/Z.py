from sys import stdin
input = stdin.readline

n, r, c = map(int, input().split())

count = 0

def solve(x, y, gap):
    global count

    if x>r or r>=x+gap or y>c or c>=y+gap: 
        count += gap**2
        return

    if x==r and y==c:
        print(count)
        exit(0)

    solve(x, y, gap//2)
    solve(x, y+gap//2, gap//2)
    solve(x+gap//2, y, gap//2)
    solve(x+gap//2, y+gap//2, gap//2)

solve(0, 0, 2**n)
