T = int(input())
for testcase in range(1, T+1):
    s = input()
    stack = []
    for i in range(len(s)):
        if not stack or s[i] not in stack:
            stack.append(s[i])
        else:
            stack.remove(s[i])

    if stack:
        print(f'#{testcase}', ''.join(sorted(stack)))
    else:
        print(f'#{testcase} Good')