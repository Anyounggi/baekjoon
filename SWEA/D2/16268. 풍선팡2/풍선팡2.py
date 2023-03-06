di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

T = int(input())
for testcase in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]


    max_cnt = 0
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j]
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    cnt += arr[ni][nj]
            if cnt > max_cnt:
                max_cnt = cnt

    print(f'#{testcase}', max_cnt)