T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    lst = []
    for i in range(N):
        s = int(input())
        lst.append(s)
    n = sum(lst) // N

    cnt = 0
    for i in lst:
        if i < n:
            cnt += n-i
    
    print(f'#{testcase} {cnt}')