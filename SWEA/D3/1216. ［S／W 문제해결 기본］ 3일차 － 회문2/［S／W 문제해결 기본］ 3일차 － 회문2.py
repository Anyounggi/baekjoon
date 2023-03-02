def is_pal(a, n):
    for lst in a:
        for i in range(N-n+1):
            for j in range(n//2):
                if lst[i+j] != lst[i+n-1-j]:
                    break
            else:
                return True
    return False


N = 100
for testcase in range(1, 11):
    no = int(input())
    arr = [list(input()) for _ in range(N)]
    _arr = list(map(list, zip(*arr)))

    for length in range(N, 1, -1):
        if is_pal(arr, length) or is_pal(_arr, length):
            break

    print(f'#{testcase} {length}')