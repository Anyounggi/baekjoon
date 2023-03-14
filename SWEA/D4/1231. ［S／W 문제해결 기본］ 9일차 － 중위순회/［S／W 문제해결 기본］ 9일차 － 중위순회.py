def inorder(v):
    if v <= N:
        inorder(v*2)
        print(tree[v], end = '')
        inorder(v*2+1)

T = 10
for testcase in range(1, T+1):
    N = int(input())
    tree = [[0] for _ in range(N+1)]

    for i in range(1, N+1):
        arr = input().split()
        tree[int(arr[0])] = arr[1]

    print(f'#{testcase}', end = ' ')
    inorder(1); print()