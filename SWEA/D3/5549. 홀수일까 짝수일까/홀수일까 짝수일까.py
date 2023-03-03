T = int(input())
for testcase in range(1, T+1):
    s = input()[-1]
    if int(s) % 2:
        ans = 'Odd'
    else:
        ans = 'Even'
    print(f'#{testcase} {ans}')