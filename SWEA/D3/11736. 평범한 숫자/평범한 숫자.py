T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    for i in range(1, N-1):
        if min(arr[i-1:i+2]) != arr[i] and max(arr[i-1:i+2]) != arr[i]:
            cnt += 1

    print(f'#{testcase} {cnt}')