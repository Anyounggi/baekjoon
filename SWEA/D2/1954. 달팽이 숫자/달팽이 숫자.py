di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    i = j = k = 0
    for num in range(1, N*N+1):
        arr[i][j] = num
        ni = i + di[k]
        nj = j + dj[k]
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0:
            i, j = ni, nj
        else:
            k = (k+1) % 4
            i, j = i+di[k], j+dj[k]
            
    print(f'#{testcase}')
    for lst in arr:
        print(*lst)
