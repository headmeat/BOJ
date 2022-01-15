N = int(input())
lst = list(set(map(int, input().split())))
lst.sort()

print(" ".join(map(str, lst)))
