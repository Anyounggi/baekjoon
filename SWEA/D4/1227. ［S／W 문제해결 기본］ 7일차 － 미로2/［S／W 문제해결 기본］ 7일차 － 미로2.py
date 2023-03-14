from collections import deque

def bfs(i, j):
    arr[i][j] = 1
    Q = deque()
    Q.append((i, j))

    while Q:
        si, sj = Q.popleft()
        for k in range(4):
            ni = si + di[k]
            nj = sj + dj[k]
            if 0<=ni<100 and 0<=nj<100 and arr[ni][nj] != 1:
                Q.append((ni, nj))
                if arr[ni][nj] == 3:
                    return 1
                else:
                    arr[ni][nj] = 1
    return 0

def find_start():
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                return i, j


di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
for testcase in range(1, 11):
    no = int(input())
    arr = [list(map(int, input())) for _ in range(100)]

    a, b = find_start()
    print(f'#{testcase}', bfs(a, b))
