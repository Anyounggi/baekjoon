T = int(input())
for testcase in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    lst = []
    for i in range(1, N+1):
        if i not in arr:
            lst.append(i)

    print(f'#{testcase}', *lst)