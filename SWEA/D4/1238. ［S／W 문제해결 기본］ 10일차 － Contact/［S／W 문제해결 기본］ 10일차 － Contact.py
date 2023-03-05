from collections import deque

def bfs(v):
    Q = deque()
    Q.append(v)
    visited = [0] * 101
    visited[v] += 1

    while Q:
        v = Q.popleft()
        for w in adj_l[v]:
            if visited[w] == 0:
                visited[w] = visited[v] + 1
                Q.append(w)
    return visited


for testcase in range(1, 11):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    adj_l = [[] for _ in range(101)]

    for i in range(N//2):
        s, g = arr[i*2], arr[i*2+1]
        adj_l[s].append(g)

    visited = bfs(S)

    max_val = 0
    max_idx = 0
    for idx, key in enumerate(visited):
        if key >= max_val:
            max_val = key
            max_idx = idx
    print(f'#{testcase}', max_idx)