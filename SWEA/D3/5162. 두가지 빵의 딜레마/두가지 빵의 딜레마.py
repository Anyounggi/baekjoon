T = int(input())
for testcase in range(1, T+1):
    A, B, C = map(int, input().split())
    print(f'#{testcase} {C//min(A,B)}')