T = int(input())
for testcase in range(1, T+1):
    N, A, B = map(int, input().split())
    _min = min(A, B)
    if N-(A+B) > 0:
        _max = 0
    else:
        _max = abs(N - (A+B))
    print(f'#{testcase} {_min} {_max}')