T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    lst = list(input().split())
    n = (N+1) // 2

    s1 = lst[:n]
    s2 = lst[n:]


    new_lst = []
    for i in range(N//2):
        new_lst.append(s1[i])
        new_lst.append(s2[i])

    if N%2:
        new_lst.append(s1[-1])

    print(f'#{testcase}', *new_lst)