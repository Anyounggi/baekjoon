for testcase in range(1, 11):
    N, pw = input().split()
    stack = []

    for i in range(int(N)):
        if not stack:
            stack.append(pw[i])
        else:
            if stack[-1] == pw[i]:
                stack.pop()
            else:
                stack.append(pw[i])

    print(f'#{testcase}', ''.join(stack))