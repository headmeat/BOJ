from sys import stdin
input = stdin.readline

initial_string = input().rstrip()
bomb_string = list(input().rstrip())
alphabet = [0 for _ in range(128)]
n = len(bomb_string)
stack = []

for i in range(n):
    alphabet[ord(bomb_string[i])] = 1

for i in range(len(initial_string)):
    stack.append(initial_string[i])

    if alphabet[ord(initial_string[i])]==1:
        if len(stack)>=len(bomb_string):
            if stack[len(stack)-n:] == bomb_string:
                for _ in range(n):
                    stack.pop()

if len(stack)==0: print("FRULA")
else: print("".join(map(str, stack)))
