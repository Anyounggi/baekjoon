for test in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    for i in range(N):
        if not M & 1:
            answer = 'OFF'
            break
        M >>= 1
    else:
        answer = 'ON'
    print(f'#{test} {answer}')