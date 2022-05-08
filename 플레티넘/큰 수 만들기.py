from sys import stdin
input = stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

numbers = list(map(str, numbers))
numbers.sort(key=lambda x: x*9, reverse = True)

print(int("".join(numbers)))
