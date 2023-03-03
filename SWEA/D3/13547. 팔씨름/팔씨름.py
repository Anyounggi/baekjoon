T = int(input())
for testcase in range(1, T+1):
    s = input()
    n = len(s)
    o_cnt = 0
    x_cnt = 0
    for i in range(n):
        if s[i] == 'o':
            o_cnt += 1
        else:
            x_cnt += 1

    if 8-o_cnt <= 15-n:
        ans = 'YES'
    else:
        ans = 'NO'

    print(f'#{testcase} {ans}')