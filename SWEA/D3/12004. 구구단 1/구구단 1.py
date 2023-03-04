arr = [0] * 101
for i in range(1, 10):
    for j in range(1, 10):
        arr[i*j] = 1

T = int(input())
for testcase in range(1, T+1):
    N = int(input())

    if arr[N]:
        print(f'#{testcase} Yes')
    else:
        print(f'#{testcase} No')