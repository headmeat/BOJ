from sys import stdin
input = stdin.readline

t = int(input())

def find(x):
    global parent

    if x not in parent.keys():
        parent[x] = x
        size[x] = 1
        return x
    elif x == parent[x]: return x
    else: 
        parent[x] = find(parent[x])
        return parent[x]

def union(x, y):
    a, b = find(x), find(y)

    if a==b: return

    if size[a] < size[b]:
        parent[a] = parent[b]
        size[b] += size[a]
    else:
        parent[b] = parent[a]
        size[a] += size[b]

    return

parent = {}
size = {}

for _ in range(t):
    f = int(input())
    parent = {}
    size = {}

    for _ in range(f):
        a, b = input().rstrip().split()

        union(a, b)
        print(max(size[parent[a]], size[parent[b]]))
