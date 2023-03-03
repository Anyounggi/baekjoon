for testcase in range(1, 11):
    no = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    _arr = list(map(list, zip(*arr)))

    cross1 = 0
    cross2 = 0

    total_lst = []

    for i in range(100):
        total = 0
        for j in range(100):
            total += arr[i][j]
            if i == j:
                cross1 += arr[i][j]
        total_lst.append(total)

    for i in range(100):
        total = 0
        for j in range(100):
            total += _arr[i][j]
            if i == j:
                cross2 += _arr[i][j]
        total_lst.append(total)

    total_lst.append(cross1)
    total_lst.append(cross2)

    print(f'#{testcase} {max(total_lst)}')