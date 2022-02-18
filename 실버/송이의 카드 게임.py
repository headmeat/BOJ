from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cards = []
count = n * k

for i in range(n):
    for j in range(k):
        cards.append((arr[i][j], i))

idx = 0

while len(cards) > 1:
    no, who = cards[idx]
    del cards[idx]
    count -= 1

    if count <= 1: break
    move = (no-1) % count

    if idx + move < len(cards):
        idx += move
    else:
        move -= len(cards) - idx
        idx = 0
        idx += move

card, winner = cards[0]
print(winner + 1, card)
