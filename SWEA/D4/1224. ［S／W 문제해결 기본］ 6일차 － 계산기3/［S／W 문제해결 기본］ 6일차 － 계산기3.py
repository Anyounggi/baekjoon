isp = {'*' : 2, '+' : 1, '(' : 0}
icp = {'*' : 2, '+' : 1, '(' : 3}


for testcase in range(1, 11):
    N = int(input())
    s = list(input())
    stack = []
    result = []

    # 후위 표기식으로 변경
    for i in range(N):
        if s[i].isdigit():
            result.append(s[i])

        elif s[i] in ['(', '*', '+']:
            if stack:
                if icp[s[i]] > isp[stack[-1]]:
                    stack.append(s[i])
                else:
                    while icp[s[i]] < isp[stack[-1]]:
                        a = stack.pop()
                        result.append(a)
                    stack.append(s[i])

            else:
                stack.append(s[i])

        # '('가 들어오면 ')'가 나올때까지 연산자 pop, '('는 제거
        elif s[i] == ')':
            while stack[-1] != '(':
                b = stack.pop()
                result.append(b)
            stack.pop()

    # 후위 표기식 계산
    for i in range(len(result)):
        if result[i].isdigit():
            stack.append(int(result[i]))
        elif result[i] in ['*', '+']:
            b = stack.pop()
            a = stack.pop()
            if result[i] == '+':
                ans = a + b
            elif result[i] == '*':
                ans = a * b
            stack.append(ans)
    print(f'#{testcase} {stack[0]}')