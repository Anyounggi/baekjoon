T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    m = N//2

    cnt = 0
    for i in range(N):
        for j in range(abs(m-i), N-abs(m-i)):
            cnt += arr[i][j]

    print(f'#{testcase} {cnt}')