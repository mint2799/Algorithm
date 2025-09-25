for _ in range(int(input())):
    s = input()
    stack = []
    for i in s:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        print("NO" if len(stack) != 0 else "YES")