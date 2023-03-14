T = int(input())
for testcase in range(1, T+1):
    D, H, M = map(int, input().split())

    M -= 11
    H -= 11
    D -= 11
    if M < 0:
        M += 60
        H -= 1
    if H < 0:
        H += 24
        D -= 1
    if D < 0:
        ans = -1
    else:
        ans = M + H*60 + D*1440
    print(f'#{testcase}', ans)