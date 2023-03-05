T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    _arr = list(map(list, zip(*arr)))

    print(f'#{testcase}')
    for i in range(N):
        print(f'{"".join(_arr[i][::-1])} {"".join(arr[N-1-i][::-1])} {"".join(_arr[N-1-i][::])}')

    