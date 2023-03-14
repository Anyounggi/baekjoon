T = int(input())
for testcase in range(1, T+1):
    s = [''] + list(input())
    H = int(input())
    num = list(map(int, input().split()))
    for i in range(H):
        s[num[i]] += '-'

    print(f'#{testcase}', ''.join(s))