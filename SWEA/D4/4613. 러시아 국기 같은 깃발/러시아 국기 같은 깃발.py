T = int(input())
for testcase in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    min_cnt = M*N
    # 3개의 영역으로 나누기...
    for a in range(N-2):            # 첫번째(W) 영역 맨 아래
        for b in range(a+1, N-1):   # 두 번째(B) 영역 맨 아래
            cnt = M*N                 # 각 영역에서 새로 칠하는 횟수
            for i in range(a+1):
                cnt -= arr[i].count('W')
            for i in range(a+1, b+1):
                cnt -= arr[i].count('B')
            for i in range(b+1, N):
                cnt -= arr[i].count('R')

            if cnt < min_cnt:
                min_cnt = cnt

    print(f'#{testcase}', min_cnt)