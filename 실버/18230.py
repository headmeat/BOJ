#2xN 예쁜 타일링
from sys import stdin
input = stdin.readline

beauty = 0
n, a, b = map(int, input().split())
one = list(map(int, input().split()))
two = list(map(int, input().split()))
one.sort()
two.sort()

if n % 2 == 1:
    n -= 1
    a -= 1
    beauty += one[-1]
    del one[-1]

while(n>0):
    ill = yee = 0

    if a>1:
        ill += one[-1] + one[-2]
    if b>0:
        yee += two[-1]

    if ill>yee:
        a -= 2
        beauty += one.pop() + one.pop()
    else:
        b -= 1
        beauty += two.pop()
    
    n -= 2

print(beauty)
