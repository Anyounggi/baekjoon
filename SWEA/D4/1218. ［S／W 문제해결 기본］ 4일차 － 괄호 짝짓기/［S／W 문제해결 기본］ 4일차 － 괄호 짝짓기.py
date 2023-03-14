for testcase in range(1, 11):
    N = int(input())
    arr = list(input())
    stack = []
    ans = 1
    for i in range(N):
        if arr[i] in ['(', '{', '<', '[']:
            stack.append(arr[i])
        else:
            if not stack:
                ans = 0
                break
            else:
                if arr[i] == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        ans = 0
                        break
                elif arr[i] == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        ans = 0
                        break
                elif arr[i] == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        ans = 0
                        break
                elif arr[i] == '>':
                    if stack[-1] == '<':
                        stack.pop()
                    else:
                        ans = 0
                        break
    
    print(f'#{testcase}', ans)
