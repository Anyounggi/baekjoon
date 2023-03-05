def bfs(i, j):
    Q = []
    Q.append((i,j))

    while Q:
        si, sj = Q.pop(0)
        for k in range(4):
            ni = si + di[k]
            nj = sj + dj[k]
            if 0<=ni<N and 0<=nj<N:
                if ni == 0 and nj == 0: continue
                elif visited[ni][nj] == 0:
                    Q.append((ni, nj))
                    visited[ni][nj] = 1
                    waste_time[ni][nj] = waste_time[si][sj] + arr[ni][nj]
                else:
                    if waste_time[ni][nj] > waste_time[si][sj] + arr[ni][nj]:
                        waste_time[ni][nj] = waste_time[si][sj] + arr[ni][nj]
                        Q.append((ni, nj))





di = [0, 1, 0, -1]     # 우 하 좌 상
dj = [1, 0, -1, 0]
T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    waste_time = [[0] * N for _ in range(N)]


    bfs(0, 0)
    ans = waste_time[N-1][N-1]


    print(f'#{testcase}', ans)