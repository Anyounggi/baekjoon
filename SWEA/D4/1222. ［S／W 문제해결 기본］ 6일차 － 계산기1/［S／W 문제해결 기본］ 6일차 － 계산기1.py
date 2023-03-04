for testcase in range(1, 11):
    N = int(input())
    s = input()
    stack = []
    result = ''
    for i in range(N):
        if s[i].isdigit():
            result += (s[i])
        else:
            if stack:
                a = stack.pop()
                result += a
            stack.append(s[i])
    result += stack.pop()

    for i in result:
        if i.isdigit():
            stack.append(int(i))
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(a+b)

    print(f'#{testcase}', *stack)