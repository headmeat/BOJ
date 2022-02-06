t = int(input())

for i in range(t):
    string = input()
    stack = []
    sw = True

    for j in string:
        if j == ")":
            if len(stack) == 0:
                sw = False
                break
            else: stack.pop()
        else: stack.append("(")

    if sw == True and len(stack) == 0: print("YES")
    else: print("NO")
