T = int(input())
for testcase in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    total = 0
    for i in range(K):
        total += arr.pop()
    
    print(f'#{testcase} {total}')