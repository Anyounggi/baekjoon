T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    num = input()
    cnt = [0] * 10
    for i in num:
        cnt[int(i)] += 1

    min_val = 0
    min_num = 0
    for i in range(10):
        if cnt[i] >= min_val:
            min_val = cnt[i]
            min_num = i

    print(f'#{testcase}', min_num, min_val)