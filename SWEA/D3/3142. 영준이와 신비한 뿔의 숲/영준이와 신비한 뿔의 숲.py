T = int(input())
for testcase in range(1, T+1):
    N, M = map(int, input().split())

    twin = N-M

    print(f'#{testcase} {M-twin} {twin}')