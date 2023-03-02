for testcase in range(1, 11):
    no = int(input())
    s1 = input()
    n = len(s1)
    s2 = input()
    m = len(s2)

    i = cnt = 0
    while i <= m-n:
        if s2[i:i+n] == s1:
            cnt += 1
            i += n
        else:
            i += 1

    print(f'#{testcase} {cnt}')