T = int(input())
for testcase in range(1, T+1):
    s = input()
    cnt = 0

    for i in range(len(s)):
        if s[i] == '(':
            cnt += 1
        elif s[i] == ')':
            if s[i-1] == '|':
                cnt += 1
    print(f'#{testcase} {cnt}')