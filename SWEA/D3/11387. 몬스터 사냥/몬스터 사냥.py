T = int(input())
for testcase in range(1, T+1):
    D, L, N = map(int, input().split())

    total = 0
    for i in range(N):
        total += D*(1+i*L*0.01)

    print(f'#{testcase}', int(total))