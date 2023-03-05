from collections import deque

def bfs(v):
    visited[v] += 1

    Q = deque()
    Q.append(v)

    while Q:
        v = Q.popleft()
        for w in adj_l[v]:
            if visited[w] == 0:
                bfs(w)


for testcase in range(1, 11):
    no, N = map(int, input().split())
    arr = list(map(int, input().split()))
    adj_l = [[] for _ in range(100)]
    visited = [0] * 100

    for i in range(N):
        s, g = arr[i*2], arr[i*2+1]
        adj_l[s].append(g)

    bfs(0)
    if visited[99]:
        ans = 1
    else:
        ans = 0

    print(f'#{testcase} {ans}')