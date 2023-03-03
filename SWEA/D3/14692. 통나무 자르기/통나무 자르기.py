T = int(input())
for testcase in range(1, T+1):
    N = input()[-1]
    if int(N) % 2:
        ans = 'Bob'
    else:
        ans = 'Alice'
    print(f'#{testcase} {ans}')