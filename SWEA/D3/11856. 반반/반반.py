T = int(input())
for testcase in range(1, T+1):
    S = list(input())
    s = list(set(S))
    lst = []
    for i in s:
        lst.append(S.count(i))

    if lst == [2, 2]:
        ans = f'#{testcase} Yes'
    else:
        ans = f'#{testcase} No'

    print(ans)