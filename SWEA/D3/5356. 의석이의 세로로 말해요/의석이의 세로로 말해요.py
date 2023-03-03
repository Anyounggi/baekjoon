T = int(input())
for testcase in range(1, T+1):
    arr = [list(input()) for _ in range(5)]

    ans = ''
    for j in range(15):
        for i in range(5):
            if j < len(arr[i]):
                ans += arr[i][j]

    print(f'#{testcase} {ans}')