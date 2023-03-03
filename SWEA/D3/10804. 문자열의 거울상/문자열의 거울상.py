str_dict = {'b' : 'd', 'd' : 'b', 'p' : 'q', 'q' : 'p'}

T = int(input())
for testcase in range(1, T+1):
    s = input()
    n = len(s)

    ans = ''
    for i in range(n-1, -1, -1):
        ans += str_dict[s[i]]

    print(f'#{testcase} {ans}')