T = int(input())
for testcase in range(1, T+1):
    arr = list(map(int,input().split()))
    N = len(arr)

    total = 0
    for i in range(N):
        if arr[i] < 40:
            arr[i] = 40
        total += arr[i]

    print(f'#{testcase} {total // N}')