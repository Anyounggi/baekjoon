from collections import deque

def find_start():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j


def bfs(i, j):
    Q = deque()
    Q.append((i,j))
    arr[i][j] = 1

    while Q:
        si, sj = Q.popleft()
        for k in range(4):
            ni, nj = si + di[k], sj + dj[k]
            if 0<=ni<N and 0<=nj<N:
                if arr[ni][nj] == 3:
                    return 1
                elif arr[ni][nj] == 0:
                    Q.append((ni, nj))
                    arr[ni][nj] = 1
    return 0

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for testcase in range(1, 11):
    no = int(input())
    N = 16
    arr = [list(map(int, input())) for _ in range(N)]

    x, y = find_start()
    print(f'#{testcase}', bfs(x, y))