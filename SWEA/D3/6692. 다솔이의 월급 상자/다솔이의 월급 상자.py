T = int(input())
for testcase in range(1, T+1):
    N = int(input())

    total = 0
    for i in range(N):
        p, x = map(float, input().split())
        total += p*x

    print(f'#{testcase} {total:6f}')