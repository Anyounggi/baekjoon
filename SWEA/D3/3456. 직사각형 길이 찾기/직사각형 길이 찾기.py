T = int(input())
for testcase in range(1, T+1):
    arr = list(map(int, input().split()))
    arr.sort()

    if arr[0] == arr[1]:
        ans = arr[2]
    else:
        ans = arr[0]

    print(f'#{testcase} {ans}')