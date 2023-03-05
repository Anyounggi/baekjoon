for testcase in range(1, 11):
    no = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    i = 99
    j = 0
    while arr[i][j] != 2:
        j += 1

    while i > 0:
        arr[i][j] = 9
        if 0<=j-1<100:
            if arr[i][j-1] == 1:
                j -= 1
                continue
        if 0<=j+1<100:
            if arr[i][j+1] == 1:
                j += 1
                continue
        i -= 1

    print(f'#{testcase}', j)