for testcase in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for j in range(N):
        i = 0
        while i < 99:
            if arr[i][j] == 1:
                for k in range(i+1, N):
                    if arr[k][j] == 0:
                        continue
                    elif arr[k][j] == 1:
                        break
                    elif arr[k][j] == 2:
                        cnt += 1
                        break
            i += 1

    print(f'#{testcase} {cnt}')